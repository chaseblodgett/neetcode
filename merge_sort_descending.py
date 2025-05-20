from typing import List

def merge(arr, left, mid, right):
    left_len = mid - left + 1
    right_len = right - mid

    l = [0] * left_len
    r = [0] * right_len

    for i in range(left_len):
        l[i] = arr[left + i]

    for j in range(right_len):
        r[j] = arr[mid + j + 1]

    i = 0
    j = 0
    k = left

    while i < left_len and j < right_len:
        if l[i] >= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    
    while i < left_len:
        arr[k] = l[i]
        i += 1
        k +=1 
    
    while j < right_len:
        arr[k] = r[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
    return arr

def sort_words(words: List[str]) -> List[str]:
    return merge_sort(words, 0, len(words) -1)

def sort_numbers(numbers: List[int]) -> List[int]:
    return merge_sort(numbers, 0, len(numbers) -1)

def sort_decimals(numbers: List[float]) -> List[float]:
    return merge_sort(numbers, 0, len(numbers) -1)



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))