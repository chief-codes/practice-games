# You are an IT Support Administrator Specialist charged with the task
#  of creating email accounts for new hires  
# Your applicatioon should do the following;
# 1. Generate an email with the following syntax: firstname.lastname@department.company.com
# 2. Determine the department (sales, development, accounting), if none leave blank
# 3. Have set methods to change the password, set the mailbox capacity and 
#    define an alternate email address
# 4. Have get methods to display the name, email and mailbox capacity.


import random
import string
#from Password_Function import password_generator

mailbox_capacity = 100
departments = { #This is dictionary of the departments and their acronyms 
        "Sales":"Sales",
        "Development":"Dev",
        "Account":"Acc",
        "None":""
        }
   
employee_department = ''
    
first_name = input(f"Enter first name: ")

last_name = input(f"Enter last name: ")
    
company_name = input("Enter company name: ")

department_choice = int(input(f"Enter \n (1) for Sales \n (2) for Development \n (3) for Account \
            \n (4) for None \n")) #ask the user to select their department

if department_choice == 1:
        department = departments["Sales"]
    
elif department_choice == 2:
        department = departments["Development"]

elif department_choice == 3:
        department = departments["Account"]

elif department_choice == 4:
        department = departments["None"]

email = (f"{first_name.lower()}.{last_name.lower()}@{department.lower()}.{company_name.lower()}.com")

    
full_name = (first_name + " " + last_name)
print(f"\nHi {full_name},\n Your E-Mail is: {email}")


# Random Password Generator
lower = string.ascii_lowercase # saves lowercase alphabets to lower
upper = string.ascii_uppercase # saves uppercase alphabets to upper
numbers = string.digits # saves numbers to numbers
            #characters = string.punctuation

all = lower + upper + numbers #+ characters.... combines lower, upper and numbers to form a list
temp = random.sample(all, 8) # selects randomly 8 characters and saves them as temp
password = "".join(temp) 
print(f" Your Password is: {password}")

22
print(f" You have {mailbox_capacity} mailbox capacity...")

alternate_options = int(input("\nEnter \n (1) for Alternate E-Mail \n (2) for Change Password \n \
(3) for Change Mailbox Capacity \n (4) for View Profile \n (5) for Exit \n "))

alternate_email = ""
while alternate_options != 5:
    
    if alternate_options == 1:
        alternate_email = input("Enter alternate E-Mail: ")
        alternate_options = int(input("\nEnter \n (1) for Alternate E-Mail \n (2) for Change Password \n \
(3) for Change Mailbox Capacity \n (4) for View Profile \n (5) for Exit \n "))

    elif alternate_options == 2:
        password_vali = input("Enter Password: ")
        if password_vali == password:
            password = input("Enter New Password: ")
        else:
            print("Incorrect Password!!!!")
        alternate_options = int(input("\nEnter \n (1) for Alternate E-Mail \n (2) for Change Password \n \
(3) for Change Mailbox Capacity \n (4) for View Profile \n (5) for Exit \n "))
    
    elif alternate_options == 3:
        mailbox_capacity = input("Enter New Mailbox Capacity: ")
        alternate_options = int(input("\nEnter \n (1) for Alternate E-Mail \n (2) for Change Password \n \
(3) for Change Mailbox Capacity \n (4) for View Profile \n (5) for Exit \n "))

    elif alternate_options == 4:
            print(f"Hi {full_name}, \n E-mail = {email} \n Alternate E-mail = {alternate_email}\
                    \n Password = {password} \n Mailbox Capacity = {mailbox_capacity} ")
    alternate_options = int(input("\nEnter \n (1) for Alternate E-Mail \n (2) for Change Password \n \
(3) for Change Mailbox Capacity \n (4) for View Profile \n (5) for Exit \n "))


else:
    print("Thank You!!!!!")
