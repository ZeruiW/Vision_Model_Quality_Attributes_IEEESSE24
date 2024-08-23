
import os
from common import load_images_from_directory, ensure_rgb
from cvt import load_model as load_cvt, preprocess_image as preprocess_cvt, predict as predict_cvt
from vit import load_model as load_vit, preprocess_image as preprocess_vit, predict as predict_vit
from swin import load_model as load_swin, preprocess_image as preprocess_swin, predict as predict_swin
from nvidia import load_model as load_nvidia, preprocess_image as preprocess_nvidia, predict as predict_nvidia
from resnet import load_model as load_resnet, preprocess_image as preprocess_resnet, predict as predict_resnet
from convnext import load_model as load_convnext, preprocess_image as preprocess_convnext, predict as predict_convnext

def main():
    model_choice = input("Choose a model (cvt/vit/swin/nvidia/resnet/convnext): ").strip().lower()
    image_directory = input("Enter the path to the image directory: ").strip()

    # Load images from the directory
    images = load_images_from_directory(image_directory)

    # Model-specific operations
    if model_choice == "cvt":
        model = load_cvt()
        preprocess = preprocess_cvt
        predict = predict_cvt
    elif model_choice == "vit":
        model = load_vit()
        preprocess = preprocess_vit
        predict = predict_vit
    elif model_choice == "swin":
        model = load_swin()
        preprocess = preprocess_swin
        predict = predict_swin
    elif model_choice == "nvidia":
        model = load_nvidia()
        preprocess = preprocess_nvidia
        predict = predict_nvidia
    elif model_choice == "resnet":
        model = load_resnet()
        preprocess = preprocess_resnet
        predict = predict_resnet
    elif model_choice == "convnext":
        model = load_convnext()
        preprocess = preprocess_convnext
        predict = predict_convnext
    else:
        print("Invalid model choice!")
        return

    # Predict for each image
    for img, label, filename in images:
        img_rgb = ensure_rgb(img)
        img_tensor = preprocess(img_rgb)
        prediction = predict(model, img_tensor)
        print(f"Prediction for {filename}: {prediction}")

if __name__ == "__main__":
    main()
