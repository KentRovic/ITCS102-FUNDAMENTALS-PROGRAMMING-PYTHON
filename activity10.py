name = input("Name Input Here:")
isStudent = input("Are you a student (Y/N):")
fare = eval(input("fee amount:"))

if isStudent.upper() == "Y":
	discount = fare * .2
	new_fare = fare - discount
	print("Hi", name, "Student discount is:", discount, "The Total Discounted Fare Is", new_fare)

else: 
	print("Sorry,", name,"you are not eligible for the student discount") 