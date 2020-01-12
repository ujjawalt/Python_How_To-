"""
Linear Search-> The list(or any sequence) needs to be sorted in order to apply Binary Search.
"""

pos = -1


def search(nums, n):

    lower_bound = 0
    # If length is 5 then index only go up to 0-4
    upper_bound = len(nums) - 1

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound)//2

        if nums[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if nums[mid] < n:
                lower_bound = mid + 1
            else:
                upper_bound = mid - 1
    return False


nums = [5, 10, 15, 20, 25, 30, 35, 40]
n = 30

if search(nums, n):
    print("Found at ", pos+1)
else:
    print("Not Found")
