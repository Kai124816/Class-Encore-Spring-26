"""
CS 211 - Practice Midterm Exam
Object-Oriented Programming

INSTRUCTIONS (Multiple Choice):
  For each multiple choice question, assign your answer to the provided variable.
  Example: Q0 = "A"
================================================================================
"""

# ============================================================
# MULTIPLE CHOICE — Assign your answer as a string: "A", "B", "C", or "D"
# ============================================================

# 1) Which of the following correctly describes method overriding in Python?
#
#    A) A subclass defines a method with a different name than the parent class method.
#    B) A subclass defines a method with the same name as a parent class method,
#       replacing its behavior.
#    C) A parent class calls a method defined in its subclass.
#    D) Two sibling subclasses share the same method implementation.

Q1 = ""


# 2) What is the output of the following code?
#
class Shape:
    def area(self):
        return 0
    def describe(self):
        print(f"Area: {self.area()}")

class Circle(Shape):
    def area(self):
        return 42

c = Circle()
c.describe()
#
#    A) Area: 0
#    B) Area: 42
#    C) AttributeError
#    D) None

Q2 = ""


# 3) What keyword is used to call a method from a parent class inside a subclass?
#
#    A) parent()
#    B) super()
#    C) base()
#    D) inherit()

Q3 = ""


# 4) Which statement about abstract classes in Python is TRUE?
#
#    A) An abstract class can be instantiated directly.
#    B) Abstract classes cannot have any concrete (non-abstract) methods.
#    C) A class with at least one abstract method cannot be instantiated.
#    D) Python does not support abstract classes.

Q4 = ""


# 5) What is the output of the following code?
#
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
c = Counter()
print(Counter.count)
#
#    A) 0
#    B) 1
#    C) 3
#    D) Error

Q5 = ""


# 6) Which import statement correctly imports only the class Dog from a file named animals.py?
#
#    A) import Dog from animals
#    B) from animals import Dog
#    C) import animals.Dog
#    D) from Dog import animals

Q6 = ""


# 7) What is the output of the following code?
#
class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    def describe(self):
        return f"Speed: {self.speed}"

class Car(Vehicle):
    def __init__(self, speed, brand):
        super().__init__(speed)
        self.brand = brand
    def describe(self):
        return f"{self.brand}, {super().describe()}"

c = Car(100, "Toyota")
print(c.describe())
#
#    A) Speed: 100
#    B) Toyota, Speed: 100
#    C) Toyota, 100
#    D) Error: super() not allowed here

Q7 = ""


# 8) What is printed by the following exception-handling code?
#
try:
    lst = [1, 2, 3]
    print(lst[5])
except ValueError:
    print("value error")
except IndexError:
    print("index error")
finally:
    print("done")
#
#    A) value error
#       done
#    B) index error
#       done
#    C) index error
#    D) done

Q8 = ""


# 9) What does __str__ allow you to do in a class?
#
#    A) Compare two objects using ==
#    B) Control what is printed when print() is called on an object
#    C) Define how an object is stored in memory
#    D) Prevent the object from being modified

Q9 = ""


# 10) Which of the following statements about class variables is FALSE?
#
#     A) Class variables are shared across all instances of a class.
#     B) A class variable can be accessed using the class name.
#     C) Assigning to a class variable via an instance creates a new instance variable.
#     D) Class variables are always private and cannot be accessed outside the class.

Q10 = ""


# 11) What is the term for an object's ability to take on different forms depending on
#     the context in which it is used?
#
#     A) Encapsulation
#     B) Abstraction
#     C) Polymorphism
#     D) Inheritance

Q11 = ""


# 12) What is the output of the following code?
#
def apply(func, value):
    return func(value)

def double(x):
    return x * 2

result = apply(double, 5)
print(result)
#
#     A) 5
#     B) 10
#     C) double
#     D) Error

Q12 = ""


# 13) Which of the following is a correct definition of an abstract method using
#     Python's abc module?
#
#     A) def my_method(self): pass
#     B) @abstract
#        def my_method(self): ...
#     C) @abstractmethod
#        def my_method(self): ...
#     D) abstract def my_method(self): ...

Q13 = ""


# 14) What is the output of the following code?
#
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

n3 = Node(3)
n2 = Node(2, n3)
n1 = Node(1, n2)

curr = n1
total = 0
while curr is not None:
    total += curr.val
    curr = curr.next
print(total)
#
#     A) 1
#     B) 3
#     C) 6
#     D) Error

Q14 = ""


# 15) What does the following code print?
#
x = {"a": 1, "b": 2, "c": 3}
x["b"] += 10
del x["a"]
print(len(x))
#
#     A) 3
#     B) 2
#     C) 1
#     D) Error

Q15 = ""


# 16) When would you use an abstract base class rather than a regular base class?
#
#     A) When you want to allow the base class to be instantiated directly.
#     B) When you want to guarantee that all subclasses implement certain methods.
#     C) When you want to prevent any class from inheriting from it.
#     D) When the base class has no methods at all.

Q16 = ""


# 17) What is the output of the following code?
#
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
for num, letter in pairs:
    print(num, letter)
#
#     A) 1 a
#        2 b
#        3 c
#     B) (1, 'a')
#        (2, 'b')
#        (3, 'c')
#     C) 1
#        2
#        3
#     D) Error: cannot unpack

Q17 = ""


# 18) In Python, which built-in function returns True if an object is an instance of a
#     given class or any of its subclasses?
#
#     A) type()
#     B) isinstance()
#     C) issubclass()
#     D) hasattr()

Q18 = ""


# 19) What is the Big-O time complexity of looking up a key in a Python dictionary
#     (average case)?
#
#     A) O(n)
#     B) O(log n)
#     C) O(1)
#     D) O(n log n)

Q19 = ""


# 20) What is printed by the following code?
#
class Foo:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x

a = Foo(5)
b = Foo(5)
c = a
print(a == b, a is b, a is c)
#
#     A) False False True
#     B) True False True
#     C) True True True
#     D) False True True

Q20 = ""

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
    # YOUR CODE HERE
    pass

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
    >>> s.pop()
    Traceback (most recent call last):
        ...
    IndexError: pop from empty stack
    """
    def __init__(self):
        # YOUR CODE HERE
        pass
 
    def push(self, item):
        # YOUR CODE HERE
        pass
 
    def pop(self):
        # YOUR CODE HERE
        pass
 
    def peek(self):
        # YOUR CODE HERE
        pass
 
    def is_empty(self) -> bool:
        # YOUR CODE HERE
        pass
 
    def __len__(self) -> int:
        # YOUR CODE HERE
        pass
 
    def __str__(self) -> str:
        # YOUR CODE HERE
        pass
 
# ============================================================
# Run doctests when this file is executed directly
# ============================================================
if __name__ == "__main__":
    import doctest
    doctest.testmod()