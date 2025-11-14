#This script processes time-series data from a CSV file, averaging the data over 15-minute intervals and saving the results to a new CSV file.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import csv

Timestep = 15   # Time interval in Minutes
data = pd.read_csv(".../voyager.csv")
data = data.to_numpy()
[length, width] = data.shape
gridspacing = data[0, 1]
modulation = data[0, 2]
output_power = data[0, 3]
laser_frequency = data[0, 5]

current_PMdata = np.zeros([1000, 8])

try:
    # Correctly access the minute attribute directly from the result of pd.to_datetime
    minutes = pd.to_datetime(data[:, 0], errors='coerce').minute % 60
except Exception as e:
    print(f"Error parsing dates: {e}")


csvFile = open(".../voyager_15min_ave.csv", "w", newline="")
csvWriter = csv.writer(csvFile)
cols = ["Time_Start", "Time_End"] + [f"channel{n}" for n in range(1, 9)]

csvWriter.writerow(cols)

i = 0
j = 0

while length - i > 0:
    while (length - i - j) > 0 and (Timestep - ((minutes[i + j] - minutes[i]) + ((minutes[i + j] - minutes[i]) < 0) * 60)) > 0:
        current_PMdata[j, :] = data[i + j, 1:9]  # Adjusted to select only channel1 to channel8
        j = j + 1
    average_PMdata = np.average(current_PMdata[0:j, :], axis=0)  # Adjusted j-1 to j to include the last data point
    data_add = [data[i, 0], data[i + j - 1, 0]] + average_PMdata.tolist()
    csvWriter.writerow(data_add)
    i = i + j
    j = 0

csvFile.close()
