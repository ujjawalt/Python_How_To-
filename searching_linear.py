"""
Binary Search-> Simples searching technique. Search entire list one by one.
"""

pos = -1


def search(nums, n):

    for i in range(len(nums)):
        if nums[i] == n:
            globals()['pos'] = i
            return True
    return False


nums = [10, 20, 30, 2, 5, 9, 18, 15]
n = 15
if search(nums, n):
    print("Found at ", pos+1)
else:
    print("Not Found")
