import random
    
def gamewin(comp,you):
    if comp==you:
        return None
        # print("Game Tie")
    elif comp=='stone':
        if you=='paper':
            return True
            # print("You win")
        elif you=='scissor':
            return False
            # print("You Lose")
    elif comp=='paper':
        if you=='scissor':
            return True
            # print("You win")
        elif you=='stone':
            return False
            # print("You Lose")
    elif comp=='scissor':
        if you=='stone':
            return True
            # print("You win")
        elif you=='paper':
            return False
            # print("You Lose")
    

a= random.randint(1,3)
if a==1:
    comp='stone'
    # print(comp)
elif a==2:
    comp='paper'
    # print(comp)
elif a==3:
    comp='scissor'
    # print(comp)



b=int(input("Enter 1 for scissor, 2 for paper or 3 for stone: "))
print(f"computer chose {comp}")
if b==1:
    you='scissor'
elif b==2:
    you='paper'
elif b==3:
    you='stone'
a=gamewin(comp,you)
if a==None:
    print("Game Tie")
elif a==True:
    print('You won')
elif a==False:
    print('You lose')
            

    
