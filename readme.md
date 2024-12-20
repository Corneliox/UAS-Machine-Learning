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