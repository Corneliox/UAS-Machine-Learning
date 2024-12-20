import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
images_dir = 'images'
labels_dir = 'label'

train_dir = 'train'
val_dir = 'val'
test_dir = 'test'

# Output directories
for split in [train_dir, val_dir, test_dir]:
    os.makedirs(f'{split}/images', exist_ok=True)
    os.makedirs(f'{split}/label', exist_ok=True)

# All image files
image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]
train_files, temp_files = train_test_split(image_files, test_size=0.3, random_state=42)
val_files, test_files = train_test_split(temp_files, test_size=0.1667, random_state=42)

# Copy images and labels
def copy_files(file_list, split_dir):
    for file in file_list:
        # Copy image file
        shutil.copy(os.path.join(images_dir, file), os.path.join(split_dir, 'images', file))
        
        label_file = os.path.splitext(file)[0] + '.txt'
        src_label_path = os.path.join(labels_dir, label_file)
        dst_label_path = os.path.join(split_dir, 'label', label_file)

        if os.path.exists(src_label_path):
            shutil.copy(src_label_path, dst_label_path)
        else:
            print(f"Label file missing for {file}. Skipping...")

# Copy files to respective directories
copy_files(train_files, train_dir)
copy_files(val_files, val_dir)
copy_files(test_files, test_dir)

print("Data split completed!")
