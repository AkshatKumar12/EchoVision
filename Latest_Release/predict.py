import torch
from PIL import Image
from transformers import ViTImageProcessor, ViTForImageClassification
import sys

def predict_action(image_path, model_dir="./vit_stanford_40_model"):
    processor = ViTImageProcessor.from_pretrained(model_dir)
    model = ViTForImageClassification.from_pretrained(model_dir)
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
    
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    predicted_label = model.config.id2label[predicted_class_idx]
    
    print(f"Predicted Action: {predicted_label.replace('_', ' ').title()}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        predict_action(sys.argv[1])
    else:
        print("Usage: python predict.py <path_to_image.jpg>")