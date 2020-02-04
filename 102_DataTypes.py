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

#Special methods for strings
my_string_new = " HeLLoooO this is an amazing string"

#.count()
print(my_string_new.count(''))

#.strip() removes trailing white spaces
print(my_string_new)
print(my_string_new.strip())

#Len() - function not a method()
print(len(my_string_new))
print(len(my_string_new.strip()))

#Capitalize()
print(my_string_new.strip())
print(my_string_new.strip().capitalize())

#EVERY thing upper
print(my_string_new.strip().upper())

#Everything lower
print(my_string_new.strip().lower())

#a method to separate the string into several string
new_string = my_string_new.split()
print(new_string)