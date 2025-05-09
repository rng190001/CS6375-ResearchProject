# CS6375-ResearchProject
Visual Language Model (LLaVA) focusing on testing different parsing techniques from generated responses. This study investigates three different parsing techniques: rule-based parsing, dependency parsing and lastly sequence to sequence parsing to determine their efficiency in converting LLM generated responses into executable UI actions 

## ![image](https://github.com/user-attachments/assets/94aa549a-378f-406b-8059-01f83bcd3e25) Datasets

- [Dataset Link for Images](huggingface.co/datasets/ivelin/ui_refexp_saved?row=1)
- [Dataset Link for Custom Generated Prompts, VLM Repsonses, and Handwritten JSON Formatted Structure](https://github.com/rng190001/CS6375-ResearchProject/blob/main/VLM_responses_Baseline_i.csv)
- [Dataset Link for Generated Rule-Based Parsing Output](https://github.com/rng190001/CS6375-ResearchProject/blob/main/VLM_responses_Baseline_SemanticParser.csv)
- [Dataset Link for Generated Dependency Parser Output](https://github.com/rng190001/CS6375-ResearchProject/blob/main/VLM_responses_Baseline_DependencyParser.csv)
- [Dataset Link for Training Seq2Seq Parser](https://github.com/rng190001/CS6375-ResearchProject/blob/main/VLM__training_responses.csv)
- [Dataset Link for Generated Seq2Seq Parser Output](https://github.com/rng190001/CS6375-ResearchProject/blob/main/Seq2SeqParsingOutput2.csv)

## ![image](https://github.com/user-attachments/assets/0331e4f6-4804-4b41-9d0b-0c28e746c5e9) Implemenation
- LLaVa Model
    - Model Used: LLaVA 1.6 Multi-Modal Language Model
    - Challenge: Resource Limitations
    - Solution: Kaggle GPU T4 x 2 processor & loaded the model with the use of bitsandbytes
    - Prompt Engineering:
      - Key Challenge: VLM hallucinated on key UI elements in output
      - Final Effective Prompt: Fed in the dataset prompt and UI image, specifically asked the model to not make assumptions
      
- Rule-Based Parser
    - Libraries Used: Regex (re python)
    - Challenge: Identifying all of the necessary patterns to structure the parser
      
- Dependency Parser
    - Libraries Used: SpaCy, NLTK
    - Strategy: Analyze dependency trees and take commonly observable grammar rules 

- Seq2Seq Parser
    - Model Used: BART
    - Challenge: Poor performance on converting VLM responses to desired JSON objects
    - Expanded Training Dataset so that we could fine-tune the BART model
    - Optimizer: AdamW
    - Hyperparameters: 
        - Learning Rate: 2e-5
        - Epochs: 10
        - Early Stopping Patience: 3
        - Gradient Accumulation Steps (for small batch sizes): 2

## ![image](https://github.com/user-attachments/assets/5f8edaea-fc57-479e-87e5-e0dda8788b7b) Evaluation
- TF-IDF Cosine Similarity:
    - TF-IDF vectorizer was used from sklearn python library.
    - Ranks each word based on keyword importance.
    - The vectorizer inputs were fed into the cosine similarity function which resulted in an accuracy score.
    - Offers a **baseline lexical similarity** score between the ground truth and parsed outputs.

- BERT Embedding Cosine Similarity:
    - BERT Embeddings (all-distilroberta-v1 model) were created for each ground truth and parsed outputs.
    - The embeddings were fed into the cosine similarity function which resulted in an accuracy.
    - Offers more of a **context aware** result.  

- Recall Curve & AUC:
    - We developed a custom recall-like curve to see which percentage of each parsing technique surpassed a certain similarity threshold to visualize the parser consistency.
    - An AUC value was computed to see how the overall model performed. An AUC value closer to 1 reflects a better model.

## ![image](https://github.com/user-attachments/assets/e98e73ef-f6f2-4317-b8a5-a2fad8cb28e8) Final Results
- The final overall accuracy score:
    - Weight of 0.2 to the TF-IDF cosine similarity scores
    - Weight of 0.8 to the BERT embedding cosine similarity scores
    - Valued semantic correctness versus lexical correctness

      <img width="202" alt="Screenshot 2025-05-08 at 7 21 33 PM" src="https://github.com/user-attachments/assets/014300fb-ede4-4f5c-ac85-3d86acf0ec9f" />

- Recall Curves and AUCs
    - The AUC scores for each parser are shown below:
        - Rule-based Parsing AUC: **0.7553**
        - Sequence to Sequence Parsing AUC: **0.7225**
        - Dependency Parsing AUC: **0.6937**

      <img width="569" alt="Screenshot 2025-05-08 at 7 23 58 PM" src="https://github.com/user-attachments/assets/796aa830-8a97-4ddc-8cc3-412142878dbd" />

  - Conclusion:
    - Highest AUC --> Rule-Based Parsing
          - In Our implementation this model ended up having the best perfomance
    - Seq2Seq Model has a lot of potential but the lack of data caused the model to decline overall
    - The dependency parser relies on syntactic structure without considering the variability limits performance


      









