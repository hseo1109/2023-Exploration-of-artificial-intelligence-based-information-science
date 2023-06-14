import numpy as np
weights=[86,74,59,95,81,68]
heights=[1.83,1.76,1.59,1.86,1.77,1.73]
bmi=[]
for i in range(6):
    bmi.append(weights[i]/(heights[i]*heights[i]))
    if bmi[i]<18.5:
        bmi[i]="저체중"
    elif 18.6<+bmi[i]<=22.9:
        bmi[i]="정상"
    elif 23.0<=bmi[i]<=24.9:
        bmi[i]="과체중"
    else:
        bmi[i]="비만"
print(f"{bmi}")