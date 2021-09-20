# string type variable - 

student_name = 'rokon'
student_date_of_birth = '10-06-1996'
student_address = "Dhaka"

# first function of string - len() - length()
# oprators - equal(==), not equal(!=), greater than(>), less than (<), grater than or eual, (>=), 
# less than or equal(<=)

name = 'rokonrr123456789'
print(len(name))

regid = 'abcd1234'
print(len(regid))

if len(regid) == 8:
    print("Successfull!")
else:
    print("Not Sucessfull!")

# next function : make a string lower case to upper case.

lower_case = 'abcsef'
upper_case = lower_case.upper()
print(upper_case)

upper_case_1 = 'AVCDERERF'
lower_case_1 = upper_case_1.lower()
print(lower_case_1)

mixed_variables = 'abcDEFdfdf'
print(mixed_variables.lower())
print(mixed_variables.upper())

# string function of strip() - 

test_string = 'abcd '
print(len(test_string))

after_strip_variable = test_string.strip()
print(len(after_strip_variable))

print(test_string.strip())

test_variables = 'abc,def'
after_test_variable = test_variables.split('d')
print(after_test_variable)

# indexing at string 
# index in python always starts with 0 and increased by 1. 

test = ' Our Country name is Bangladesh '
print(test.strip())
test_variables = test.strip()
new_test = test_variables[3]
print(new_test)

age = 'aaaaaaa'
print(age.isnumeric())

if (age.endswith('a')):
    print('True')
else:
    print('False')

# replace function in python string

first_string = "Our country capital is Kolkata"
print(first_string)
replaced_string = first_string.replace('Kolkata','Dhaka')
print(replaced_string)

new_replaced_string = first_string.replace('capital is Kolkata','Name is Bangladesh')
print(new_replaced_string)

my_previous_phone_number = '01758014948'
new_phone_number = my_previous_phone_number.replace('01758014948','01313002661')
print(new_phone_number)

# string format function 

name = input("Enter your name: ")
welcome_string = "Welcome back, {} ".format(name)
print(welcome_string)

name = input("Enter your name: ")
adress = input("ENter your address: ")

another_format_string = "My name is {} and i live in {}".format(name,adress)
print(another_format_string)

# \ - front slash - escape sequences

new_string = "Don't disturb \t dgdfgdfgdfgdfgdfg"
new_line_string = "Don't disturb \ndgdfgdfgdfgdfgdfg \ndgdfgdfgdfgdfgdfg \ndgdfgdfgdfgdfgdfg"

print(new_string)
print(new_line_string)



