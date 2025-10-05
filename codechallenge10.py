print("\t\t *",end= " ")

for main in range(1,11):
    for L in range(10,main,-1):
        print(" ",end=" ")

    for ML in range(1,main,1):
        print("*",end=" ")

    for R in range(1,main,1):
        print("*",end=" ")
    print()