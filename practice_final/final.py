"""
CS 211 - Practice Final Exam
OOP, Recursion, Trees, Binary Numbers, and Data Structures

INSTRUCTIONS (Multiple Choice):
  For each multiple choice question, assign your answer to the provided variable.
  Example: Q0 = "A"
================================================================================
"""

# ============================================================
# MULTIPLE CHOICE — Assign your answer as a string: "A", "B", "C", or "D"
# ============================================================

# 1) What is printed by the following code?
#
class Animal:
    def sound(self):
        return "..."

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

def make_noise(animal):
    print(animal.sound())

make_noise(Dog())
make_noise(Cat())
make_noise(Animal())
#
#    A) Woof / Meow / ...
#    B) ... / ... / ...
#    C) Woof / Meow / Woof
#    D) TypeError: cannot call sound() on Animal

Q1 = ""


# 2) What is printed by the following code?
#
class Furniture:
    def __init__(self, material):
        self.material = material

class Chair(Furniture):
    def __init__(self, material, legs):
        super().__init__(material)
        self.legs = legs

c = Chair("oak", 4)
print(c.material, c.legs)
#
#    A) AttributeError: Chair has no attribute 'material'
#    B) oak 4
#    C) None 4
#    D) oak None

Q2 = ""


# 3) What is printed by the following code?
#
class Robot:
    count = 0
    def __init__(self, name):
        self.name = name
        Robot.count += 1

r1 = Robot("R2D2")
r2 = Robot("C3PO")
r3 = Robot("BB8")
print(Robot.count, r2.count)
#
#    A) 3 1
#    B) 1 3
#    C) 3 3
#    D) 3 0

Q3 = ""


# 4) What is printed by the following code?
#
class Base:
    def hello(self):
        return "A"

class Mid(Base):
    def hello(self):
        return "B" + super().hello()

class Top(Mid):
    def hello(self):
        return "C" + super().hello()

print(Top().hello())
#
#    A) CBA
#    B) C
#    C) CB
#    D) ABC

Q4 = ""


# 5) What is printed by the following code?
#
class Shape:
    pass

class Polygon(Shape):
    pass

class Triangle(Polygon):
    pass

t = Triangle()
print(isinstance(t, Shape), isinstance(t, Polygon), type(t) == Shape)
#
#    A) True True True
#    B) True True False
#    C) False False True
#    D) True False False

Q5 = ""


# 6) What is printed by the following code?
#
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
#
#    A) (1, 2)
#    B) (3, 4)
#    C) (4, 6)
#    D) TypeError: unsupported operand type

Q6 = ""


# 7) What happens when the highlighted line is executed?
#
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self): ...

class Square(Drawable):
    def draw(self):
        return "square"

d = Drawable()   # <--- this line (what does this do if run on its own?)
#
#    A) Creates a Drawable instance with no draw() method
#    B) Raises NotImplementedError
#    C) Raises TypeError: Can't instantiate abstract class Drawable
#    D) Creates a Drawable with draw() returning None

Q7 = ""


# 8) What is printed by the following code?
#
class Item:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Item({self.name})"
    def __repr__(self):
        return f"<Item name={self.name!r}>"

item = Item("sword")
print(item)
print([item])
#
#    A) Item(sword) and [<Item name='sword'>]
#    B) Item(sword) and [Item(sword)]
#    C) <Item name='sword'> and [<Item name='sword'>]
#    D) <Item name='sword'> and [Item(sword)]

Q8 = ""


# 9) What is printed by the following code?
#
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

print(recursive_sum(5))
#
#    A) 5
#    B) 10
#    C) 25
#    D) 15

Q9 = ""


# 10) What is printed by the following code?
#
class Lit:
    def __init__(self, val):
        self.val = val
    def eval(self):
        return self.val

class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        return self.left.eval() + self.right.eval()

class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        return self.left.eval() * self.right.eval()

# Represents: (3 + 4) * (2 + 1)
expr = Mul(Add(Lit(3), Lit(4)), Add(Lit(2), Lit(1))) # Mul(Add(3, 4), Add(2, 1)) -> Mul(7, 3) -> 21
print(expr.eval())
#
#     A) 10
#     B) 21
#     C) 14
#     D) 9

Q10 = ""


# 11) What is printed by the following code?
#
class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def mystery_ll(node):
    if node is None:
        return []
    return mystery_ll(node.next) + [node.val]

head = LLNode(1, LLNode(2, LLNode(3)))
print(mystery_ll(head))
#
#     A) [1, 2, 3]
#     B) [3, 2, 1]
#     C) [1]
#     D) []

Q11 = ""


# 12) What is printed by the following code?
#
class BTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes(tree):
    if tree is None:
        return 0
    return 1 + count_nodes(tree.left) + count_nodes(tree.right)

#      1
#     / \
#    2   3
#   / \
#  4   5
bt = BTree(1, BTree(2, BTree(4), BTree(5)), BTree(3))
print(count_nodes(bt))
#
#     A) 3
#     B) 4
#     C) 5
#     D) 6

Q12 = ""


# 13) What is printed by the following code?
#
class BSTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

# bst_q13 tree structure
#        8
#       / \
#      3   10
#     / \    \
#    1   6    14 

bst_q13 = BSTNode(8,
                  BSTNode(3, BSTNode(1), BSTNode(6)),
                  BSTNode(10, None, BSTNode(14)))
print(inorder(bst_q13))
#
#     A) [1, 3, 6, 8, 10, 14]
#     B) [8, 3, 10, 1, 6, 14]
#     C) [1, 6, 3, 14, 10, 8]
#     D) [14, 10, 6, 3, 1, 8]

Q13 = ""


# 14) Which of the following correctly finds the maximum value in a
#     NON-EMPTY linked list of integers using recursion? If the list is
#     empty find_max() should return -inf
#
# A) 
def find_max(node):
    if node is None:
        return None
    return max(node.val, find_max(node.next))
#
# B) 
def find_max(node):
    if node.next is None:
        return node.val
    return max(node.val, find_max(node.next))
#
# C) 
def find_max(node):
    if node is None:
        return 0
    return max(node.val, find_max(node.next))
#
# D) 
def find_max(node):
    if node is None:
        return float('-inf')
    return max(node.val, find_max(node.next))

Q14 = ""


# 15) What is printed by the following code?
#
class FileSys:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class DirSys:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

def count_files(node):
    if isinstance(node, FileSys):
        return 1
    return sum(count_files(c) for c in node.children)

root_q15 = DirSys("home", [
    FileSys("notes.txt", 5),
    DirSys("photos", [
        FileSys("a.jpg", 100),
        FileSys("b.jpg", 200)
    ]),
    DirSys("docs", [])
])
print(count_files(root_q15))
#
#     A) 1
#     B) 2
#     C) 3
#     D) 5

Q15 = ""


# 16) What is the decimal value of the unsigned 4-bit binary number 1101?
#
#     A) 11
#     B) 12
#     C) 13
#     D) 14

Q16 = ""


# 17) In 4-bit two's complement representation, what decimal value
#     does 1110 represent?
#
#     A) 14
#     B) -1
#     C) -6
#     D) -2

Q17 = ""


# 18) What is the result of adding binary 0111 and 0001?
#     (4-bit unsigned; ignore overflow.)
#
#     A) 0111
#     B) 1001
#     C) 0110
#     D) 1000

Q18 = ""


# 19) A BinaryNumber object stores the value 5 (decimal) as bits
#     [0, 1, 0, 1] (MSB first). After a LEFT shift by 2 positions,
#     what is the new decimal value?
#
#     A) 20
#     B) 10
#     C) 1
#     D) 2

Q19 = ""


# 20) What is the result of bitwise OR between binary 1010 and 0110?
#
#     A) 0010
#     B) 1110
#     C) 1000
#     D) 1010

Q20 = ""


# 21) What is the result of bitwise XOR between binary 1011 and 0110?
#
#     A) 1101
#     B) 0010
#     C) 1111
#     D) 0001

Q21 = ""


# 22) What is printed by the following code?
#
class SimpleQueue:
    def __init__(self):
        self._items = []
    def enqueue(self, item):
        self._items.append(item)
    def dequeue(self):
        if not self._items:
            raise IndexError("empty queue")
        return self._items.pop(0)

sq = SimpleQueue()
sq.enqueue("A")
sq.enqueue("B")
sq.enqueue("C")
print(sq.dequeue())
print(sq.dequeue())
#
#     A) A / B
#     B) C / B
#     C) A / C
#     D) B / C

Q22 = ""


# 23) What is printed by the following code?
#
def list_depth(lst):
    if not isinstance(lst, list):
        return 0
    if not lst:
        return 1
    return 1 + max(list_depth(item) for item in lst)

print(list_depth([1, [2, [3]], 4]))
#
#     A) 1
#     B) 2
#     C) 4
#     D) 3

Q23 = ""


# 24) What is printed by the following code?
#
def count_ints(d):
    total = 0
    for val in d.values():
        if isinstance(val, dict):
            total += count_ints(val)
        elif isinstance(val, int):
            total += 1
    return total

nested_data = {"a": 1, "b": {"c": 2, "d": {"e": 3}}, "f": "hello"}
print(count_ints(nested_data))
#
#     A) 1
#     B) 2
#     C) 4
#     D) 3

Q24 = ""


# 25) What is the average-case time complexity of searching for a value
#     in a BALANCED Binary Search Tree with n nodes?
#
#     A) O(1)
#     B) O(log n)
#     C) O(n)
#     D) O(n log n)

Q25 = ""


# 26) What is the PREORDER traversal of the following binary tree?
#
#         10
#        /  \
#       5    15
#      / \
#     3   7
#
#     A) [3, 5, 7, 10, 15]
#     B) [3, 7, 5, 15, 10]
#     C) [10, 15, 5, 7, 3]
#     D) [10, 5, 3, 7, 15]

Q26 = ""


# 27) Which of the following correctly describes the property that makes
#     a binary tree a valid Binary Search Tree (BST)? (Assume the tree has 
#     no duplicate values).
#
#     A) For every node, ALL values in its left subtree are smaller than
#        the node's value, and ALL values in its right subtree are larger.
#     B) Every node's left child has a smaller value than its right child.
#     C) The tree must be balanced: all leaf nodes are at the same depth.
#     D) Values are inserted in sorted order, from smallest to largest.

Q27 = ""


# 28) If a BinaryNumber stores the value 12,
#     what decimal value results from right-shifting by 1?
#
#     A) 24
#     B) 6
#     C) 3
#     D) 4

Q28 = ""


# 29) In a SignedBinaryNumber stored MSB-first, bits[0] is the sign bit.
#     Which condition correctly identifies that a number is NEGATIVE?
#
#     A) bits[0] == 0
#     B) bits[-1] == 1
#     C) bits[0] == 1
#     D) sum(bits) > len(bits) // 2

Q29 = ""


# 30) What is the WORST-CASE time complexity for inserting a value into
#     an unbalanced Binary Search Tree with n existing nodes?
#
#     A) O(1)
#     B) O(log n)
#     C) O(n)
#     D) O(n^2)

Q30 = ""


# ============================================================
# FREE RESPONSE — Problem 31 (10 points)
# ============================================================
#
# Implement a LibraryBook class and a DigitalBook subclass.
#
# LibraryBook:
#   - __init__(self, title: str, author: str, year: int)
#       Store all three as instance attributes.
#       Increment the class variable books_created by 1.
#   - Class variable books_created: int  (starts at 0)
#   - age(self, current_year: int) -> int
#       Return current_year - year.
#   - __lt__(self, other: "LibraryBook") -> bool
#       Return True if self was published BEFORE other (compare year).
#   - __str__(self) -> str
#       Return the string  "LibraryBook(title, year)"
#
# DigitalBook(LibraryBook):
#   - __init__(self, title, author, year, file_size_mb: float)
#       Call super().__init__ for the inherited fields, then store file_size_mb.
#       (books_created is still incremented via the parent __init__.)
#   - can_download(self, max_mb: float) -> bool
#       Return True if file_size_mb <= max_mb.
#   - __str__(self) -> str
#       Return "DigitalBook(title, year, Xmb)"  where X is file_size_mb.
#
# Example execution:
#
#   >>> b1 = LibraryBook("Dune", "Herbert", 1965)
#   >>> b2 = LibraryBook("Foundation", "Asimov", 1951)
#   >>> LibraryBook.books_created
#   2
#   >>> b1.age(2025)
#   60
#   >>> b2 < b1
#   True
#   >>> str(b1)
#   'LibraryBook(Dune, 1965)'
#   >>> db = DigitalBook("Neuromancer", "Gibson", 1984, 1.8)
#   >>> LibraryBook.books_created
#   3
#   >>> db.age(2025)
#   41
#   >>> db.can_download(2.0)
#   True
#   >>> db.can_download(1.5)
#   False
#   >>> str(db)
#   'DigitalBook(Neuromancer, 1984, 1.8mb)'


class LibraryBook:
    """A physical library book tracked in a catalog.

    >>> b1 = LibraryBook("Dune", "Herbert", 1965)
    >>> b2 = LibraryBook("Foundation", "Asimov", 1951)
    >>> b1.title
    'Dune'
    >>> b1.author
    'Herbert'
    >>> b1.year
    1965
    >>> b1.age(2025)
    60
    >>> b2 < b1
    True
    >>> b1 < b2
    False
    >>> str(b1)
    'LibraryBook(Dune, 1965)'
    """
    books_created: int = 0

    def __init__(self, title: str, author: str, year: int):
        # YOUR CODE HERE
        pass

    def age(self, current_year: int) -> int:
        """Return the number of years since this book was published.

        >>> LibraryBook("X", "Y", 2000).age(2025)
        25
        >>> LibraryBook("X", "Y", 1965).age(2025)
        60
        """
        # YOUR CODE HERE
        pass

    def __lt__(self, other: "LibraryBook") -> bool:
        """Return True if this book was published earlier than other.

        >>> LibraryBook("A", "X", 1990) < LibraryBook("B", "Y", 2000)
        True
        >>> LibraryBook("A", "X", 2000) < LibraryBook("B", "Y", 1990)
        False
        >>> LibraryBook("A", "X", 1990) < LibraryBook("B", "Y", 1990)
        False
        """
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        """Return 'LibraryBook(title, year)'.

        >>> str(LibraryBook("Dune", "Herbert", 1965))
        'LibraryBook(Dune, 1965)'
        """
        # YOUR CODE HERE
        pass


class DigitalBook(LibraryBook):
    """A digital (e-book) version of a library book.

    Inherits all behavior from LibraryBook. Adds a file_size_mb attribute,
    a can_download method, and overrides __str__. Instantiating a
    DigitalBook also increments LibraryBook.books_created (via super().__init__).

    >>> db = DigitalBook("Neuromancer", "Gibson", 1984, 1.8)
    >>> db.title
    'Neuromancer'
    >>> db.file_size_mb
    1.8
    >>> db.age(2025)
    41
    >>> db.can_download(2.0)
    True
    >>> db.can_download(1.5)
    False
    >>> str(db)
    'DigitalBook(Neuromancer, 1984, 1.8mb)'
    """

    def __init__(self, title: str, author: str, year: int, file_size_mb: float):
        # YOUR CODE HERE (call super().__init__ for inherited fields)
        pass

    def can_download(self, max_mb: float) -> bool:
        """Return True if this file fits within max_mb.

        >>> DigitalBook("X", "Y", 2000, 3.0).can_download(3.0)
        True
        >>> DigitalBook("X", "Y", 2000, 3.1).can_download(3.0)
        False
        """
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        """Return 'DigitalBook(title, year, Xmb)'.

        >>> str(DigitalBook("Dune", "Herbert", 1965, 2.5))
        'DigitalBook(Dune, 1965, 2.5mb)'
        """
        # YOUR CODE HERE
        pass


# ============================================================
# FREE RESPONSE — Problem 32 (10 points)
# ============================================================
#
# A Node class for a singly linked list is provided below.
# Implement two RECURSIVE functions:
#
# 1. list_filter(head, pred) -> Node | None
#    Return a NEW linked list containing only nodes from head whose
#    values satisfy pred (i.e., pred(val) is True). Preserve order.
#    Return None if no nodes satisfy pred (or the list is empty).
#
# 2. list_map(head, func) -> Node | None
#    Return a NEW linked list where each value is replaced by
#    func(original_value). Preserve order.
#    Return None if the list is empty.
#
# Example execution:
#
#   >>> n = Node(1, Node(2, Node(3, Node(4, Node(5)))))
#   >>> print(n)
#   1 -> 2 -> 3 -> 4 -> 5 -> None
#   >>> filtered = list_filter(n, lambda x: x % 2 == 0)
#   >>> print(filtered)
#   2 -> 4 -> None
#   >>> list_filter(None, lambda x: x > 0) is None
#   True
#   >>> mapped = list_map(n, lambda x: x * x)
#   >>> print(mapped)
#   1 -> 4 -> 9 -> 16 -> 25 -> None
#   >>> list_map(None, lambda x: x + 1) is None
#   True
#   >>> odds_doubled = list_map(
#   ...     list_filter(n, lambda x: x % 2 != 0),
#   ...     lambda x: x * 2)
#   >>> print(odds_doubled)
#   2 -> 6 -> 10 -> None


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


def list_filter(head, pred):
    """Return a new linked list keeping only nodes where pred(val) is True.

    >>> n = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    >>> print(list_filter(n, lambda x: x % 2 == 0))
    2 -> 4 -> None
    >>> print(list_filter(n, lambda x: x > 3))
    4 -> 5 -> None
    >>> list_filter(None, lambda x: x > 0) is None
    True
    >>> list_filter(Node(1, Node(2, Node(3))), lambda x: x > 10) is None
    True
    """
    # YOUR CODE HERE
    pass


def list_map(head, func):
    """Return a new linked list with each value transformed by func.

    >>> n = Node(1, Node(2, Node(3)))
    >>> print(list_map(n, lambda x: x * 2))
    2 -> 4 -> 6 -> None
    >>> print(list_map(n, lambda x: x * x))
    1 -> 4 -> 9 -> None
    >>> list_map(None, lambda x: x + 1) is None
    True
    """
    # YOUR CODE HERE
    pass


# ============================================================
# FREE RESPONSE — Problem 33 (10 points)
# ============================================================
#
# A BSTNode class for a Binary Search Tree is provided below.
# Implement three RECURSIVE functions:
#
# 1. bst_insert(root, val) -> BSTNode
#    Insert val into the BST rooted at root. Return the (possibly new) root.
#    If val already exists in the tree, do NOT insert a duplicate; return
#    root unchanged.
#
# 2. bst_count_leaves(root) -> int
#    Return the number of leaf nodes (nodes with BOTH left and right == None).
#    Return 0 for an empty tree.
#
# 3. bst_range_sum(root, lo, hi) -> int
#    Return the sum of all node values v satisfying lo <= v <= hi.
#    Hint: use the BST property to PRUNE branches that cannot contain
#    values in [lo, hi] — do not recurse into a subtree if it is
#    impossible for it to hold any values in range.
#
# Example execution:
#
#   >>> root = None
#   >>> for v in [5, 3, 7, 1, 4, 6, 8]:
#   ...     root = bst_insert(root, v)
#   >>> root.val
#   5
#   >>> root.left.val
#   3
#   >>> bst_count_leaves(root)
#   4
#   >>> bst_range_sum(root, 3, 7)
#   25
#   >>> bst_range_sum(root, 1, 1)
#   1
#   >>> bst_range_sum(root, 10, 20)
#   0


class BSTNode:
    """A node in a Binary Search Tree."""
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bst_insert(root, val: int):
    """Insert val into the BST; return the new root. Ignore duplicates.

    >>> root = bst_insert(None, 5)
    >>> root.val
    5
    >>> root = bst_insert(root, 3)
    >>> root = bst_insert(root, 7)
    >>> root.left.val
    3
    >>> root.right.val
    7
    >>> root = bst_insert(root, 5)
    >>> bst_count_leaves(root)
    2
    """
    # YOUR CODE HERE
    pass


def bst_count_leaves(root) -> int:
    """Return the number of leaf nodes (no children) in the BST.

    >>> bst_count_leaves(None)
    0
    >>> bst_count_leaves(BSTNode(1))
    1
    >>> bst_count_leaves(BSTNode(5, BSTNode(3), BSTNode(7)))
    2
    """
    # YOUR CODE HERE
    pass


def bst_range_sum(root, lo: int, hi: int) -> int:
    """Return the sum of all BST values v where lo <= v <= hi.

    Uses BST ordering to skip branches outside the range.

    >>> bst_range_sum(None, 1, 10)
    0
    >>> root = BSTNode(5, BSTNode(3, BSTNode(1), BSTNode(4)),
    ...                   BSTNode(7, BSTNode(6), BSTNode(8)))
    >>> bst_range_sum(root, 3, 7)
    25
    >>> bst_range_sum(root, 1, 1)
    1
    >>> bst_range_sum(root, 10, 20)
    0
    >>> bst_range_sum(root, 1, 8)
    34
    """
    # YOUR CODE HERE
    pass


# ============================================================
# Run doctests when this file is executed directly
# ============================================================
if __name__ == "__main__":
    import doctest
    doctest.testmod()
