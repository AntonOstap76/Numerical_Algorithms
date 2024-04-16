from array import array


# #8
# def list_of_tuple(list1):
#     n = []
#
#     for i in range(0, len(list1), 1):
#         t = list(list1[i])
#         t[2] = 0
#
#         n.append(tuple(t))
#
#     print(n)
#
#
# list_of_tuple([(1, 2, 3), (4, 5, 6), (7, 8, 9)])

# 2
# def occurrences(arr, number):
#     count = 0
#     for i in range(0, len(arr), 1):
#         if arr[i] == number:
#             count = count + 1
#     first_occ = arr.index(number)
#     print(f"How much:{count}")
#     print(f"Where:{first_occ}")
#
#
# occurrences(array('i', [ 5, 6, 2, 12, 56, 2, ]), 2)


# # 3
# def twenty_to_one():
#     l = array('i', [])
#     for i in range(20, 0, -1):
#         l.append(i)
#
#     for num in l:
#         if num % 3 == 0 or num % 7 == 0:
#             l.pop(l.index(num))
#
#     # for j in range(n):
#     #     if l[j] % 3 == 0 and l[j] % 7 == 0:
#     #         arr2.append(j)
#     # for k in arr2:
#
#     print(l)
#
#
# twenty_to_one()

# # 4
# def average_of_input():
#     arr = array('i', [])
#
#     while len(arr) < 15:
#         user_input = input("Enter a number:")
#
#         try:
#             number = int(user_input)
#             arr.append(number)
#         except ValueError:
#             print("Already 15 integers.")
#
#     if len(arr) == 15:
#         mean = sum(arr) / len(arr)
#         print(mean)
#
#
# average_of_input()

# # 5
# def grades():
#     arr = array('i', [])
#     i=1
#     while len(arr) < 5:
#
#         grade_input = input(f"The grade from {i} judge from 0 to 20:")
#         number = int(grade_input)
#         if number >= 0 and number <= 20:
#             arr.append(number)
#         i=i+1
#
#
#
#     minim = min(arr)
#     maxi = max(arr)
#     arr.pop(arr.index(minim))
#     arr.pop(arr.index(maxi))
#     print(sum(arr))
#
#
# grades()

# # 7
# def occurance_in_tuple(tuple, number):
#     arr = array('i', tuple)
#     print(arr)
#     new_arr = array('i', [])
#     for element in range(0, len(arr), 1):
#         if arr[element] == number:
#             new_arr.append(element)
#     print(new_arr)
#
#
# occurance_in_tuple((1, 6, 8, 4, 6, 78, 6, 12, 6), 6)

# # 6
# def create_2d_structure(rows, columns):
#
#         structure = [[0 for _ in range(columns)] for _ in range(rows)]
#
#
#         for i in range(rows):
#             for j in range(columns):
#                 structure[i][j] = (i + 1) * (j + 1)
#
#         return structure
#
# def display_2d_structure(structure):
#
#         for row in structure:
#             print(row)
#
# rows = 5
# columns = 3
#
# structure = create_2d_structure(rows, columns)
# display_2d_structure(structure)

# # 9
# def remove_tuple(tuple):
#     new_tuple_list = [t for t in tuple if len(t) > 0]
#     print(new_tuple_list)
#
#
# remove_tuple([(), (), ('',), ('i1', 'i2'), ('i1', 'i2', 'i3'), ('i4')])

# # 10
# def two_dimensional_tuple(tuple):
#     for i in range(0, len(tuple), 1):
#         sum = 0
#         for j in range(0, len(tuple), 1):
#             sum = sum + tuple[j][i]
#             ave = sum / 4
#         print(ave)
#
#
# two_dimensional_tuple(((1, 2, 3, 4), (10, 15, 25, 35), (70, 80, 90, 100), (-20, -15, -10, -5)))

# #11
# def sort(tuple):
#     list_t=sort(tuple)
#     new_t=tuple(list_t)
#     print(new_t)
