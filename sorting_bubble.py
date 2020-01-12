"""
Bubble sort-> Read more about Bubble Sort on:
https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm
"""


def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


list = [5, 3, 8, 6, 7, 2]
sort(list)
print(list)
