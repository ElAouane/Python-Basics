# #Contol flow
# #If statments
# #Control where the code will execute. Depending on conditions.
# #And assertion is something that returns True or False
#
# #Syntax
#
# #if <condition>:
#     # block of code
# #elfi <condition>:
#     #block of code
# #else:
#     #block of code
#
# weather = 'stormy and rainy'
#
# if weather == 'rainy':
#     print('Take umbrella')
# elif weather == 'stormy':
#     print('Take rain coat')
# elif 'rainy' and 'rainy' in weather:
#     print('Stay at home')
# else:
#     print('Take sunglasses')
#
#
age = 14
driver_licence = True
mate = 17

if age >= 18 and driver_licence == True:
    print('You can drive and vote')
elif age >= 18:
    print('You can vote')
elif age <= 16 and mate >= 16:
    print('You cant legally drink but....')
elif driver_licence == True:
    print('You can drive')
else:
    print('You are too young, go back to school')


