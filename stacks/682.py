"""
STACKS
- Last In, First Out

example:

stacks are conceptually like this

[0] <- last
[1] <- third
[2] <- second
[3] <- first

this is equivalent to stack = [3,2,1,0]

remove elem from stack:

[1] <- last
[2] <- second
[3] <- first

this is equivalent to stack = [3,2,1,0]

stack.pop()

stack = [3,2,1]

push = adding to top
pop = removing top elem
peek = looking at top elem

________________________________________
Leetcode # 682 Baseball Game

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.



"""
operations = ["5","2","C","D","+"]

def calPoint(operations):

    # create empty stack using array
    stack = []

    # for each value in the operations stack
    for op in operations:

        # if the val is '+' go to the last pos in the stack and the second to last pos and add
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
        # if 'D' add the result of doubling the last val in the stack
            stack.append(stack[-1] * 2)
        elif op == 'C':
        # if 'C' remove the last elem from the stack
            stack.pop()
        else:
        # otherwise it's a number so just convert it to an integer and add it to the stack at the end
            stack.append(int(op))
    # print out the sum of integers in the stack
    print(sum(stack))

calPoint(operations)

"""
let's walk through the stack with the operations being operations = ["5","2","C","D","+"]

first one is "5"

so our stack looks like this conceptually:

[5]

and is implemented like this: stack = [5]

next is "2"

so now our stack is like this:

og  curr
    [2]
[5] [5]

stack = [5,2]

next is "C"

so we remove 2 with stack.pop() which removes the last elem form an array

og      curr
    [X]
[5] [5] [5]

stack = [5]

next is "D" so we double 5 and add that res to our stack

5 * 2 is 10

og          curr
    [X]     [10]
[5] [5] [5] [5]

stack = [5,10]

next is "+" so we add the last val in the stack plus the second to last

5 + 10 is 15

og                curr
                  [15]
    [X]     [10]  [10]
[5] [5] [5] [5]   [5]


at this point we reached the end of the loop so we have the sum statement to execute

we get the sum of [5,10,15]

5 + 10 + 15 is 30

our final result is the integer 30

"""


