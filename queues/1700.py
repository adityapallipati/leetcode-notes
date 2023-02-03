"""
QUEUES

FIRST IN, FIRST OUT
enqueue - adds from tail O(1)
dequeue - removes from head O(1)

()->()->()->()->NONE
head        tail
- most common implementation is using a linked list
- two most common operations are enqueue and dequeue

Enqueue adds elements to the tail

fn enqueue(val):
    newNode = ListNode(val)
    if queue is not empty:
        tail.next = newNode
        tail = tail.next
    else:
        # Queue is empty so head and tail both point to newNode
        head = newNode
        tail = newNode

Dequeue removes elements from the head

fn dequeue():
    if queue is empty:
        return -1
    # Otherwise remove from the head and update the head pointer
    else:
        val = head
        head = head.next
        if head is null:
            tail = null
        return val


Leetcode # 1700 Number of Students Unable to Eat Lunch

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
"""

from collections import deque
from collections import List

students = [1,1,0,0]
sandwhiches = [0,1,0,1]

def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        # two deques are implemented using the student and sandwhiches arrays
        """
        deques are DOUBLE ENDED QUEUES allows for quicker pop and push from both ends of the queue

        """
        students = deque(students)
        sandwiches = deque(sandwiches)

        # while non empty
        while True:

            # n is the length of students
            n = len(students)

            # current mismatch is 0
            mismatch = 0

            # do this for loop len(student) number of times
            for _ in range(n):

                # the curr var is the popleft() of the students deque
                # so if students is [1,1,0,0] then curr becomes 1
                cur = students.popleft()

                # if cur isn't sandwhiches[0] then do this which would mean you add 1 to mismatch
                if cur != sandwiches[0]:

                    # in this case students is [1,1,0,0] and sandwhiches is [0,0,1,1]
                    # cur is 1 and one does not equal sandwiches[0] which is 0
                    # so we add cur to the end of students making it [1,0,0,1] 
                    # then add 1 to mismatch BECAUSE they sandwhich and student vals are mismatched
                    students.append(cur)

                    mismatch += 1

                # otherwise popleft from sandwhiches so now we remove the first val from sandwhiches deque
                else:

                    sandwiches.popleft()
            # if we get n number of mismatches then we stop
            # so in this case if all 4 miss matched then we break and return students length
            if mismatch == n:
                break

        return len(students)

"""
if we continued with the for loop

we have students [1,0,0,1]
cur = 1
and sandwhiches [0,0,1,1]
mismatch = 2

then students [0,0,1,1]
cur = 0
and sandwhiches [0,0,1,1]
mismatch = 2

then students [0,1,1]
cur = 0
sandwiches = [0,1,1]
mismatch = 2

then students [1,1]
cur = 1
sandwiches = [1,1]
mismatch = 2

then students [1]
cur = 1
sandwiches = [1]
mismatch = 2

then students []
cur = None
sandwiches = []
mismatch = 2

return the length of students which is 0

so our answer is 0

"""