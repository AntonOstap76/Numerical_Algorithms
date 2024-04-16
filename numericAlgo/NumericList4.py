# # 2
# import random
# import matplotlib.pyplot as plt
#
#
# def generate_ascending_dataset(n):
#     return list(range(0, n, 1))
#
#
# def generate_descending_dataset(n):
#     return list(range(n, 0, -1))
#
#
# def generate_unsorted_dataset(n):
#     return random.sample(range(0, n), n)
#
#
# def time_quicksort(arr):
#     start_time = time.time()
#     quicksort(arr)
#     return time.time() - start_time
#
#
# def time_merge_sort(arr):
#     start_time = time.time()
#     merge_sort(arr)
#     return time.time() - start_time
#
#
# def time_heap_sort(arr):
#     start_time = time.time()
#     heap_sort(arr)
#     return time.time() - start_time
#
#
# import time
# import random
#
#
# # Quicksort algorithm
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#     less = [x for x in arr[1:] if x <= pivot]
#     greater = [x for x in arr[1:] if x > pivot]
#     return quicksort(less) + [pivot] + quicksort(greater)
#
#
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]
#
#         # Recursive call on each half
#         merge_sort(left_half)
#         merge_sort(right_half)
#
#         # Merge the sorted halves
#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1
#
#         # Check for any remaining elements in left_half
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
#
#         # Check for any remaining elements in right_half
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1
#
#
# def heapify(arr, n, i):
#     largest = i  # Initialize largest as root
#     left_child = 2 * i + 1
#     right_child = 2 * i + 2
#     # Check if left child exists and is greater than the root
#     if left_child < n and arr[left_child] > arr[largest]:
#         largest = left_child
#         # Check if right child exists and is greater than the largest so far
#     if right_child < n and arr[right_child] > arr[largest]:
#         largest = right_child
#         # Swap the root (largest) with the largest child and recursively heapify
#     # the
#     # affected
#     # subtree
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#     heapify(arr, n, largest)
#
#
# def heap_sort(arr):
#     n = len(arr)
#     # Build a max heap
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#     # Extract elements one by one
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]  # Swap
#         heapify(arr, i, 0)
#
#
# datasets = [200, 500, 1000]
# sorting_algorithms = ['QuickSort', 'MergeSort', 'HeapSort']
# for size in range(0,len(datasets), 1):
#     ascending_data = generate_ascending_dataset(200)
#     descenting_data = generate_descending_dataset(200)
#     unsorted_data = generate_unsorted_dataset(200)
#
#     times = []
#
#     times.append(time_quicksort(unsorted_data.copy()))
#
#     times.append(time_quicksort(ascending_data.copy()))
#
#     times.append(time_quicksort(descenting_data.copy()))
#
#
#
#     for algorithm in range(0, 3, 1):
#         plt.plot(datasets, times, label="algorithm")
#
#     plt.xlabel('Dataset Size')
#     plt.ylabel('Execution Time (s)')
#     plt.title(f'Time Complexity of Sorting Algorithms (Size = {size})')
#     plt.legend()
#     plt.show()

# # 3
# class Car:
#     def __init__(self, model, year, max_speed, color):
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.color = color
#
#     def __repr__(self):
#         return f"{self.year} {self.color} {self.model} (Max Speed: {self.max_speed} km/h)"
#
#
# def quicksort_cars(cars, key):
#     if len(cars) <= 1:
#         return cars
#     else:
#         pivot = cars[0]
#     less = [car for car in cars[1:] if getattr(car, key) < getattr(pivot, key)]
#     greater = [car for car in cars[1:] if getattr(car, key) >= getattr(pivot, key)]
#     return quicksort_cars(less, key) + [pivot] + quicksort_cars(greater, key)
#
#
# def mergesort_car(cars, key):
#     if len(cars) > 1:
#         mid = len(cars) // 2
#         left_half = cars[:mid]
#         right_half = cars[mid:]
#
#         # Recursive call on each half
#         mergesort_car(left_half, key)
#         mergesort_car(right_half, key)
#
#         # Merge the sorted halves
#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if getattr(left_half[i], key) < getattr(right_half[j], key):
#                 cars[k] = left_half[i]
#                 i += 1
#             else:
#                 cars[k] = right_half[j]
#                 j += 1
#             k += 1
#
#         # Check for any remaining elements in left_half
#         while i < len(left_half):
#             cars[k] = left_half[i]
#             i += 1
#             k += 1
#
#         # Check for any remaining elements in right_half
#         while j < len(right_half):
#             cars[k] = right_half[j]
#             j += 1
#             k += 1
#
#
#
# cars_list = [
#     Car("Civic", 2022, 180, "Blue"),
#     Car("Accord", 2021, 200, "Red"),
#     Car("Camry", 2020, 190, "Silver"),
#     Car("Mustang", 2022, 250, "Yellow"),
# ]
# quick_sorted_cars = quicksort_cars(cars_list, 'year')
# print(f"Sorted by year:{quick_sorted_cars}")
# mergesort_car(cars_list, 'max_speed')
# print()
# print(f"Sorted by max speed: {cars_list}")

# 5
# Radix sort in Python


# Using counting sort to sort the elements in the basis of significant places
def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Method to do Radix Sort


def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10


# Bucket Sort
def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucketSort(x):
    arr = []
    slot_num = 10  # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x


# shell sort

def shellSort(arr, n):
    # code here
    gap = n // 2

    while gap > 0:
        j = gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j < n:
            i = j - gap  # This will keep help in maintain gap value

            while i >= 0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if arr[i + gap] > arr[i]:

                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]

                i = i - gap  # To check left side also
                # If the element present is greater than current element
            j += 1
        gap = gap // 2


data = [121, 432, 564, 23, 1, 45, 788]
# radixSort(data)
arr = [0.897, 0.565, 0.656,
       0.1234, 0.665, 0.3434]
print(bucketSort(arr))
print()
print(data)
print()
shellSort(data, len(arr))
print(data)


