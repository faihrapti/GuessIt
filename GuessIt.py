import random

comGuess = random.randint(1,20)
m=0
print("I'm thinking of a number between one and twenty...Can you guess it? ")

while m<3: 
    fails=0
    userGuess = int(input())
    while userGuess<1 or userGuess>20:
        fails+=1
        if fails==1:
            print("Don't be a pain and pick a number within limits, for crying out loud.")
        elif fails==2:
            print("I'm serious, quit playing around.")
        else:
            print("PLease")
        userGuess = int(input())
    m+=1
    if userGuess > comGuess and m<3:
        print("Guess lower, dumbass")
    elif userGuess < comGuess and m<3:
        print("Nope, it's higher")
    elif userGuess == comGuess:
        print("Yup, that's right! Congrats, twat.")
        break
    if m == 3: 
        print(f"God, it was {comGuess}. How hard can it be?")
        break

