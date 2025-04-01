from datasets import load_dataset
from transformers import AutoTokenizer, AutoModel, AutoProcessor
import json
import torch
from open_flamingo import create_model_and_transforms
import open_clip
from PIL import Image

# Step 1: Load and preprocess dataset
def load_and_clean_dataset():
    dataset = load_dataset("ivelin/ui_refexp_saved")
    cleaned_data = []

    for entry in dataset["validation"]:
        # Check if entry is a string and attempt to convert to dict
        if isinstance(entry, str):
            try:
                entry = json.loads(entry)
            except json.JSONDecodeError:
                print(f"Warning: Failed to decode JSON string: {entry}")
                continue  # Skip this entry if decoding fails

        cleaned_entry = {
            "image": entry.get("image"),  # Use get() to avoid KeyError if key is missing
            "image_id": entry.get("image_id"),
            "image_file_path": entry.get("image_file_path"),
            "prompt": entry.get("prompt"),
        }
        cleaned_data.append(cleaned_entry)

    return cleaned_data

loaded_data = load_and_clean_dataset()
#print(loaded_data[0])

# Load OpenFlamingo model
def load_flamingo():
    model, image_processor, tokenizer = create_model_and_transforms(
        clip_vision_encoder_path="ViT-L-14-quickgelu",
        clip_vision_encoder_pretrained="openai",
        lang_encoder_path="facebook/opt-2.7b",
        tokenizer_path="facebook/opt-2.7b"
    )
    return model, image_processor, tokenizer

# Step 2: Extract UI elements using OpenFlamingo
def extract_ui_elements(image_file_path, prompt):
    """
    Uses OpenFlamingo to identify UI elements in an image.
    """
    model, image_processor, tokenizer = load_flamingo()

    # Load and process image
    #image = Image.open(image_file_path).convert("RGB")
    image_tensor = image_processor(image).unsqueeze(0)  # Add batch dimension

    # Tokenize prompt
    input_text = f"Identify UI elements in this image. {prompt}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    # Generate response
    with torch.no_grad():
        output = model.generate(
            vision_x=[image_tensor],  # List of image tensors
            lang_x=[[tokenizer.bos_token_id] + input_ids.squeeze(0).tolist()],  # Tokenized input with BOS token
            max_length=50
        )

    extracted_elements = tokenizer.decode(output[0], skip_special_tokens=True)

    return extracted_elements

# Example usage:
image = loaded_data[0]["image"]
prompt = loaded_data[0]["prompt"]
#print(open_clip.list_pretrained())

ui_elements = extract_ui_elements(image, prompt)
print(ui_elements)