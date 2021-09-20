#user input in python

# print('Hello') -- 

# Task - 1: Take user input of A person name for vaccine registration
# Task - 2: Take age of that person for resgistration
# Task - 3: Take Nid number of that person to complete the registration

person_name = str(input('Enter your name: '))
person_age = float(input('Enter your age: '))
person_nid = int(input('Enter your NID number: '))

if person_age < 18:
    print('You Are Not Eligible for Registartion.')

elif len(str(person_nid)) != 10:
    print('Youe NID number is not valid.')
else:
    print("Registration Successfull.")
    # save to the database....

#kinds of operator
a = 10
b = 15
c = a + b
d = a - b

# Arithmetic operator
# +,-,*,/
# Assignment Operator
# =, not equal,!=, >=, <=

# Or, and Operator, | , &&

my_roll = float(input('ENter your roll no: '))
print(my_roll)


