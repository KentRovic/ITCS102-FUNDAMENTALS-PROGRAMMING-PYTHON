import random
num = random.randint(1,20)
GuessNum = 0
idk = True

while idk == True:
    inp = int(input("Guess a number between 1-20 : :p  "))
    GuessNum += 1

    if inp == num:
        print("Congrats you guess Right! :D ")
        print(f"the right random number is {num} :O  ")
        print(f"You took {GuessNum} tries :) ")
        break

    else:
        print("Wrong Guess Try Again. -_- ")
        continue