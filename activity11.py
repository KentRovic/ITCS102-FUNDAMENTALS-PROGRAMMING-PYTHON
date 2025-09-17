temp = eval(input("Input Temperature Value Here ->"))


if temp >=1 and temp <=20:
 print("temperature outside is cold")
elif temp >=21 and temp <=30:
 print("temperature outside is lukewarm")
elif temp >=31 and temp <=40:
 print("temperature outside is warm")
elif temp >=41 and temp <=50:
 print("temperature outside is hot")
elif temp >=51:
 print("temperature outside is boiling hot")
else:
 print("invalid temperature")