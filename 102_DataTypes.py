#Strings. Strings are a immutable sequence of character
#defined by '' OR ""
my_string = "Amazing grilled fish"
print(my_string, type(my_string))

#JOIN TWO STRINGS
#Concatenation:
firs_name = "Hamza"
last_name = "El Aouane"
print (firs_name + " " + last_name)

#Interpolation
#Inject a string inside another string
name = 'Hamza'
welcome_message = 'Welcome to the DANGERZOOOOOOONEEEEEEE!'

print("{}, {}".format(name, welcome_message))