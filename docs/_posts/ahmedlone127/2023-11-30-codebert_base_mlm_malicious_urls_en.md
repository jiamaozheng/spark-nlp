---
layout: model
title: English codebert_base_mlm_malicious_urls RoBertaForSequenceClassification from DunnBC22
author: John Snow Labs
name: codebert_base_mlm_malicious_urls
date: 2023-11-30
tags: [roberta, en, open_source, sequence_classification, onnx]
task: Text Classification
language: en
edition: Spark NLP 5.2.0
spark_version: 3.0
supported: true
engine: onnx
annotator: RoBertaForSequenceClassification
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained RoBertaForSequenceClassification model, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`codebert_base_mlm_malicious_urls` is a English model originally trained by DunnBC22.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/codebert_base_mlm_malicious_urls_en_5.2.0_3.0_1701364075111.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/codebert_base_mlm_malicious_urls_en_5.2.0_3.0_1701364075111.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python

document_assembler = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

tokenizer = Tokenizer()\
    .setInputCols("document")\
    .setOutputCol("token")  
    
sequenceClassifier = RoBertaForSequenceClassification.pretrained("codebert_base_mlm_malicious_urls","en")\
            .setInputCols(["document","token"])\
            .setOutputCol("class")

pipeline = Pipeline().setStages([document_assembler, tokenizer, sequenceClassifier])

data = spark.createDataFrame([["PUT YOUR STRING HERE"]]).toDF("text")

result = pipeline.fit(data).transform(data)

```
```scala

val document_assembler = new DocumentAssembler()
    .setInputCol("text")
    .setOutputCol("document")

val tokenizer = new Tokenizer()
    .setInputCols("document") 
    .setOutputCol("token")  
    
val sequenceClassifier = RoBertaForSequenceClassification.pretrained("codebert_base_mlm_malicious_urls","en")
            .setInputCols(Array("document","token"))
            .setOutputCol("class")

val pipeline = new Pipeline().setStages(Array(documentAssembler, tokenizer, sequenceClassifier))

val data = Seq("PUT YOUR STRING HERE").toDS.toDF("text")

val result = pipeline.fit(data).transform(data)


```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|codebert_base_mlm_malicious_urls|
|Compatibility:|Spark NLP 5.2.0+|
|License:|Open Source|
|Edition:|Official|
|Input Labels:|[documents, token]|
|Output Labels:|[class]|
|Language:|en|
|Size:|468.3 MB|

## References

https://huggingface.co/DunnBC22/codebert-base-mlm-Malicious_URLs