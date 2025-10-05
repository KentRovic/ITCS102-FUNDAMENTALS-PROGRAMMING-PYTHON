
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
