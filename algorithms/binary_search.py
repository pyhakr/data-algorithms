import random

nums = sorted([random.randint(0, 25) for n in range(25)])

def binary_search(n, seq):
    left = 0
    right = len(seq) - 1

    while left <= right:

        mid = (left + right) // 2

        if seq[mid] == n:
            print('{} : found'.format(n))
            return True
        elif n < seq[mid]:
            right = mid - 1
        else:
            left = mid + 1

    print('{} : not found'.format(n))
    return False


def binary_search_recursive(n, seq, left, right):
    if left > right:
        print('{} : not found'.format(n))
        return False

    mid = (left + right) // 2

    if seq[mid] == n:
        print('{} : found'.format(n))
        return True
    elif n < seq[mid]:
        return binary_search_recursive(n, seq, left, mid - 1)
    else:
        return binary_search_recursive(n, seq, mid + 1, right)


for i in range(25):
    binary_search_recursive(i, nums, 0, len(nums) - 1)
    binary_search(i, nums)

