"""
LINKED LISTS: SINGLY LINKED LISTS

- access, retrieve elem from list O(n)
- search, look for elem from list O(n)
- insert, add elem given ref O(1)
- del, remove elem given ref O(1)

1. Made up of objects called ListNodes
    - has value
    - has next

(VAL)->next(NULL)

class ListNode:
    constructor (value, next):
        1. Set value to the desired value, i.e. integer, char, etc.
        2. Set the next pointer to the desired node, null by default


- has a head and tail pointer

(VAL)->(VAL)->(VAL)
head          tail

Leetcode # 206: Reverse Linked List
- given head of linked list, reverse the list, and return the reversed list

example:

(1)->(2)->(3)->(4)

(4)->(3)->(2)->(1)
"""

class ListNode:
    # constructor which creates this: (0)->None
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: ListNode) -> ListNode:
    # whatever is before head is Null
    prev = None

    # current position is the head of the linked list
    curr = head

    # while the current position isn't Null
    while curr:

        # the temporary 'nxt' pointer is whatever is directly after the head node
        nxt = curr.next

        # whatever is currently after the head node is now the previous node
        curr.next = prev

        # the previous pointer is now the current position
        prev = curr

        # the current pointer is now whatever the original value of the node directly after head
        curr = nxt
    return prev


"""

[1]->[2]->[3]->[4]->[5]

prev = None so this --->  NONE->[1]->[2]

curr = head so this --> [1]

nxt = curr.next so this --> [2]

prev is now this -> [1]

curr is now this -> [2]

so this [1]->[2] became this [2]->[1]

this continues until we hit None which would be directly after [5]->NONE

this ends the loop because the condition is while curr isn't set to None

"""