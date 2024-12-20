import os
import xml.etree.ElementTree as ET

# Paths
xml_file = 'annotations.xml'
images_dir = '/movie_posters'  # Path to images
labels_dir = '/label'  # Path to save YOLO label files
os.makedirs(labels_dir, exist_ok=True)

# Class mapping
class_mapping = {
    "Judul": 0,
    "Sub-Text": 1,
    "Actor/Actress": 2,
    "Subject": 3
}

# Parse the XML file
tree = ET.parse(xml_file)
root = tree.getroot()

# Process each image in the XML
for image in root.findall('image'):
    image_name = image.get('name')
    image_width = int(image.get('width'))
    image_height = int(image.get('height'))
    
    # Label file path
    label_file = os.path.join(labels_dir, os.path.splitext(image_name)[0] + '.txt')
    with open(label_file, 'w') as lf:
        # Process each bounding box
        for box in image.findall('box'):
            label = box.get('label')
            xtl = float(box.get('xtl'))
            ytl = float(box.get('ytl'))
            xbr = float(box.get('xbr'))
            ybr = float(box.get('ybr'))
            
            # Convert to YOLO format
            x_center = (xtl + xbr) / 2 / image_width
            y_center = (ytl + ybr) / 2 / image_height
            width = (xbr - xtl) / image_width
            height = (ybr - ytl) / image_height
            class_id = class_mapping[label]
            
            # Write to label file
            lf.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

print("XML annotations converted to YOLO format!")
