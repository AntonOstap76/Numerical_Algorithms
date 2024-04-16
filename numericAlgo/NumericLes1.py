# #2
# def fill_and_display_pattern(n):
#     # Initialize a square array with zeros
#     array = [[0] * n for _ in range(n)]
#
#     # Fill the array with the specified pattern
#     for i in range(n):
#         count = 0
#         check = 0
#         for j in range(n):
#             if(check <= i):
#                 count+=1
#                 check+=1
#             array[i][j] = count
#
#     # Display the filled array
#     for row in array:
#         print(' '.join(map(str, row)))
# fill_and_display_pattern(5)


# # 3
# def list_to_nested_list(reg_list, n):
#
#     count = 0
#     check=n
#     nested_list = []
#
#     while check>0:
#         mas=[]
#         for i in range(count, len(reg_list), n):
#             mas.append(reg_list[i])
#         check=check-1
#         count=count+1
#         nested_list.append(mas)
#     print(nested_list)
#
#
# list_to_nested_list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'], 4)


# 4
# def add_of_lists(list1, list2):
#     list3 = []
#     for i in range(len(list1)):
#         list3.append(list1[i])
#     for k in range(len(list2)):
#         list3.append(list2[k])
#     print(list3)
# add_of_lists([100, 90, 80, 70, 60, 50], [49, 39, 29, 19])

# 5
# def add_string_to_element(listStr, str):
#     new_list = []
#     new_str = ''
#     for i in range(len(listStr)):
#         new_str = str + ' ' + listStr[i]
#         new_list.append(new_str)
#         new_str = ''
#     print(new_list)
#
#
# add_string_to_element(['A', 'B', 'C', 'D'], 'Exit')


# 6
# def convert_chart_to_string(list_char):
#     list = ''
#     for i in range(len(list_char)):
#         list = list + list_char[i]
#     print(list)
#
# convert_chart_to_string(['A', 'n', 't', 'o', 'n'])

# 7
# def find_identical_elements(list1, list2):
#     print(set(list1) & set(list2))
#
# find_identical_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])

# 8
# def move_ones_to_end(input_list):
#     count_ones = input_list.count(1)
#     input_list = [element for element in input_list if element != 1]
#     input_list.extend([1] * count_ones)
#
#     return input_list
#
#
# input_list = [3, 5, 1, 4, 1, 2, 11, 7, 1, 5, 9, 1]
#
# result_list = move_ones_to_end(input_list)
#
# print("Original List:", input_list)
# print("Modified List:", result_list)

# 9
# def sum_of_diction(dic):
#     product = 0.0
#
#     for value in dic.values():
#         product = product + value
#     print(product)
#
#
# sum_of_diction({'f1': 4.8, 'f2': 2.4, 'f3': 1.2, 'f4': 0.6})

# 10
# def value_power_four_of_keys(n):
#     result_dict = {i: i ** 4 for i in range(1, n + 1)}
#     print(result_dict)
#
#
# value_power_four_of_keys(6)

# 11
# def unique_value_in_dict(dict):
#     unique_values=set(dict.values())
#     for val in unique_values:
#         print(val)
#
# unique_value_in_dict({1: 'A201', 2: 'B218', 3: 'H018', 4: 'B218', 5: 'H018', 6: 'G123', 7: 'A007', 8: 'G230'})
