# CS6375-ResearchProject
Visual Language Model (Flamingo) focusing on testing different parsing techniques from generated responses 

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
