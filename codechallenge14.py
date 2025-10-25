name = input("Hello what is your name?")
sum = 0
odd = ""
cont = True

while cont == True:
    try:
        num = int(input("please imput a number: "))
    except ValueError:
        print("Invalid input")
        continue

    if num % 2 == 1:
        print("odd number detected")
        odd += str(num) + ","
        sum += num
        continue
    elif num == 0:
        print("Loop Terminated")
        break
    elif num % 2 == 0:
        print("Even Number Detected Skipping....")
        continue

print(f"Thank you, {name}! The sum of all odd numbers entered is: {sum}")
print(f"List of all odd numbers entered: {odd}")



