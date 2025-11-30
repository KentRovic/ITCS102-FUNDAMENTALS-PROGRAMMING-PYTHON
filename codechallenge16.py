import os
import json


os.system('cls')
print("Student Information System")
print("==================================")

Records_of_Students = {}

while True:
    print("select from the options commands \nA- Add New Info\nP- Print the records\nS- Search for a Record\nD- delete a record\nM- Modify a Record\nI- Import a record \nE- Export a Record\nEXIT- Stop Program")

    choice = input("input choice here ->_->")

    if choice == 'A':
        print('ADDING STUDENT INFO =-) ')
        print("-----------------------------")
        student_id = input("Key Id of the student use this pattern (course-id)")

        first_name=input("input student First name ->_->")
        last_name=input("input student Last Name ->_->")
        course =input("input student Course ->_->")
        email =input("input student Email ->_->")

        Records_of_Students[student_id] = [first_name,last_name,course,email]
        print("DATA SAVED :)")

   
        continue

    elif choice == 'P':
        print("printing student record....")

        for id, record in Records_of_Students.items():
            print(f"STUDENT ID - {id} \n STUDENT RECORD - {record}")
        continue

    elif choice == 'S':
        os.system('cls')
        print("SEARCH STUDENT RECORDS")
        print("**************************************")

        search_id = input("imput search code")
        
        for id in Records_of_Students.keys():
            if search_id in Records_of_Students.keys():

                print("******************************")
                print("\n\nRecord Found")
                print("******************************")

                for i in Records_of_Students[search_id]:
                    print(f"--  {i}  ") 
            else:
                    print("******************************")
                    print("\n\nno record found")
                    print("******************************")

        continue

    elif choice == "D":
        os.system("cls")
        print("Delete Student Record")
        print("*******************************")

        search_id = input("imput id to search code")


        if search_id in Records_of_Students.keys():
                print("******************************")
                print("\n\nRecord Found")
                print("******************************")

                for i in Records_of_Students[search_id]:
                    print(f"--  {i}  ") 
                Records_of_Students.pop(search_id)
        else:
                    print("******************************")
                    print("\n\nno record found")
                    print("******************************")
        continue

    elif choice == "M":
        os.system("cls")
        print("Modify Student Records")
        print("******************************")

        search_id = input("imput id to search code")


        if search_id in Records_of_Students.keys():
                print("******************************")
                print("\n\nRecord Found")
                print("******************************")

                for i in Records_of_Students[search_id]:
                    print(f"--  {i}  ") 
                
                first_name=input("input NEW student First name ->_->")
                last_name=input("input NEW student Last Name ->_->")
                course =input("input NEW student Course ->_->")
                email =input("input NEW student Email ->_->")

                print("DATA UPDATED")

        else:
             print("******************************")
             print("\n\nNo Record Found")
             print("*******************************")
             continue

    elif choice == "I":
        os.system("cls")

        with open('records_of_students.json',"r") as new_file:
            records_of_students_json = json.load(new_file)

        Records_of_Students = records_of_students_json
        print("data Imported from json")

        continue

    elif choice == "E":
       os.system("cls")

       with open ('records_of_students.json',"w") as new_file:
            json.dump(Records_of_Students, new_file, indent=5)
        
       print("Data Successfully Exported to JSON")
       continue

    elif choice == "EXIT":
        print("EXITING Program *_*")
        break
    
    else:
        print("Invalid Output")
        continue