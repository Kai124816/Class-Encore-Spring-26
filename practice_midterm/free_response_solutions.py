# ============================================================
# FREE RESPONSE (5 points)
# ============================================================
# ============================================================
# FREE RESPONSE (5 points)
# ============================================================
 
# 21) A Node class for a singly linked list is provided below.
#     Write a function sum_evens(head) that takes the head node of a linked
#     list of integers and returns the sum of all even values in the list.
#     If there are no even values, return 0.
#
#     Given the following program execution:
#
#     >>> n5 = Node(7)
#     >>> n4 = Node(3, n5)
#     >>> n3 = Node(4, n4)
#     >>> n2 = Node(2, n3)
#     >>> n1 = Node(5, n2)
#     >>> print(n1)
#     5 -> 2 -> 4 -> 3 -> 7 -> None
#     >>> sum_evens(n1)
#     6
#     >>> sum_evens(Node(1))
#     0
#     >>> sum_evens(None)
#     0
 
class Node:
    """A node in a singly linked list."""
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        result = ""
        curr = self
        while curr is not None:
            result += f"{curr.val} -> "
            curr = curr.next
        return result + "None"
 
 
def sum_evens(head) -> int:
    """
    Returns the sum of all even values in a linked list.
    Returns 0 if there are no even values or the list is empty.
 
    >>> sum_evens(None)
    0
    >>> sum_evens(Node(1))
    0
    >>> sum_evens(Node(2))
    2
    >>> n5 = Node(7)
    >>> n4 = Node(3, n5)
    >>> n3 = Node(4, n4)
    >>> n2 = Node(2, n3)
    >>> n1 = Node(5, n2)
    >>> sum_evens(n1)
    6
    >>> sum_evens(Node(2, Node(4, Node(6))))
    12
    """
    if head is None:
        return 0
    
    curr_node = head
    acc = 0
    while curr_node:
        if curr_node.val % 2 == 0:
            acc += curr_node.val
        curr_node = curr_node.next
    return acc
        

# ============================================================
# FREE RESPONSE (5 points)
# ============================================================
 
# 22) Implement a Stack class using OOP.
#
#     A Stack is a data structure that follows Last-In-First-Out (LIFO) order.
#     Your Stack class must support the following operations:
#
#       push(item)  — adds item to the top of the stack
#       pop()       — removes and returns the top item; raises IndexError if empty
#       peek()      — returns the top item without removing it; raises IndexError if empty
#       is_empty()  — returns True if the stack has no items, False otherwise
#       __len__()   — returns the number of items in the stack
#       __str__()   — returns a string representation (see doctests below)
#
#     Given the following program execution:
#
#     >>> s = Stack()
#     >>> s.is_empty()
#     True
#     >>> s.push(1)
#     >>> s.push(2)
#     >>> s.push(3)
#     >>> len(s)
#     3
#     >>> s.peek()
#     3
#     >>> s.pop()
#     3
#     >>> len(s)
#     2
#     >>> print(s)
#     Stack([1, 2])
#     >>> s.is_empty()
#     False
#     >>> s.pop()
#     2
#     >>> s.pop()
#     1
#     >>> s.is_empty()
#     True
#     >>> s.pop()
#     Traceback (most recent call last):
#         ...
#     IndexError: pop from empty stack
 
class Stack:
    """
    A Last-In-First-Out (LIFO) stack.
 
    >>> s = Stack()
    >>> s.is_empty()
    True
    >>> s.push(1)
    >>> s.push(2)
    >>> s.push(3)
    >>> len(s)
    3
    >>> s.peek()
    3
    >>> s.pop()
    3
    >>> len(s)
    2
    >>> print(s)
    Stack([1, 2])
    >>> s.is_empty()
    False
    >>> s.pop()
    2
    >>> s.pop()
    1
    >>> s.is_empty()
    True
    >>> s.pop()  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last): 
        ...
    IndexError: pop from empty stack
    """
    def __init__(self):
        self.data = []
 
    def push(self, item):
        self.data.append(item)
 
    def pop(self):
        if len(self.data) == 0:
            raise IndexError
        return self.data.pop()
 
    def peek(self):
        if len(self.data) == 0:
            raise IndexError
        return self.data[-1]
 
    def is_empty(self) -> bool:
        return len(self.data) == 0
 
    def __len__(self) -> int:
        return len(self.data)
 
    def __str__(self) -> str:
        return f"Stack({self.data})"
 
# ============================================================
# Run doctests when this file is executed directly
# ============================================================
if __name__ == "__main__":
    import doctest
    doctest.testmod()