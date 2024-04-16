# #2
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#
#         tmp=arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = tmp
#     print(arr)
#
#
# arr = [64, 25, 12, 22, 11]
# selection_sort(arr)
import time


# # 3
# import random
# import time
#
#
# def generate_dataset(size):
#     dataset = [random.randint(0, 1000) for i in range(0, size, 1)]
#     return dataset
#
#
# def bubble_sort(dataset):
#     n = len(dataset)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if dataset[j] > dataset[j + 1]:
#                 tmp = dataset[j]
#                 dataset[j] = dataset[j + 1]
#                 dataset[j + 1] = tmp
#
#
# def insertion_sort(dataset):
#     for i in range(1, len(dataset)):
#         key = dataset[i]
#         j = i - 1
#         while j >= 0 and key <= dataset[j]:
#             dataset[j + 1] = dataset[j]
#             j -= 1
#             dataset[j + 1] = key
#
#
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#
#         tmp = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = tmp
#
#
# dataset_size = 5000
# dataset = generate_dataset(dataset_size)
#
# bubble_sort_dataset = dataset.copy()
# selection_sort_dataset = dataset.copy()
# insertion_sort_dataset = dataset.copy()
# sorted_sort_dataset = dataset.copy()
#
# start_time = time.time()
# bubble_sort(bubble_sort_dataset)
# bubble_sort_time = time.time() - start_time
#
# start_time = time.time()
# insertion_sort(selection_sort_dataset)
# insertion_sort_time = time.time() - start_time
#
# start_time = time.time()
# selection_sort(selection_sort_dataset)
# selection_sort_time = time.time() - start_time
#
# start_time = time.time()
# python_sorted_dataset = sorted(sorted_sort_dataset)
# python_sorted_time = time.time() - start_time
#
# print(f"Bubble Sort Time: {bubble_sort_time} seconds")
# print(f"Selection Sort Time: {selection_sort_time} seconds")
# print(f"Insertion sort time {insertion_sort_time} seconds")
# print(f"Python Sorted Time: {python_sorted_time} seconds")

# # 4
# import time
# import random
#
#
# def create_dataset(size):
#     return [random.randint(0, 1000000) for i in range(size)]
#
#
# def linear_search(dataset, num):
#     for i in range(0, len(dataset), 1):
#         if dataset[i] == num:
#             return i
#     return -1
#
#
# def binary_search(dataset, num):
#     low, high = 0, len(dataset) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if dataset[mid] == num:
#             return mid
#         elif dataset[mid] < num:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
#
#
# number = random.randint(0, 1000000)
# dataset_size = 1000000
# dataset = create_dataset(dataset_size)
#
# linear_dataset = dataset.copy()
# binary_dataset = dataset.copy()
#
# start_time = time.time()
# linear_search_wow = linear_search(linear_dataset, number)
# end_time = time.time()
# linear_time = end_time - start_time
#
# start_time = time.time()
# binary_search_wow = linear_search(binary_dataset, number)
# end_time = time.time()
# binary_time = end_time - start_time
#
# print(f"Target: {number}")
# print(f"Linear Search Time: {linear_time} seconds")
# print(f"Binary Search Time: {binary_time} seconds")
#
# if linear_time==binary_time:
#     print(f"The time of searching is the same: {linear_time}")


# # 5
#
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def __repr__(self):
#         return f"Student(name={self.name}, age={self.age}, grade={self.grade})"
#
#
# class StudentListSorter:
#     @staticmethod
#     def bubble_sort(students, key='name'):
#         n = len(students)
#         for i in range(n - 1):
#             for j in range(0, n - i - 1):
#                 if getattr(students[j], key) > getattr(students[j + 1], key):
#                     students[j], students[j + 1] = students[j + 1], students[j]
#
#     @staticmethod
#     def insertion_sort(students, key='name'):
#         for i in range(1, len(students)):
#             current_student = students[i]
#             j = i - 1
#             while j >= 0 and getattr(current_student, key) < getattr(students[j], key):
#                 students[j + 1] = students[j]
#                 j -= 1
#             students[j + 1] = current_student
#
#     @staticmethod
#     def selection_sort(students, key='name'):
#         n = len(students)
#         for i in range(n):
#             min_index = i
#             for j in range(i + 1, n):
#                 if getattr(students[j], key) < getattr(students[min_index], key):
#                     min_index = j
#             students[i], students[min_index] = students[min_index], students[i]
#
#
# students = [
#     Student("Alice", 20, 85),
#     Student("Bob", 22, 92),
#     Student("Charlie", 19, 78),
#     Student("David", 21, 95),
# ]
#
# sorter = StudentListSorter()
#
# sorter.bubble_sort(students, key='grade')
# print("Sorted by grades (Bubble Sort):", students)
#
# sorter.insertion_sort(students, key='age')
# print("Sorted by ages (Insertion Sort):", students)
#
# sorter.selection_sort(students, key='name')
# print("Sorted by names (Selection Sort):", students)


def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True


        if not swapped:
            break
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [64, 45, 78,25, 12, 22, 11, 456, 458, 788,2587, 672, 252, 11231]

start_time = time.time()
optimized_bubble_sort(arr)
end_time = time.time()
optimized_bubble_sort_time = end_time - start_time

start_time= time.time()
bubble_sort(arr)
end_time = time.time()
bubble_sort_time = end_time - start_time

print(f"Bubble time time:{bubble_sort_time} {bubble_sort(arr)}")
print(f"Optimized time:{optimized_bubble_sort_time} {optimized_bubble_sort(arr)}")
