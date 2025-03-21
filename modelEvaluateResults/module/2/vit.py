
from transformers import ViTForImageClassification

def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = ViTForImageClassification.from_pretrained('google/vit-large-patch32-384').to(device)
    model.eval()
    return model

def preprocess_image(img):
    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    transform = transforms.Compose([
        transforms.Resize((384, 384)), # Adjust size for ViT
        transforms.ToTensor(),
        normalize
    ])
    img_tensor = transform(img)
    return img_tensor

def predict(model, img_tensor):
    with torch.no_grad():
        logits = model(img_tensor.unsqueeze(0)).logits
        predicted_label = torch.argmax(logits, dim=1).item()
    return predicted_label
