"""
STATIC ARRAYS
Leetcode # 27: Remove Element

1. given an array of integers 'nums' and integer 'val'
2. remove all occurances of 'val' within 'nums' IN-PLACE
3. you CAN change relative order
4. first 'k' elements of 'nums' should hold final res
5. return first 'k' elements

"""


"""
nums = [3,2,2,3]

val = 3

k = 0

for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1
return nums

EXPLANATION:

what's happening here is we have two pointers in the 'nums' array to keep track of the 'val' integer

this is i
\/
[3,2,2,3]
^
this is k

if nums[i] != val:

- if nums[0] which is 3 is not equal to 'val' which is 3
- then we execute the rest of the if statment but 3 IS equal to 3 so we go through the loop again

  this is i
   \/
[3,2,2,3]
^
this is k

if nums[i] != val:

- if nums[1] which is 2 is not equal to 'val' which is 3
- then we execute the rest of the if statment
- nums[k] = nums[i]
- so nums[0] which is 3 is equal to nums[i] which is 2
- now our array looks like this: [2,2,3]
- k is incremented by 1 so now its nums[1] while nums[i] is nums[2] 
- nums[2] is equal to 3 but since our problem only requires us to return the first 'k' elements it doesn't matter

SO:

we return this [2,2,_,_] techincally it's [2,2,3,3] since we are doing this inplace

end result is [2,2] meaning we've successfuly removed all of the 'val' integers

"""