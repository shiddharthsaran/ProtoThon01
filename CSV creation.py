import csv
import os
import random
List= [['#','Num1','Num2','Num3','Num4','Num5']]
Number_of_rows=1
for i in range(0,3):
    File=open(f"file_{i}.csv", "x")
    while os.stat(f"file_{i}.csv").st_size< 2048:
        List.append([Number_of_rows,random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)])
        Number_of_rows=Number_of_rows+1
        with open(f"file_{i}.csv", 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(List)