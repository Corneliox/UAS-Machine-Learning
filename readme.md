Final Project by YOLO
---

So yeah this just my note on how This Project progress..

What we should test was 

```py
# Models to train and evaluate
models = {
    "YOLOv3": "yolov3.pt",
    "YOLOv4": "yolov4.pt",
    "YOLOv5x": "yolov5x.pt",
    "YOLOv6": "yolov6.pt",
    "YOLOv7": "yolov7.pt",
}
```

### Desember 18, 2024
#### Project Progress Update
I have made some progress on the project, but I still have a lot of work to do.

It was a rough day tho, i was confused how do we can work together, but collab help em and richard..

What we do today, 
- Make a anotation per image was totaled about 413, with some eror...
- We also have some issue with the data, some of the images are not clear, and we need to reshape, hopefully this work well end
---
### Desember 19, 2024
#### Project Progress Update
We Have already finished our last anotation and we faced error on Colab at first try because there's a lot.. What we found today

- Cpu usage == 12+ (lead to collab eror)

We Try to use T4, but still have eror on label, and overwhelmed epoch and batch

- We put the epoch down from 50 into 12 (based on our dataset loss for our last cifar project) 
- We put Batch from 30 to 8

Its work, but we got eror label 0, and we found the problem is at 1.0 split data which was "labels" and not "label"

We were gonna fix it tommorow

---
### Desember 20, 2024
#### Project Progress Update
Ohohoho..  Heee?? still no labels found? anyway.. its running right now

So.. After tying again.. its our fault that we dont read the YOLO docs.. Which they request the "labels" and not "label" folder.. so its now all fixed

The result of yolo v3 try tonight is 

- System RAM Usage = 7.4 GB
- GPU RAM Usage is = 9.8 GB - 12 GB

We will see if Epoch 12 and Batch 8 was good enough (24/26/30 Is the best (based on cifar))

##### 9.10 PM 
Its Eror Again heheh, now the problem is on the metrics collection, will try with the best param after this (26)

##### 9.15 PM 
Let's Try Againn !! - Btw, im trying the new Format of readme eheh

Result 
- We need larger memory for larger batch sooo, i till try with 20? Lets try, if not work i will just jump into 12

##### 9.23 PM

Woops E/B = 12/20 is working tho xD, even the GPU Reach peach of 14,4/15 (Very Closeee to error) but it works ehehehh.. Lets wait for the result :D

##### 10.08 PM
After several Error i can save all the logs and all T-T i will try for v4 after thiss Wish me Luck!!

##### 10.15 PM
Yolo V4 is Missing Error tho, no models found Yolo V4... and then im trying with Yolo5x

what i found 
- Yolo5x use E/B = 12/16, its reach peak 15.3/15 GB of GPU RAM before, so yeah
- If u see the report later, it said it using 15.4 G GPU_mem tho hahahahh, God so Good to me that its nor crashing

Wish me luck so this program can run well

##### 10.36 PM 
YOLO V5x is done with some adjustment before but its fine

##### 11.13 PM 
Repair the parameter, and now its ready to take the other YOLO... Thnaks GOD its already done.. 

Will continue this project tommorow

--- 
### Desember 21, 2024
#### Project Progress Update
Today we were so busy hahahha, and its only me (Cornel) who available for training

Now its v6 and v7 turn tho heheheh

##### 8.00 PM
I found that the model is'nt available for 4, 6, and 7..

Summary of available models:
- yolov8n
- yolov8s
- yolov8m
- yolov8l
- yolov8x
- yolov5n
- yolov5s
- yolov5m
- yolov5l
- yolov5x
- yolov3
- yolov3-spp
- yolov3-tiny

```py
from ultralytics import YOLO

# Define a list of potential model names to check
models_to_check = [
    # YOLOv8 Models
    "yolov8n", "yolov8s", "yolov8m", "yolov8l", "yolov8x",
    
    # YOLOv5 Models
    "yolov5n", "yolov5s", "yolov5m", "yolov5l", "yolov5x",
    
    # YOLOv4 Models
    "yolov4", "yolov4-csp", "yolov4-p5", "yolov4-p6", "yolov4-p7",
    
    # YOLOv3 Models
    "yolov3", "yolov3-spp", "yolov3-tiny",
    
    # YOLOv6 Models
    "yolov6n", "yolov6s", "yolov6m", "yolov6l",
    
    # YOLOv7 Models
    "yolov7", "yolov7-tiny", "yolov7x",
]

# List to store available models
available_models = []

print("Checking available models in Ultralytics...")

# Loop through the model list and test loading
for model_name in models_to_check:
    try:
        YOLO(f"{model_name}.pt")  # Attempt to load the model
        available_models.append(model_name)
        print(f"✅ Model available: {model_name}")
    except Exception as e:
        print(f"❌ Model not available: {model_name}")

# Summary of results
print("\nSummary of available models:")
if available_models:
    for model in available_models:
        print(f"- {model}")
else:
    print("No models are available.")
```

So yeah ill jump into... Nah I think i will take a break today hehehe.. Goodnight All, God Bless

###### 8.37 PM 
There is a major problem happen on logging, which was happen because too many dir, and simply i dont take a look on it, i should remake all the code of logging the data after this hahahah, will update when im done

##### 11.03 PM
I need RESTTT T-T

---
### Desember 22, 2024
#### Project Progress Update

##### 08.00 PM
Result Exraction Complete via extracting using the `shutil` library

--# Thanks to Raka for the raw Ideas :D