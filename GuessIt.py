import random

comGuess = random.randint(1,20)
m,fails=0,0
print("I'm thinking of a number between one and twenty...Can you guess it? ")

while m<3:
    try_again = True
    while (try_again == True):
        try:
            userGuess = input()
            userGuess = int(userGuess)
            try_again = False
        except ValueError:
            print("Dude")

    while userGuess<1 or userGuess>20:
        fails+=1
        if fails==1:
            print("Don't be a pain and pick a number within limits, for crying out loud.")
        elif fails==2:
            print("I'm serious, quit playing around.")
        elif fails==5:
            print("This is highly unfunny.")
        elif fails==9:
            print("For the life of you.")                       
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

