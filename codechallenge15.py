name = input("Hello what is your name?")
anime_titles = []
cont = True

while cont == True:
    AE = input("Type an anime title here:")
    print("Anime Title Added To The List")
    anime_titles.append(AE)
    if AE == "EXIT":
        print("Confirmed Exit, exitting the loop")
        anime_titles.pop()
        print(f"Thank you, {name}! all the listed anime are: {anime_titles}")
        break
    
