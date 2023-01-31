"""
Leetcode #21 Merge Two Sorted Lists

- you have the heads of two sorted linked lists
- merge them into one sorted linked list
- return the head of the new merged list

example:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


"""

class ListNode():
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        # dummy node of a temporary ListNode
        dummy = ListNode()

        # tail is set to the dummy node so it's at the end eg: (0)->None this is that node
        tail = dummy

        # while the two lists aren't empty
        while list1 and list2:

            # if the val in list1 is less than the val in list2 then whatever is after the current tail is list1
            if list1.val < list2.val:
                tail.next = list1

                # then list1 is set to next
                list1 = list1.next
            else:
                # if list2 val is < list1 val then tail.next is list2
                tail.next = list2

                # list2 is set to next
                list2 = list2.next
            # tail is now whichever list what set to the tail position based on the conditional
            tail = tail.next
        if list1:
            #if list1 is non empty the next pos is list1
            tail.next = list1
        elif list2:
            # else if list2 is not empty the next pos is list2
            tail.next = list2

        # once the list is sorted, return the head of the list which is the next pos of the dummy node
        return dummy.next