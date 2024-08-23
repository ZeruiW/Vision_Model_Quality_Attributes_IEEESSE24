
from common import load_images_from_directory, preprocess_images, evaluate
from cvt import load_model, predict

# Main execution
path = 'path_to_images_directory'
images = load_images_from_directory(path)
preprocessed_images = preprocess_images(images)
model = load_model()
predictions = [predict(model, img) for img in preprocessed_images]
evaluate(predictions, 'true_labels')  # Placeholder for true labels
