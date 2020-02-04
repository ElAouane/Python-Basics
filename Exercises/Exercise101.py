#Create a little program that ask the user for the folowing  details:
#Name
#Hight
#Fav color
#Secret Number

#Capture these inputs
#Print a tailored welcome message to the user
#Print other details it gathered, except the secret number of course.

name = input('HEllo, what is your name?: ')
height = int(input('What is your height?: '))
fav_color = input('What is your favorite color?: ')
secret_number = int(input("What is your secret number?: "))

print("Hello {}, your height is {}, and your favorite color is: {}".format(name, height, fav_color))
