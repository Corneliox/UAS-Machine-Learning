import os

# Base directory for datasets
base_dir = r"C:\Users\Pongo\OneDrive\Documents\~Cornel\Vs Code\Python\Sem3\Machine Learning\UAS"

# Datasets to process
datasets = ["train", "val", "test"]

for dataset in datasets:
    images_dir = os.path.join(base_dir, dataset, "images")
    labels_dir = os.path.join(base_dir, dataset, "labels")

    # Get all images and labels
    images = [f.split('.')[0] for f in os.listdir(images_dir) if f.endswith('.jpg')]
    labels = [f.split('.')[0] for f in os.listdir(labels_dir) if f.endswith('.txt')]

    # Find missing labels
    missing_labels = set(images) - set(labels)

    if missing_labels:
        print(f"Missing labels in {dataset}: {missing_labels}")
        for missing_label in missing_labels:
            print(f"Creating empty label file for {missing_label}.jpg")
            empty_label_path = os.path.join(labels_dir, f"{missing_label}.txt")
            # Create an empty label file
            with open(empty_label_path, 'w') as f:
                pass
    else:
        print(f"All images have corresponding labels in {dataset}.")
