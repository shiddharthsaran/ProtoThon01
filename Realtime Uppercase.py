import keyboard  
String="abcdefghijklmnopqrstuvwxyz"
List=[]
for i in String:
    List.append(i)
while(True):
    try:
        for j in List:
            if keyboard.is_pressed(i):  
                print(j.upper(),end='\r')
                continue
            else:
                pass
    except:
        break  