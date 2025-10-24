
for i in range(1, 11, 1):
    for D in range(10, i, -1):
        print(" ", end=" ")
    for G in range(1, i, 1):
        print("*", end=" ")
    for E in range(1, i, 1):
        print("*", end=" ")
    print()

# Bottom half
for i in range(1, 11, 1):
    for D in range(1, i, 1):
        print(" ", end=" ")
    for G in range(10, i, -1):
        print("*", end=" ")
    for E in range(10, i, -1):
        print("*", end=" ")
    print()

print("\t\t *",end= " ")

for main in range(1,11):
    for L in range(10,main,-1):
        print(" ",end=" ")

    for ML in range(1,main,1):
        print("*",end=" ")

    for R in range(1,main,1):
        print("*",end=" ")
    print()

print("\t\t *",end= " ")
for main in range(1,11):
    for L in range(10,main,-1):
        print(" ",end=" ")

    for ML in range(1,main,1):
        print("*",end=" ")

    for R in range(1,main,1):
        print("*",end=" ")
    print()

for m in range(1, 11):
    print(" " * 7, end="")  # Adds 5 spaces before each row
    for F in range(1, 11):
        print(F, end=" ")
    print()