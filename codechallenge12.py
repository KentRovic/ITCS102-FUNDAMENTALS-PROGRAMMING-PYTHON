
for m in range(1, 7):  
    for x in range(7, m, -1):
        print(" ", end="")
    for y in range(m, 0, -1):
        print(y, end="")
    for z in range(2, m + 1):
        print(z, end="")
    print()