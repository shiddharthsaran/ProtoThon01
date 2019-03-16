
s=input()
o=int(input("\n1.All Caps\n2.Small Caps\n3.Title Case\n4.Start Case"))
if(o==1):
    s=s.split(" ")
    for i in s:
        print(i.upper(),end=" ")
elif(o==2):
    print(s)
elif(o==3):
    s=s.split(" ")
    for i in s:
        print(i.capitalize(),end=" ")
elif(o==4):
    print(s.capitalize())
else:
    print("Enter a valid option")
