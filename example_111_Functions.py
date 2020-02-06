# Functions

# Functions do one small task --> this make them testable
# It makes your code more readable, maintainable and testable.

#Technical Debpt = When you dont and cant maintain your code

#DRY = DONT REPEAT YOURSELF
#Run a block of code when called

#Syntax
#def <name>(arg,arg2):
#   block of code
#   return something(optional).

#Function no args
def say_hello():
    return 'hello'

print(say_hello())

#Function wit arg
def full_name(name, surname):
    return name.capitalize() + ' '+ surname.capitalize()

print(full_name('hamza', 'el aouane'))

def welcome_message(name, surname):
    full_name_1 = full_name(name, surname)
    welcome_str = say_hello()
    return welcome_str + ' ' + full_name_1

print(welcome_message('hamza', 'el Aouane'))

def add(num1, num2):
    return num1 + num2

print(add(1, 2))