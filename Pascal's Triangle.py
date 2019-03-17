r=int(input())
p=[]
f=[]
for i in range(1,r+1):
    p=f.copy()
    f.clear()
    for j in range(0,i):
        if(j==0):
            f.append(1)
        elif(j==i-1):
            f.append(1)
        else:
            f.append(p[j-1]+p[j])
    for j in f:
        print(j,end=" ")
    print("")