#This sceript is used to convert BER to Q factor

import math
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from pandas import read_excel, read_csv 
import time
import math
from scipy import special

dataset = read_csv('.../ADVA.csv')
# dataset = read_excel('C:/Users/po19996/OneDrive - University of Bristol/Desktop/OFC_LSTM.xlsx', sheet_name = 'Sheet4',header = 0)
df = dataset.values

BER = df[:,3:4]
#print(BER)
a = math.sqrt(2)
# b = special.erfcinv(2*df)
# Q = a*b
d = []
for i in BER:
    b = special.erfcinv(2*i[0])
    Q = a*b
    c = math.log10(Q)
    Q1= 20*c
    d.append(Q1)
# print(d)

dataframe = pd.DataFrame({'Qfactor':d})
dataframe.to_csv(r".../ADVA_converted.csv", index=False)
