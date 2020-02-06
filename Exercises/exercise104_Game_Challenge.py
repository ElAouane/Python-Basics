import time
from Exercises.FizzBuzz_Core_Fun import *
while True:
    count = 0
    user = int(input("Choose a number: "))
    while count < user:
        count += 1
        if fizz_buzz(count):
            print('FizzBuzz')
            continue
        elif toc(count):
            print('TOC')
            continue
        elif pop(count):
            print('POP')
            continue
        print(count)
        time.sleep(0.5)

    ask = input("Would you like to keep playing?: Yes/No")
    if ask.lower() == 'no':
        break



