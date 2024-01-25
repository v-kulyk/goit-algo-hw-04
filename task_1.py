import timeit
import random


def merge_sort(arr):
    lst = arr[:]
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(arr):
    lst = arr[:]
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


# Використовуємо вбудований алгоритм сортування Timsort
def tim_sort(arr):
    lst = arr[:]
    lst.sort()


for i in range(4):
    # Генеруємо тестові дані для масиву довжиною 10^4
    data = [random.randint(0, 10000) for _ in range(10 ** (i + 1))]

    # Замір часу виконання для алгоритму злиття
    merge_sort_time = timeit.timeit("merge_sort(data[:])", globals=globals(), number=10)

    # Замір часу виконання для алгоритму вставками
    insertion_sort_time = timeit.timeit("insertion_sort(data[:])", globals=globals(), number=10)

    # Замір часу виконання для Timsort
    tim_sort_time = timeit.timeit("tim_sort(data[:])", globals=globals(), number=10)

    print(f"Test {i + 1}: Dataset of {len(data)} elements")
    print(f"[{i + 1}] Merge Sort Time: {merge_sort_time}")
    print(f"[{i + 1}] Insertion Sort Time: {insertion_sort_time}")
    print(f"[{i + 1}] Timsort Time: {tim_sort_time}")
    print("-------------------")
