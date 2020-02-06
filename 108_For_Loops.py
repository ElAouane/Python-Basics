#For loops
#Iteration

#Syntax

#for <placeholder> in <iterable>:
    #block of code
    #more indented lines

cars = ['Skoda Felicia Fun', 'Mustang Boss 429', 'Fiat 500', 'jaguar 420g', 'Aston Martin Vanquish']

for x in cars:
    print(x)


student1 = {'name': 'Arya',
            'stream': 'Many Face',
            'grade': 10}

# for key in student1:
        #print(key) this is the key dictionary
        #student is the dictionary
        #print the student key
#     print(student1[key])

for key in student1:
    print(f"The {key} is {student1[key]}")