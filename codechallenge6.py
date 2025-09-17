val =1 
inp1 = eval(input("type a number here:"))

for y in range (inp1, 0, -1):
    val *= y
    print("the factorial number you input is", val)