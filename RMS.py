import math
a=[]
b=[]
a=input("Eneter Numbers: ").split(",")
for i in a:
    b.append(float(i)**2)
c=0
for i in b:
    c=c+i
d=c/len(b)
print("RMS of the inputs:",math.sqrt(d))