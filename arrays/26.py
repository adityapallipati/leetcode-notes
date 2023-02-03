"""
STATIC ARRAYS

- access, get elem from arr O(1)
- insert, add elem in arr O(n)
    - if insert at end O(1)
- remove, del elem in arr O(n)
    - if remove at end O(1)


Leetcode #26: Remove Duplicates from Sorted Array
1. array is sorted in increasing order
2. remove the duplicates in place
3. relative order should be kept the same
4. res in first part of the array
5. return 'k' meaning the number of remaining values after removal
6. must be an O(1) memory solution

"""
nums = [0,0,1,1,1,2,2,3,3,4]


def removeDuplicates(nums):

    '''
    [0,1,2]
       ^
       |
    the left pointer
    '''
    left = 1

    for right in range(len(nums) - 1):
        '''
            [0,1,2]
            ^
            |
            the right pointer

        - if the 0 index and the first index is not the same then it's not a duplicate
        - so left which is position 1 is not equal to the value of right + 1 which is also 1
        - this means if it's like this [0,1] then 1 stays the same, doesn't need to change
        - then left becomes 2 because it was 1 and 1 + 1 is 2
        - repeat and then we're at 1 for right pointer and at 2 for the left pointer
        - if it's like this [0,1,1,1] then the if statement doesn execute and we continue until we can execute it
        '''
        if nums[right] != nums[right + 1]:
            nums[left] = nums[right + 1]
            left = left + 1
    print(left, nums)


removeDuplicates(nums)

