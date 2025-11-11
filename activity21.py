WashingM = True

while WashingM == True:
    CleanCheck = input("Is the Clothes Clean? (Yes or No)  ")


    if CleanCheck.lower() == "no":
        print("Continuing Washing Loop")
        continue
    elif CleanCheck.lower() == "yes":
        print("Stopping Loop.")
        break
    else:
        print("Error Invalid Input (please only put yes or no Thanks :D)")
        continue