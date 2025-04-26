# CS6375-ResearchProject
Visual Language Model (LLaVA) focusing on testing different parsing techniques from generated responses. This study investigates three different parsing techniques: rule-based parsing, dependency parsing and lastly sequence to sequence parsing to determine their efficiency in converting LLM generated responses into executable UI actions 

## 📘 Overview

This notebook performs the following steps:

1.  **Loads a Dataset**
    
    -   Retrieves a dataset from the Hugging Face Hub consisting of mobile UI screenshots and optional metadata.  
    -   [Dataset Link for Images](huggingface.co/datasets/ivelin/ui_refexp_saved?row=1)
        
2.  **Data Cleaning & Prompt Attachment**
    
    -   Filters and cleans dataset entries.
        
    -   Attaches task-specific prompts to each image, framing them as action-based queries (e.g., “What can the user do on this screen?”).
        
3.  **LLaVA Model Inference**
    
    -   Loads the **LLaVA 1.6** multi-modal language model.
        
    -   Processes each image + prompt pair through the model to generate text-based action predictions.
        
4.  **Response Collection & Export**
    
    -   Aggregates model responses.
        
    -   Outputs results (image identifier, prompt, and model response) to a CSV file for use in the second phase of the project (e.g., parsing or structuring step-by-step instructions).

## ![image](https://github.com/user-attachments/assets/94aa549a-378f-406b-8059-01f83bcd3e25) Datasets

- [Dataset Link for Images](huggingface.co/datasets/ivelin/ui_refexp_saved?row=1)
- [Dataset Link for Custom Generated Prompts, VLM Repsonses, and Handwritten JSON Formatted Structure](https://github.com/rng190001/CS6375-ResearchProject/blob/main/VLM_responses_Baseline_i.csv)
- [Dataset Link for Generated Rule-Based Parsing Output](https://github.com/rng190001/CS6375-ResearchProject/blob/main/VLM_responses_Baseline_SemanticParser.csv)
- [Dataset Link for Generated Dependency Parser Output](https://github.com/rng190001/CS6375-ResearchProject/blob/main/VLM_responses_Baseline_DependencyParser.csv)
- [Dataset Link for Training Seq2Seq Parser](https://github.com/rng190001/CS6375-ResearchProject/blob/main/VLM__training_responses.csv)
- [Dataset Link for Generated Seq2Seq Parser Output](https://github.com/rng190001/CS6375-ResearchProject/blob/main/Seq2SeqParsingOutput2.csv)

## ![image](https://github.com/user-attachments/assets/0331e4f6-4804-4b41-9d0b-0c28e746c5e9) Implemenation
- LLaVa Model
- Rule-Based Parser
- Dependency Parser
- Seq2Seq Parser

## ![image](https://github.com/user-attachments/assets/5f8edaea-fc57-479e-87e5-e0dda8788b7b) Evaluation

