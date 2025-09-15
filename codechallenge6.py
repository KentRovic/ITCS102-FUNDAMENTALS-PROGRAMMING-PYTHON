val = 1
inp1= eval(input("Type Number Here"))
for y in range (inp1, 0, -1):
    val *= y
    print("The Factorial number you input is", val)