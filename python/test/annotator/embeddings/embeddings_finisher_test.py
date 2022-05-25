#  Copyright 2017-2022 John Snow Labs
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import os
import unittest

import pytest
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import SQLTransformer

from sparknlp.annotator import *
from sparknlp.base import *
from test.util import SparkContextForTest


@pytest.mark.fast
class EmbeddingsFinisherTestSpec(unittest.TestCase):

    def setUp(self):
        self.data = SparkContextForTest.spark.read.option("header", "true") \
            .csv(path="file:///" + os.getcwd() + "/../src/test/resources/embeddings/sentence_embeddings.csv")

    def runTest(self):
        document_assembler = DocumentAssembler() \
            .setInputCol("text") \
            .setOutputCol("document")
        sentence_detector = SentenceDetector() \
            .setInputCols(["document"]) \
            .setOutputCol("sentence")
        tokenizer = Tokenizer() \
            .setInputCols(["sentence"]) \
            .setOutputCol("token")
        glove = WordEmbeddingsModel.pretrained() \
            .setInputCols(["sentence", "token"]) \
            .setOutputCol("embeddings")
        sentence_embeddings = SentenceEmbeddings() \
            .setInputCols(["sentence", "embeddings"]) \
            .setOutputCol("sentence_embeddings") \
            .setPoolingStrategy("AVERAGE")
        embeddings_finisher = EmbeddingsFinisher() \
            .setInputCols("sentence_embeddings") \
            .setOutputCols("sentence_embeddings_vectors") \
            .setOutputAsVector(True)
        explode_vectors = SQLTransformer(
            statement="SELECT EXPLODE(sentence_embeddings_vectors) AS features, * FROM __THIS__")
        kmeans = KMeans().setK(2).setSeed(1).setFeaturesCol("features")

        pipeline = Pipeline(stages=[
            document_assembler,
            sentence_detector,
            tokenizer,
            glove,
            sentence_embeddings,
            embeddings_finisher,
            explode_vectors,
            kmeans
        ])

        model = pipeline.fit(self.data)
        model.transform(self.data).show()
        # Save model
        model.write().overwrite().save("./tmp_model")
        # Load model
        PipelineModel.load("./tmp_model")
