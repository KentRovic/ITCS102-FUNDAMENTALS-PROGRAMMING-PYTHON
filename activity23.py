nm =  ['Grapes','Orange','peach','Apple','Strawberry']
nm.append('DragonFruit')   #insert it on the list
print(nm)
nm.pop()    #remove last fruit/item on the list
print(nm)
nm.insert(0,'Lemon')   #Insert it on the start
print(nm)




for i in nm:
    print(f"{i} Squishing each fruit in order given")    #all fruits one by one with 'in the basket' at the last
