from typing import List

def merge(arr, left, mid, right):
    left_len = mid - left + 1
    right_len = right - mid

    l = [0] * left_len
    r = [0] * right_len 

    for i in range(left_len):
        l[i] = arr[left + i]
    
    for i in range(right_len):
        r[i] = arr[mid + 1 + i]
    
    i = 0
    j = 0
    k = left

    while i < left_len and j < right_len:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    
    while i < left_len:
        arr[k] = l[i]
        k += 1
        i += 1
    
    while j < right_len:
        arr[k] = r[j]
        k += 1
        j += 1

def merge_sort(left, right, arr):
    if left < right:
        mid = (right + left) // 2
        merge_sort(left, mid, arr)
        merge_sort(mid+ 1, right, arr)
        merge(arr, left, mid, right)
    return arr


def sort_words(words: List[str]) -> List[str]:
    return merge_sort(0, len(words) -1, words)

def sort_numbers(numbers: List[int]) -> List[int]:
    return merge_sort(0, len(numbers) -1, numbers)

def sort_decimals(numbers: List[float]) -> List[float]:
    return merge_sort(0, len(numbers) -1, numbers)


print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
