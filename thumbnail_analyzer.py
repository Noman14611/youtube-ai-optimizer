from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import torch

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def analyze_thumbnail(image: Image.Image) -> str:
    prompts = [
        "Looks professional",
        "Grabs attention",
        "Too crowded",
        "Needs better contrast",
        "Has clickbait potential"
    ]
    inputs = processor(text=prompts, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1).squeeze()
    max_index = probs.argmax().item()
    return f"💡 AI Suggestion: {prompts[max_index]} (Confidence: {probs[max_index]:.2f})"
