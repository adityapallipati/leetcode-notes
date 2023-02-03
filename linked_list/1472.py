"""
Leetcode # 1472: Design Browser History

- you have homepage
- you can visit another url
- get back in the browser history in the number of steps
- get forward in the browser history in the number of steps

objective:

build browser history class

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.

void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history.

If you can only return x steps in the history and steps > x,
you will return only x steps. Return the current url after moving back in history at most steps.

string forward(int steps) Move steps forward in history.
If you can only forward x steps in the history and steps > x, you will forward only x steps.

Return the current url after forwarding in history at most steps.
"""

"""
This is built with a doubly linked list.
"""

# this node class creates a linked list obj that looks like this: NONE<-(VAL)->NONE
class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = Node(homepage)
        self.cur = self.history

    def visit(self, url: str) -> None:
        node = Node(url)
        self.cur.next = node
        node.prev = self.cur
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.prev != None:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next != None:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val