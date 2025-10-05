# #SF
# F = "Kent Rovic"
# M = "Abanilla"
# L = "Loveria"
# print(f"My name is {F} {M} {L}")

# #SOON

val = 0
for y in range (1, 11, 1):
    inp1= eval(input("Type Number Here"))
    if inp1 % 2:
        val += inp1
    print('new odd input to sum is', inp1)
    print("The total of the odd sum you input is", val)