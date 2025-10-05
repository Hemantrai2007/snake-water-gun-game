1'''
snake -1
water 1
gun 0
'''
import random
computer=random.choice([1,0,-1])
youstr=input("enter your choice:")
youdict={"snake":-1,"water":1,"gun":0}
youreverse={-1:"snake",1:"water",0:"gun"}

you=youdict[youstr]

print(f"you chose {youreverse[you]}\n  computer chose {youreverse[computer]}")

if you==computer:
    print("match tied")
else:
    if (you==1 and computer==-1) or (you==0 and computer==1) or (you==-1 and computer==0):
        print("you win")
    else:
        print("computer wins")
        '''or
        if you==1:
            if computer==-1:
                print("computer wins")
            else:
                print("you win")
        elif you==0:
            if computer==1:
                print("computer wins")
            else:
                print("you win")
        elif you==-1:
            if computer==0:
                print("computer wins")
            else:
                print("you win")
        '''
        '''
        or 
        if you==computer:
            print("match tied")
        else:
            if(computer==1 and you==-1)
            print("computer wins")
            elif(computer==0 and you==1)
            print("computer wins")
            elif(computer==-1 and you==0)
            print("computer wins")
            else:
            print("you win")
        '''
        '''
        or
        if you==computer:
            print("match tied")
        elif (you-computer)==2 or (you-computer)==-1:
            print("you win")
        else:
            print("computer wins")
        '''