student1 = {
    'name' : 'Morty',
    'stream' : 'Universal Quest',
    'grade' : 12
}

student2 = {
    'name' : 'Summer',
    'stream' : 'Terrestial Quest',
    'grade' : 20
}

#List of dictionary
students_list = [student1, student2]

print(students_list[1])

#Dictionary of a dictionary
student_dict = {
    'student1' : student1,
    'student2' : student2
}
print(student_dict)

#Use the list to print the individual student names
print("###########################")
print(students_list[0]['name'])
print(students_list[1]['name'])
print("###########################")
#Use the dictionary to print individual student names
print("################################")
print(student_dict['student1']['name'])
print(student_dict['student2']['name'])
print("################################")