# SDC_Challenge_2
Udacity Self-Driving Car Challenge 2

I made a little score program to test the correlation between human driving steering angle and machine detected steering angle: 

| Team Name|  :1000 |1000:2000|2000:3000|3000:4000|4000:5000|5000:     |
| ---------- |:-------:|:---------:|:---------:|:---------:|:---------:|-----------:|
| autumn     | 0.96445 | 0.97919 | 0.98314 | 0.97338 | 0.97226 |       0.9  |
| komanda    | 0.95624 | 0.97757 | 0.95274 | 0.97820 | 0.97141 |    0.9     |
| rambo      | 0.94746 | 0.96894 | 0.94798 | 0.97984 | 0.95529 | 0.9        |


```
import scipy
import csv
from scipy.stats import pearsonr

x = []
y = []
frame_id = []

#read final_evalution.csv
with open('final_evalution.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x.append(float(row['steering_angle']))
        frame_id.append(row['frame_id'])

# read submission *.csv
with open('rambo.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        y.append(float(row['steering_angle']))

print(scipy.stats.pearsonr(x[:], y[:]))
```
