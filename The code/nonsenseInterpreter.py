#A python fork of nonsense esolang originally created in C++ by EagleOnGithub
#Work in progress!!!
from collections import deque
import time

print("Do Ctrl+C to stop the program.")

while True:
    ACC = 0

    UI = input("Commands: ")
    print("Processing..")

    DUI = deque(UI)

    IP = 0

    fin = str()

    while IP!=len(DUI):
        x=DUI[IP]
        if x=="+":
            ACC+=1
        elif x=="-":
            ACC-=1
        elif x==".":
            ACC=ACC
        elif x=="#":
            fin+=str(ACC)
        elif x=="*":
            ACC=ACC**2
        elif x=="$":
            fin+=chr(ACC)
        elif x=="!":
            ACC=0
        elif x=="^":
            ACC+=10
        elif x=="&":
            ACC-=10
        elif x==",":
            temp1 = str()
            while len(temp1)!=1:
                temp1=input("Please enter input (1 character long): ")
            ACC=ord(temp1)
        elif x=="}":
            time.sleep(1)
        elif x=="%":
            IP=0
        IP+=1

    print(f"Output: {fin}")
