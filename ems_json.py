#Employee Management System (EMS) with .json
import json #importing json librery
import os #importing os librery

def clear(): #for clear screen
    os.system('cls' if os.name == 'nt' else 'clear')


emp_dict = {"count":0, "emp_list":[]} #dicttionary that contains count(counts the data) and empty list (used to store data)

def to_create(): #performs json.dump() function
    with open("employee_data.json",'w')as file: #permission to read and write file
            json.dump(emp_dict,file,indent = 4) #write and stores the data into json file
            
def to_read(): #performs json.load() function
    global emp_dict #setting emp_dict global helps to access dict data into function
    if os.path.exists('employee_data.json'): #verifying the existence of the json file
        with open("employee_data.json",'r')as file: #permission to read file
            emp_dict = json.load(file) #fetches the data from json file

# user input 1
def create_emp(): #performs employee creation 
    clear() 
    print("\t__________Create Employee__________\n")
    emp_id = int(input("Enter the ID:- ")) 
    name = str(input("Enter the Name:- "))
    age = int(input("Enter the Age:- "))
    ph_num = int(input("Enter the Phone Number:- "))
    exp = int(input("Enter Employee's Experience:- "))
    grade = str(input("Enter the grade:- "))
    #the above code will take user input and stores to the corresponding variable
    emp_dict['count'] += 1 #counts the data
    emp_dict['emp_list'].append({
        'ID':emp_id,
        'NAME':name,
        'AGE':age,
        'PHONE_NUMBER':ph_num,
        'EXPERIENCE':exp,
        'GRADE':grade
    })#performes append(data) operation to the empty list 'emp_list'
    
    user_input = str(input("Would you like to save these details |(Y/N)|:- ")) #confirms the process through another user input.
    
    if user_input.lower() == 'y': #checking the user iput
        to_create() #performs json.dump() function 
        print(f"\nEmployee: {name} with ID: {emp_id} created successfully")
        
    elif user_input.lower() == 'n':#checking the user iput
        print("\n\t------Process Canceled------ \nEmployee details not created")
    else:
        print(f"\n\t{user_input} Invalid. Try again ")
    
#user input 2
def read_employee(): #performs read employee
    clear()
    print("\t__________Read Employee__________")
    read_emp_det = int(input("\nEnter the Employee_ID to search:-  ")) #taking user input to fetch employee data
    clear()
    for employee in emp_dict['emp_list']: #iterate the emp_list from the dict
        if employee['ID'] == read_emp_det: #checking the user input
            for key,value in employee.items(): #iterate the dict from the emp_list
                print(f"{key} : {value}") #out-put will be a key:value
            to_read() #performs json.load() function
    
    
# user input 3
def search_emp():
    clear()
    print("\t__________Search Employee__________\n")
    print("\n1.NAME 2.AGE 3.PHONE NUMBER 4.EXPERIENCE 5.GRADE") #searchable field
    search_input = int(input("\nEnter the choice ( 1 / 2 / 3 / 4 / 5 ):- ")) #taking user input
    
    if search_input == 1: #check and validate user input
        clear()
        name_input = str(input("\nEnter the name to search:- ")) #name input
        for employee in emp_dict['emp_list']: #iterating 
            if employee.get('NAME') == name_input.lower(): #validating
                for key,value in employee.items(): #iterating 
                    print(f"\n{key} : {value}") #printing result
                print("\n------------------------------------\n")
        to_read()
        
    elif search_input == 2: #check and validate user input
        clear()
        age_input = int(input("\nEnter the age to search:- "))
        for employee in emp_dict['emp_list']:
            if employee.get('AGE') == age_input:
                for key,value in employee.items():
                    print(f"\n{key} : {value}")
                print("\n------------------------------------\n")
        to_read()
                
    elif search_input == 3: #check and validate user input
        clear()
        ph_input = int(input("\nEnter the phone number to search:- "))
        for employee in emp_dict['emp_list']:
            if employee.get('PHONE_NUMBER') == ph_input:
                for key,value in employee.items():
                    print(f"\n{key} : {value}")
                print("\n------------------------------------\n")
        to_read()
        
    elif search_input == 4: #check and validate user input
        clear()
        exp_input = int(input("\nEnter the experience to search:- "))
        for employee in emp_dict['emp_list']:
            if employee.get('EXPERIENCE') == exp_input:
                for key,value in employee.items():
                    print(f"\n{key} : {value}")
                print("\n------------------------------------\n")
        to_read()

    elif search_input == 5: #check and validate user input
        clear()
        grd_input = int(input("\nEnter the experience to search:- "))
        for employee in emp_dict['emp_list']:
            if employee.get('GRADE') == grd_input:
                for key,value in employee.items():
                    print(f"\n{key} : {value}")
                print("\n------------------------------------\n")
        to_read()
    else:
        print(f"\n\tE-ID[{search_input}] INVALID")
                
    
#user input 4
def display_all_emp(): #performs display all employee details
    clear()
    print("\n\t-----------All Employee Details-----------")
    for emp_det in emp_dict['emp_list']: #iterate the emp_list from the dict
        print('\n',emp_det) #printing the list that contain a dictionary data
    to_read() #performs json.load() function

#user input 5
def update_emp_det(): #performs the update function
    clear()
    print("\t__________Update Employee__________\n")
    read_emp_det = int(input("Enter the Employee_ID to search:-  ")) #taking user input to fetch employee data
    for employee in emp_dict['emp_list']:#iterate the emp_list from the dict
        if employee['ID'] == read_emp_det:#checking the user input
            for key,value in employee.items():#iterate the dict from the emp_list
                print(f"{key} : {value}")#out-put will be a key:value
            to_read()#performs json.load() function
                
            print("\n------TO UPDATE------")
            print("\n1.ID 2.NAME 3.AGE 4.PHONE NUMBER 5.EXPERIENCE 6.GRADE") #updatable field
            update_input = int(input("\nEnter the choice ( 1 / 2 / 3 / 4 / 5 / 6 ):- ")) #taking user input
            
            if update_input == 1: #employee ID #validating user input
                input_1 = int(input("\nEnter new ID:- "))
                employee['ID'] = input_1 #updating previous data with the user input
                print(f"\nEmployee ID:{read_emp_det} Updated to Employee ID:{input_1}")
                to_create() #performs json.dump() function

            elif update_input == 2: #employee NAME #validating user input
                input_2 = str(input("\nEnter new NAME:- "))
                employee['NAME'] = input_2 #updating previous data with the user input
                print(f"\nEmployee name: {employee['NAME']} Updated to Employee name:{input_2}")
                to_create() #performs json.dump() function
            
            elif update_input == 3: #employee AGE #validating user input
                input_3 = str(input("\nEnter new AGE:- "))
                employee['AGE'] = input_3 #updating previous data with the user input
                print(f"\nEmployee name: {employee['AGE']} Updated to Employee name:{input_3}")
                to_create() #performs json.dump() function
                
            elif update_input == 4: #employee PHONE NUMBER #validating user input
                input_4 = str(input("\nEnter new PHONE NUMBER:- "))
                employee['PHONE_NUMBER'] = input_4 #updating previous data with the user input
                print(f"\nEmployee name: {employee['PHONE_NUMBER']} Updated to Employee name:{input_4}")
                to_create() #performs json.dump() function
                
            elif update_input == 5: #employee EXPERIENCE #validating user input
                input_5 = str(input("\nEnter new PHONE NUMBER:- "))
                employee['EXPERIENCE'] = input_5 #updating previous data with the user input
                print(f"\nEmployee name: {employee['EXPERIENCE']} Updated to Employee name:{input_5}")
                to_create() #performs json.dump() function
                
            elif update_input == 6: #employee GRADE #validating user input
                input_6 = str(input("\nEnter new PHONE NUMBER:- "))
                employee['GRADE'] = input_6 #updating previous data with the user input
                print(f"\nEmployee name: {employee['GRADE']} Updated to Employee name:{input_6}")
                to_create() #performs json.dump() function
            else: 
                print(f"\n\t{update_input} INVALID") #performs when the user input dosnt match with te data

#user input 6
def delete_employee(): #performs the delete function
    clear()
    print("\t__________Update Employee__________\n")
    read_emp_det = int(input("Enter the Employee_ID to search:-  ")) #taking user input to fetch employee data
    for employee in emp_dict['emp_list']:#iterate the emp_list from the dict
        if employee['ID'] == read_emp_det:#checking the user input
            for key,value in employee.items():#iterate the dict from the emp_list
                print(f"{key} : {value}")#out-put will be a key:value
            to_read()#performs json.load() function
            
            user_input = str(input(f"\nWould you like to remove Employee ID[{read_emp_det}]:(Y/N):- ")) #taking user input
            if user_input.lower() == 'y': #checking the user input
                emp_dict['emp_list'].remove(employee) #performs the remove method
                emp_dict['count'] -= 1 #same time changing the count details
                print(f"\nEmployee with ID[{read_emp_det}] removed successfuly")
                to_create() #performs json.dump() function
                break
            elif user_input.lower() == 'n':
                print("\n\t------Process cancelled------")
                continue
            else: #performs when the user input dosnt match with te data
                print(f"\n\t{user_input} INVALID")
        else:
            print(f"\n\tE-ID[{read_emp_det}] INVALID")
                   
def main():
    clear()
    to_read()
    while True:
        print("""
              =====Employee Management System (EMS)=====\n
    1.Create Employee
    2.Read Employe
    3.Search Employee with specific key
    4.Display All Employee 
    5.Update Employee Details
    6.Delete Employee
    0.Exit
              """) #options 
        user_input = int(input("Enter Any choice:|1/2/0|:- ")) #taking user input 

        if user_input == 1: #check and validate user input
            clear()
            create_emp() #performs the update function
            
        elif user_input == 2: #check and validate user input
            clear()
            read_employee() #performs the update function
            
        elif user_input == 3: #check and validate user input
            search_emp()
            
        elif user_input == 4: #check and validate user input
            clear()
            display_all_emp() #performs the update function
        
        elif user_input == 5: #check and validate user input
            clear()
            update_emp_det() #performs the update function
            
        elif user_input == 6: #check and validate user input
            clear()
            delete_employee() #performs the update function
            
        elif user_input == 0: #check and validate user input
            clear()
            user_input_2 = str(input("Would you like to exit the program:|Y/N|:- ")) #performs a condiion
            
            if user_input_2.lower() == 'y':
                print("\n\t__________Exiting.... |HAND|__________")
                break
            elif user_input_2.lower() == 'n':
                print("\n\t__________Wlcome Back USER___________")
                continue
            else:
                print("\n\t|INVALID INPUT. Try again!|")
                
if __name__ == "__main__":
    main()