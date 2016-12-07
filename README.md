# SDC_Challenge_2
Udacity Self-Driving Car Challenge 2 score analysis:

I made a little score program to test the correlation between human driving steering angle and machine detected steering angle.
I broken down the trip into 1000 frame per section, I measure the pearsonr correlation coefficient for each sections and overall scores. 

The interesting I found is:
Team autumn almost lead all the sections, except 3000:4000 and 4000:5000 section. 
Team rambo has some issue at 5000: end section. 

I hope there are more submissions available, so we can do more analysis.

| Team Name |   :1000 |1000:2000|2000:3000|3000:4000|4000:5000|5000:    | overall |
| ----------|:-------:|:-------:|:-------:|:-------:|:-------:|--------:|--------:|
| autumn    | 0.96445 | 0.97919 | 0.98314 | 0.97338 | 0.97434 | 0.95287 | 0.97508 |
| komanda   | 0.95624 | 0.97757 | 0.95274 | 0.97820 | 0.97552 | 0.93064 | 0.97115 |
| rambo     | 0.94746 | 0.96894 | 0.94798 | 0.97984 | 0.97356 | 0.64140 | 0.93332 |



The following code shows how pearson correlation coefficient works. 
```
# calculates the mean
def mean(x):
    sum = 0.0
    for i in x:
         sum += i
    return sum / len(x) 

# calculates the sample standard deviation
def sampleStandardDeviation(x):
    sumv = 0.0
    for i in x:
         sumv += (i - mean(x))**2
    return math.sqrt(sumv/(len(x)-1))

# calculates the PCC using both the 2 functions above
def pearson(x,y):
    scorex = []
    scorey = []

    for i in x: 
        scorex.append((i - mean(x))/sampleStandardDeviation(x)) 

    for j in y:
        scorey.append((j - mean(y))/sampleStandardDeviation(y))

    # multiplies both lists together into 1 list (hence zip) and sums the whole list   
    return (sum([i*j for i,j in zip(scorex,scorey)]))/(len(x)-1)

print(pearson(x[100:1000], y[100:1000]))

```
