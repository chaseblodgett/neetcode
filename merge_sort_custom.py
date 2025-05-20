from typing import List

def merge(arr, left, mid, right, callback):
    left_len = mid - left + 1
    right_len = right - mid

    l = [0] * left_len
    r = [0] * right_len

    for i in range(left_len):
        l[i] = arr[left + i]
    
    for j in range(right_len):
        r[j] = arr[mid + 1 + j]
    
    i = 0
    j = 0
    k = left

    while i < left_len and j < right_len:
        if callback(l[i], r[j]):
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
        j += 1
        k += 1

def merge_sort(arr, left, right, callback):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid, callback)
        merge_sort(arr, mid + 1, right, callback)
        merge(arr, left, mid, right, callback)
    return arr


def callback_words(word_left, word_right):
    return len(word_left) >= len(word_right)

def callback_numbers(number_left, number_right):
    return abs(number_left) <= abs(number_right)

def sort_words(words: List[str]) -> List[str]:
    return merge_sort(words, 0, len(words) - 1, callback_words)

def sort_numbers(numbers: List[int]) -> List[int]:
    return merge_sort(numbers, 0, len(numbers) - 1, callback_numbers)



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
