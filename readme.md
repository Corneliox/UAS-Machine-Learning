So yeah this just my note on how This Project progress..
---
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

##### 10.08 
After several Error i can save all the logs and all T-T i will try for v4 after thiss Wish me Luck!!

