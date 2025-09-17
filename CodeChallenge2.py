amount= eval(input("deposit amount here: "))

Peso1000 = amount // 1000
amount = amount % 1000

Peso500 = amount // 500
amount = amount % 500

Peso200 = amount // 200
amount = amount % 200

Peso200 = amount // 200
amount = amount % 200

Peso100 = amount // 100
amount = amount % 100

Peso50 = amount // 50
amount = amount % 50

Peso20 = amount // 20
amount = amount % 20

Peso10 = amount // 10
amount = amount % 10

Peso5= amount // 5
amount = amount % 5

Peso1= amount // 1
amount = amount % 1

print("Breakdown Here")
print("Php1000-", Peso1000)
print("Php500-", Peso500)
print("Php200-", Peso200)
print("Php100-", Peso100)
print("Php50-", Peso50)
print("Php20-", Peso20)
print("Php10-", Peso10)
print("Php5-", Peso5)
print("Php1-", Peso1)