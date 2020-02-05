
#We need more info in out landlord list.
crazy_landlords = ['My. Richards', 'Raj', 'Mr. Shirik', 'Ms Zem']

#We need to add more data!!
#We need to know where our crazy landlords live! we need more informations!
#Introducing.....Dictionaries


#Dictionaries are organized using key and value pairs
# Like a real dictionary
#my_dictionary = {Key: 'Value'...}


# Define a simple dictionary
#Create one dictionary
my_crazy_landlord = {'name': 'Hamza',
                     'Phone': '0785412548',
                     'Email': 'askjdhajks@gmail.com',
                     'Test': ''
                     }



#Read all data of dictionary
print(my_crazy_landlord)

#Read one entry in a dictionary
print(my_crazy_landlord['Phone'])
#Update the in a key
my_crazy_landlord['Phone'] = '+351 235154865'
print(my_crazy_landlord['Phone'])

my_crazy_landlord['address'] = 'Lisboa, Portugal'
print(my_crazy_landlord)
#Destroy one key value. USE POP

#Getting all the keys out
keys = my_crazy_landlord.keys()
Values = my_crazy_landlord.values()
print(keys)
print(Values)

