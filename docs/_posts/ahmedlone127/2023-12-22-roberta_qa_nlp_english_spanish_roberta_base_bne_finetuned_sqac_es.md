---
layout: model
title: Castilian, Spanish roberta_qa_nlp_english_spanish_roberta_base_bne_finetuned_sqac RoBertaForQuestionAnswering from nlp-en-es
author: John Snow Labs
name: roberta_qa_nlp_english_spanish_roberta_base_bne_finetuned_sqac
date: 2023-12-22
tags: [roberta, es, open_source, question_answering, onnx]
task: Question Answering
language: es
edition: Spark NLP 5.2.1
spark_version: 3.0
supported: true
engine: onnx
annotator: RoBertaForQuestionAnswering
article_header:
  type: cover
use_language_switcher: "Python-Scala-Java"
---

## Description

Pretrained RoBertaForQuestionAnswering model, adapted from Hugging Face and curated to provide scalability and production-readiness using Spark NLP.`roberta_qa_nlp_english_spanish_roberta_base_bne_finetuned_sqac` is a Castilian, Spanish model originally trained by nlp-en-es.

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button>
<button class="button button-orange" disabled>Open in Colab</button>
[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/models/roberta_qa_nlp_english_spanish_roberta_base_bne_finetuned_sqac_es_5.2.1_3.0_1703239057119.zip){:.button.button-orange.button-orange-trans.arr.button-icon}
[Copy S3 URI](s3://auxdata.johnsnowlabs.com/public/models/roberta_qa_nlp_english_spanish_roberta_base_bne_finetuned_sqac_es_5.2.1_3.0_1703239057119.zip){:.button.button-orange.button-orange-trans.button-icon.button-copy-s3}

## How to use



<div class="tabs-box" markdown="1">
{% include programmingLanguageSelectScalaPythonNLU.html %}
```python


document_assembler = MultiDocumentAssembler() \
    .setInputCol(["question", "context"]) \
    .setOutputCol(["document_question", "document_context"])
    
    
spanClassifier = RoBertaForQuestionAnswering.pretrained("roberta_qa_nlp_english_spanish_roberta_base_bne_finetuned_sqac","es") \
            .setInputCols(["document_question","document_context"]) \
            .setOutputCol("answer")

pipeline = Pipeline().setStages([document_assembler, spanClassifier])

pipelineModel = pipeline.fit(data)

pipelineDF = pipelineModel.transform(data)

```
```scala


val document_assembler = new MultiDocumentAssembler()
    .setInputCol(Array("question", "context")) 
    .setOutputCol(Array("document_question", "document_context"))
    
val spanClassifier = RoBertaForQuestionAnswering  
    .pretrained("roberta_qa_nlp_english_spanish_roberta_base_bne_finetuned_sqac", "es")
    .setInputCols(Array("document_question","document_context")) 
    .setOutputCol("answer") 

val pipeline = new Pipeline().setStages(Array(document_assembler, spanClassifier))

val pipelineModel = pipeline.fit(data)

val pipelineDF = pipelineModel.transform(data)


```
</div>

{:.model-param}
## Model Information

{:.table-model}
|---|---|
|Model Name:|roberta_qa_nlp_english_spanish_roberta_base_bne_finetuned_sqac|
|Compatibility:|Spark NLP 5.2.1+|
|License:|Open Source|
|Edition:|Official|
|Input Labels:|[document_question, document_context]|
|Output Labels:|[answer]|
|Language:|es|
|Size:|459.7 MB|

## References

https://huggingface.co/nlp-en-es/roberta-base-bne-finetuned-sqac