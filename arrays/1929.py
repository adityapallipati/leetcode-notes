"""
DYNAMIC ARRAYS

- access, get an elem from array O(1)
- insert, add elem into array if in start or end O(1)
    - insert in middle, requires shifting arr O(n)
- remove, remove elem in array if in start or end O(1)
    - remove in middle, requires shfiting arr O(n)

Leetcode # 1929 Concatenation of an Array

1. given int of 'nums' of length 'n' concat a new array 'ans' that is 2n
2. ans[i] == nums[i] AND ans[n + 1] == nums[i]
3. return ans

example:
nums = [1,2,3]
ans = [1,2,3,1,2,3]

"""

nums = [1,2,3]

def concatArray(nums):
    # for i in range(len(nums)):
    #     ans = []
    #     ans = nums + nums
    
    ans = nums*2
    print(ans)

concatArray(nums)
