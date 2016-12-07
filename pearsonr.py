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

#r_row, p_value = scipy.stats.pearsonr(x[:100], y[:100])
print(scipy.stats.pearsonr(x[3000:4000], y[3000:4000]))

