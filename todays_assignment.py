# Todays assignment:
# ----------------
# 1. Take a string as user input and store its length to another variables,  
# print the variables
# 2. Second, check if the variables is greater than 10, if greater than 10, 
# then add another 10 with the variables and print this,
#  otherwise subtract 10 and print this.
# 3. Take a string input, make another string variable from that which value will be the index of 2,5,7,8 
# charecter as a string
# 4. Take a string input as a book name. If the name starts with 'A', then print book found. Otherwise not found.
# Do all of these and send the file to me as assignment..

first_variable = input("Enter the string: ")
length_of_first_variable = len(first_variable)
print("The length of this string is: ",length_of_first_variable)

if length_of_first_variable > 10:
    new_value = length_of_first_variable + 10
    print('The additional value is: ',new_value)
else:
    new_value = length_of_first_variable - 10
    print('The substraction value is: ',new_value)

# string addition, string concatenation

third_string = input("ENter the string: ")
another_string = third_string[2] + third_string [5] + third_string[7] + third_string[8]
print("Another index string is: ",another_string)

book_name = input("Enter the book name: ")
if book_name.startswith('A'):
    print("Book found!")
else:
    print("Not Found!")





