from random import randrange
## universal -> everyone can watch
## pg --> General viewing, but some scenes may be unsuitable for young children
## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
## 15 --> No one younger than 15 may see a 15 film in a cinema.
## 18 --> No one younger than 18 may see an 18 film in a cinema.

movie = {'name' : 'Saw',
          'genre' : 'Horror',
          'Cate' : '12A',
          'min' : 15,
          'rate' : 'pg'}

age = 14

if age < movie['min']:
    print('Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12')
elif age == range(14,15):
    print("No one younger than 15 may see a 15 film in a cinema.")


# rate_of_movie = '12'
# if rate_of_movie == 'universal':
#     print('Everyone can watch this!')
# elif rate_of_movie == 'pg':
#     print('General viewing, but some scenes may be unsuitable for children')
# elif rate_of_movie == '12':
#     print('This film is classified as 12A and children must be accompanied by adults')
# elif rate_of_movie == '15':
#     print('No one younger than 15 can watch this!')
# elif rate_of_movie
# else:
#     print('No one younger than 18 is able to watch this and ID may be required')
