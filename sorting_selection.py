"""
Selection Sort-> Read more about Selection Sort on:
https://www.tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm
"""


def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i, 6):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp


list = [5, 3, 8, 6, 7, 2]
sort(list)
print(list)
