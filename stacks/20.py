"""
STACKS

Leetcode # 26 Valid Parenthesis

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

example:

s = '()'
res = True

s = '[)'
res = False
"""

s = "{[()([])]}"

def isValid(s):

    # empty stack created from array
    stack = []

    # dictionary of valid parenthesis
    parenthesis = {
        ']':'[',
        '}':'{',
        ')':'('
    }

    # check every val in the 's' string
    for i in s:
        # if s[i] in parenthsis
        if i in parenthesis:
            # if the stack isn't empty and the last val of the stack is equal to to the i-th key of parenthesis 
            if stack and stack[-1] == parenthesis[i]:
                # pop from the stack
                stack.pop()
            else:
                return False
        else:
            # else add to the stack whatever 'i' is in parenthesis
            stack.append(i)

    # return True is stack isn't empty otherwise return false
    return True if not stack else False


isValid(s)

"""

s = "{[()([])]}"

parenthesis = {
        ']':'[',
        '}':'{',
        ')':'('
    }

stack = []

'{' is in parenthsis

stack = '{'

['{']

next is '['

[')']
['(']
['[']
['{']
and so on until the each open has a matching close

other false is returned

"""