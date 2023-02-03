"""
DOUBLY LINKED LISTS

- access, retrieve elem in list O(n)
- search, look for elem in list O(n)
- insert, insert elem at place u have a ref O(1)
- del, del elem at place u have a ref O(1)



This is like a singly linked list but with addition of a prev pointer.

<-(VAL)-> <-(VAL)->

implemented like this:

class ListNode:
    def __init__(self, val=0, prevNode=None, nextNode=None):
        self.val = val
        self.prev = prevNode
        self.next = nextNode


so if i do this:

ListNode(1)

I've made one list node with the value 1 like so:

NONE<-(1)->NONE

and if i want to add to this list:

a = ListNode(1)
b = ListNode(2)

a.next = b
b.prev = a

the above will look like this:

NONE<-(1)-><-(2)->NONE

Leetcode # 707: Design Linked List

Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.

int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

"""

# makes list nodes
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    # this creates a linked list with a head and a tail
    """
    conceptually looks like this:
          head        tail
    NONE<---()---><---()--->NONE

    """
    def __init__(self):
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    """
        get returns a specific val in the linked list when given the index

        if you have an linked list thats: NONE<--(0)--><--(1)--><--(2)-->NONE

        and you say get(1)

        the return value is the int 1

        binary search is used to speed up the process of looking for this val

        if 1 is <= (3 // 2) or 1 which is the size of the linked list then

        the curr variable is set to self.head so it's set to (0) then

        we iterate through the the array for whatever the input index is + 1 so in this case twice

        curr is set to curr.next which in this case is 1 the value we're looking for and at the index we're looking for

        so we return the curr.val which is 1

        if we had a list of 1 to 100 numbers and we did this it would be very quick as we eliminate the need to search
        for half of the numbers but starting at the middle

    """
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1

        if index <= self.size // 2:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(index - 1):
                curr = curr.prev
        return curr.val

    """
        adding at the head is adding at the beggining of the linked list
        if we had a list (0)-(1)-(2)-(3)-(4)

        we'll just call the add at index function which adds at the index 0 or the beggining the speciifc value we want

        so in this case if we did addAtHead(0) we would add a 0 to the list like so:

        (0)-(0)-(1)-(2)-(3)-(4)

    """
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    """
        this does the same thing as atAtHead except the index is at the end of the list

        (0)-(1)-(2)-(3)-(4) this size of this is 5

        so addAtIndex(5, 5) would be called if we did addAtTail(5) making this list look like this:

        (0)-(1)-(2)-(3)-(4)-(5)

        because we would be adding at index 5 which would be directly after the value 4 since we count from 0
        when looking at the index

    """
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return -1

        if index <= self.size // 2:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        newNode = ListNode(val)
        newNode.prev = pred
        newNode.next = succ
        pred.next = newNode
        succ.prev = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index <= self.size // 2:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        pred.next = succ
        succ.prev = pred
        self.size -= 1

















