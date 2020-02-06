# The game Fizz AND Buzz!
# multiple of 3 are POP
# multiple of 5 are TOC
# multiples of 3 and 5 are FizzBuzz
# as a user I should be ask for a number,
 # so that I can play the game with my input
# As a player, I should see the game counting up to my number and
 # substituting the multiples of 3 and 5 with the appropriate values,
 # So that I can see if it is working
## EXTRA TASK!
# As a player, I should be able to exit the game using a key word,
  # so that I can stop playing

import time

# play = True
#count = 0
while True:
    count = 0
    user = int(input("Choose a number: "))
    while count < user:
        count += 1
        if count % 5 == 0 and count % 3 == 0:
            print('FizzBuzz')
            continue
        elif count % 5 == 0:
            print('TOC')
            continue
        elif count % 3 == 0:
            print('POP')
            continue
        print(count)
        time.sleep(0.5)

    ask = input("Would you like to keep playing?: Yes/No")
    if ask.lower() == 'no':
        break




