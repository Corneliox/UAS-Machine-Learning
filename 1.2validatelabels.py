import os

# Base directory for datasets
base_dir = r"C:\Users\Pongo\OneDrive\Documents\~Cornel\Vs Code\Python\Sem3\Machine Learning\UAS"

# Datasets to process
datasets = ["train", "val", "test"]

for dataset in datasets:
    labels_dir = os.path.join(base_dir, dataset, "labels")

    print(f"\nValidating labels in {dataset}...")
    # Check each label file
    for label_file in os.listdir(labels_dir):
        if label_file.endswith('.txt'):
            with open(os.path.join(labels_dir, label_file), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) != 5:
                        print(f"Invalid label format in {os.path.join(labels_dir, label_file)}: {line}")
