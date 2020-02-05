#LIST

#Defining a list
#The syntax of a list is []
crazy_landlords = []

#print(type(crazy_landlords))

# We can dynamically define a list
crazy_landlords = ['My. Richards', 'Raj', 'Mr. Shirik', 'Ms Zem']

#Access a item in a list.
#List are organized based on the index
crazy_landlords = ['My. Richards', 'Raj', 'Mr. Shirik', 'Ms Zem']
print(crazy_landlords)
print(crazy_landlords[1])

#We can also redefine at a specific index
#Change Raj to Rajesh
crazy_landlords[1] = 'Rajesh'
print(crazy_landlords)

#Adding a record to the list
crazy_landlords.append('Raj')
crazy_landlords.insert(0, 'Hamza')
print(crazy_landlords)

#Remove an item from a list
crazy_landlords.remove('Raj')
print(crazy_landlords)

#Remove using the index using POP
crazy_landlords.pop() #<= Remove the highest index in the list
crazy_landlords.pop(0) #<= Remove the specific index in the list
print(crazy_landlords)

#We can have mixed data list
hybrid_list = ['JSON', 'Jason', 13, 53, [1, 2]]
print(hybrid_list)

#Tuples
#immutable lists
my_tuple = (2, 'Hello', 22, 'more values')
print(my_tuple)

#Range Slicing



crazy_landlords[0 : 1] #<= from 0 to 1 not inclusive
crazy_landlords[1 : 2] #<= from 1 to 2 not inclusive









