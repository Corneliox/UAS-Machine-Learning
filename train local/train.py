import os
from ultralytics import YOLO
from tqdm import tqdm

# Paths
yaml_path = "dataset.yaml"  # Path to your dataset YAML file
results_dir = "results"     # Directory to save results
os.makedirs(results_dir, exist_ok=True)

# Models to train and evaluate
models = {
    "YOLOv3": "yolov3.pt",
    "YOLOv4": "yolov4.pt",
    "YOLOv5x": "yolov5x.pt",
    "YOLOv6": "yolov6.pt",
    "YOLOv7": "yolov7.pt",
}

# Metrics storage
metrics = {}

# Train, Evaluate, and Collect Metrics for Each Model
for model_name, model_path in tqdm(models.items(), desc="Processing Models"):
    print(f"\nTraining and evaluating {model_name}...")
    
    # Train the model
    model = YOLO(model_path)  # Load pre-trained model
    model.train(
        data=yaml_path,
        epochs=50,
        imgsz=640,
        batch=16,
        name=f"{model_name}_detection",
        save_dir=os.path.join(results_dir, model_name)
    )
    
    # Validate the model
    val_results = model.val()
    
    # Collect metrics
    metrics[model_name] = {
        "AP50": val_results["metrics/mAP50"],  # Average Precision at IoU=0.50
        "AP": val_results["metrics/mAP50-95"], # Average Precision (IoU=0.50:0.95)
        "Precision": val_results["metrics/precision"],
        "Recall": val_results["metrics/recall"],
        "F1-Score": val_results["metrics/F1"],
        "IoU": val_results["metrics/mIoU"],  # Mean IoU
        "Loss": val_results["metrics/loss"],
        "Speed": val_results["metrics/speed"],
    }
    
    # Save validation plots
    model.plot_results(save_dir=os.path.join(results_dir, model_name))

# Display the metrics
print("\nFinal Metrics:")
for model_name, model_metrics in metrics.items():
    print(f"\nModel: {model_name}")
    for metric, value in model_metrics.items():
        print(f"  {metric}: {value:.4f}")
