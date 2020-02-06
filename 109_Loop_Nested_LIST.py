normal_list = [ 1, 2, 3, 5]
embedded_list = [[1, 2, 3], [4, 5, 6]]

# for num in embedded_list:
#     print(num * 3,5)
#
# for data in embedded_list:
#     print(data)
#     for num in data:
#         print(num)

dict_data = {1: {'name': 'Stanley ho',
                 'money': '$0.05'},
             2: {'name': 'Jeff Bezzos',
                 'money': '$0.08'},
             3:{'name': 'Trump',
                 'money': '$0.02'}
             }

#objective
#--> name
#--> money * 4000000

for key_dict1 in dict_data:
    #print(key_dict1)
    sub_dict = dict_data[key_dict1]
    print(sub_dict['name'])
    money_var = float(sub_dict['money'].replace('$', '')) * 4000000
    money_var = str(money_var)
    print('$' + money_var)

