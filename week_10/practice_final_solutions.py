from __future__ import annotations
import doctest
from abc import ABC, abstractmethod
from typing import Optional


# ============================================================
# CS 211 — PRACTICE FINAL EXAM
# ============================================================
#
# This file covers concepts from Weeks 1–9:
#   Problems 1–3  : OOP — new classes, inheritance, class variables
#   Problems 4–5  : Recursion — expression trees, linked lists
#   Problems 6–7  : Trees — binary trees, binary search trees
#   Problem  8    : Filesystem — N-ary trees
#   Problems 9–10 : Binary numbers, nested structures


# ============================================================
# OOP SECTION — Problems 1–3
# ============================================================


# ------------------------------------------------------------------
# Problem 1 — Duration
# ------------------------------------------------------------------
#
# Implement a Duration class that represents a time duration in
# hours, minutes, and seconds.

class Duration:
    """Represents a time duration stored as hours, minutes, and seconds.

    Attributes:
        hours   (int): the hours component (non-negative)
        minutes (int): the minutes component (0–59)
        seconds (int): the seconds component (0–59)

    >>> Duration(1, 30, 0).hours
    1
    >>> Duration(1, 30, 0).minutes
    30
    >>> Duration(0, 0, 45).seconds
    45
    >>> str(Duration(1, 5, 9))
    '01:05:09'
    """

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def total_seconds(self) -> int:
        """Return the total number of seconds this Duration represents.

        >>> Duration(0, 0, 0).total_seconds()
        0
        >>> Duration(0, 1, 0).total_seconds()
        60
        >>> Duration(1, 0, 0).total_seconds()
        3600
        >>> Duration(1, 30, 15).total_seconds()
        5415
        """
        return (3600 * self.hours) + (60 * self.minutes) + self.seconds

    def __eq__(self, other: object) -> bool:
        """Return True if self and other represent the same total duration.

        >>> Duration(0, 1, 0) == Duration(0, 1, 0)
        True
        >>> Duration(1, 0, 0) == Duration(0, 59, 60)
        True
        >>> Duration(1, 0, 0) == Duration(0, 59, 0)
        False
        """
        if type(other) == Duration:
            return self.total_seconds() == other.total_seconds()
        return False
 
    def __lt__(self, other: "Duration") -> bool:
        """Return True if self is a shorter duration than other.

        >>> Duration(0, 1, 0) < Duration(0, 2, 0)
        True
        >>> Duration(1, 0, 0) < Duration(0, 59, 59)
        False
        >>> Duration(0, 1, 0) < Duration(0, 1, 0)
        False
        """
        if type(other) == Duration:
            return self.total_seconds() < other.total_seconds()
        return False

    def __add__(self, other: "Duration") -> "Duration":
        """Return a new Duration equal to the sum of self and other.

        Hint: add total_seconds() for both, then convert back to H/M/S.

        >>> str(Duration(0, 30, 0) + Duration(0, 30, 0))
        '01:00:00'
        >>> str(Duration(1, 45, 30) + Duration(0, 14, 30))
        '02:00:00'
        >>> str(Duration(0, 0, 0) + Duration(2, 3, 4))
        '02:03:04'
        """
        total_seconds = self.total_seconds() + other.total_seconds()
        total_minutes = total_seconds // 60
        total_hours = total_minutes // 60
    
        
        return Duration(total_hours, total_minutes % 60, total_seconds % 60)

    def __str__(self) -> str:
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# ------------------------------------------------------------------
# Problem 2 — Subscription(Service)
# ------------------------------------------------------------------
#
# PROVIDED BASE CLASS (do not modify):

class Service:
    """A service with a name and monthly fee.

    >>> s = Service("Streaming", 9.99)
    >>> s.annual_cost()
    119.88
    >>> str(s)
    'Service(Streaming)'
    """

    def __init__(self, name: str, monthly_fee: float):
        self.name = name
        self.monthly_fee = monthly_fee

    def annual_cost(self) -> float:
        """Return the standard annual cost (monthly_fee * 12)."""
        return round(self.monthly_fee * 12, 2)

    def __str__(self) -> str:
        return f"Service({self.name})"


class Subscription(Service):
    """A Subscription is a Service that tracks how long the user has been
    subscribed. Long-term subscribers receive a 10% annual discount.

    Rules:
        - Inherit name and monthly_fee from Service using super().__init__.
        - Add months_active: int as a third __init__ parameter.
        - Override annual_cost() to return the standard annual cost with
          a 10% discount if months_active >= 12; no discount otherwise.
        - Add total_paid() -> float that returns monthly_fee * months_active while
        also factoring in the discount if months active >= 12.
        - Override __str__ to return
          "Subscription(<name>, <months_active> months)".

    >>> s1 = Subscription("Streaming", 10.0, 6)
    >>> s1.annual_cost()
    120.0
    >>> s2 = Subscription("Streaming", 10.0, 24)
    >>> s2.annual_cost()
    108.0
    >>> s1.total_paid()
    60.0
    >>> s2.total_paid()
    228.0
    >>> str(s1)
    'Subscription(Streaming, 6 months)'
    >>> str(s2)
    'Subscription(Streaming, 24 months)'
    """

    def __init__(self, name: str, monthly_fee: float, months_active: int):
        # YOUR CODE HERE (use super().__init__)
        super().__init__(name, monthly_fee)
        self.months_active = months_active

    def annual_cost(self) -> float:
        if self.months_active < 12:
            return self.monthly_fee * 12
        
        non_discounted_fee = self.monthly_fee * 12
        return non_discounted_fee * 0.9

    def total_paid(self) -> float:
        non_discounted_months = min(self.months_active, 12)
        discounted_months = max(0, self.months_active - 12)

        discounted_rate = self.monthly_fee * 0.9
        return (self.monthly_fee * non_discounted_months) + (discounted_rate* discounted_months)

    def __str__(self) -> str:
        return f'Subscription({self.name}, {self.months_active} months)'


# ------------------------------------------------------------------
# Problem 3 — ScoreBoard (class variable)
# ------------------------------------------------------------------
#
# Implement a ScoreBoard class that tracks every score ever submitted
# across ALL ScoreBoard instances using a class variable.

class ScoreBoard:
    """Tracks player scores and maintains a class-wide record of all
    scores ever submitted across every ScoreBoard instance.

    Class variable:
        all_scores (list[int]): all scores recorded by any instance.

    >>> ScoreBoard.all_scores = []  # reset for testing
    >>> sb1 = ScoreBoard("Alice")
    >>> sb2 = ScoreBoard("Bob")
    >>> sb1.record(150)
    >>> sb2.record(200)
    >>> sb1.record(175)
    >>> ScoreBoard.all_scores
    [150, 200, 175]
    >>> sb1.high_score()
    200
    >>> str(sb1)
    'ScoreBoard(Alice)'
    """

    all_scores: list = []  # class variable — do not move this

    def __init__(self, player: str):
        """Store the player's name. Do NOT reset all_scores.

        >>> ScoreBoard.all_scores = []
        >>> sb = ScoreBoard("Dana")
        >>> sb.player
        'Dana'
        """
        self.player = player

    def record(self, score: int) -> None:
        """Append score to ScoreBoard.all_scores.

        >>> ScoreBoard.all_scores = []
        >>> sb = ScoreBoard("Eve")
        >>> sb.record(50)
        >>> sb.record(80)
        >>> ScoreBoard.all_scores
        [50, 80]
        """
        ScoreBoard.all_scores.append(score)

    def high_score(self) -> int:
        """Return the highest score in ScoreBoard.all_scores.
        Assumes at least one score has been recorded.

        >>> ScoreBoard.all_scores = []
        >>> sb = ScoreBoard("Frank")
        >>> sb.record(42)
        >>> sb.record(99)
        >>> sb.record(17)
        >>> sb.high_score()
        99
        """
        return max(ScoreBoard.all_scores)

    def __str__(self) -> str:
        """Return 'ScoreBoard(<player>)'.

        >>> str(ScoreBoard("Grace"))
        'ScoreBoard(Grace)'
        """
        return f'ScoreBoard({self.player})'


# ============================================================
# EXPRESSION TREE — Problem 4
# ============================================================
#
# PROVIDED (do not modify):

class Expr(ABC):
    """Abstract base for expression tree nodes."""
    @abstractmethod
    def eval(self) -> int: ...
    @abstractmethod
    def __str__(self) -> str: ...

class Lit(Expr):
    """A literal integer node."""
    def __init__(self, value: int):
        self.value = value
    def eval(self) -> int:
        return self.value
    def __str__(self) -> str:
        return f"Lit({self.value})"

class BinOp(Expr, ABC):
    """Abstract binary operation node with a left and right child."""
    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right
    @abstractmethod
    def op_symbol(self) -> str: ...
    def __str__(self) -> str:
        return f"({self.left} {self.op_symbol()} {self.right})"

class Add(BinOp):
    """Addition node: left + right."""
    def op_symbol(self) -> str: return "+"
    def eval(self) -> int: return self.left.eval() + self.right.eval()

class Mul(BinOp):
    """Multiplication node: left * right."""
    def op_symbol(self) -> str: return "*"
    def eval(self) -> int: return self.left.eval() * self.right.eval()


# ------------------------------------------------------------------
# Problem 4 — max_literal
# ------------------------------------------------------------------
def max_literal(expr: Expr) -> int:
    """Return the maximum integer value stored in any Lit node in the
    expression tree.

    Visits every node recursively. You may assume the tree contains at
    least one Lit node.

    Parameters:
        expr (Expr): The root of an expression tree.

    Returns:
        int: The largest integer value stored in any Lit node.

    >>> max_literal(Lit(7))
    7
    >>> max_literal(Add(Lit(3), Lit(9)))
    9
    >>> max_literal(Mul(Add(Lit(10), Lit(4)), Add(Lit(2), Lit(7))))
    10
    >>> max_literal(Add(Mul(Lit(5), Lit(1)), Mul(Lit(3), Lit(8))))
    8
    """
    if isinstance(expr, Lit):
        return expr.eval()
    
    max_left = max_literal(expr.left)
    max_right = max_literal(expr.right)
    return max(max_left, max_right)


# ============================================================
# LINKED LIST — Problem 5
# ============================================================
#
# PROVIDED (do not modify):

class ListNode:
    """A node in a singly-linked list.

    >>> str(ListNode(1, ListNode(2, ListNode(3, None))))
    '[1 -> 2 -> 3]'
    >>> str(ListNode(42, None))
    '[42]'
    """
    def __init__(self, value: int, next: "ListNode | None" = None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        parts = []
        node = self
        while node is not None:
            parts.append(str(node.value))
            node = node.next
        return "[" + " -> ".join(parts) + "]"


# ------------------------------------------------------------------
# Problem 5 — list_remove_all
# ------------------------------------------------------------------
def list_remove_all(node: "ListNode | None", target: int) -> "ListNode | None":
    """Recursively return a new linked list with all nodes whose value
    equals target removed. The original list must NOT be modified.

    Parameters:
        node   (ListNode | None): the head of the linked list.
        target (int)            : the value to remove.

    Returns:
        ListNode | None: the head of the filtered list, or None if empty.

    >>> list_remove_all(None, 5) is None
    True
    >>> str(list_remove_all(ListNode(1, ListNode(2, ListNode(3, None))), 4))
    '[1 -> 2 -> 3]'
    >>> str(list_remove_all(ListNode(1, ListNode(2, ListNode(1, None))), 1))
    '[2]'
    >>> list_remove_all(ListNode(3, ListNode(3, ListNode(3, None))), 3) is None
    True
    >>> str(list_remove_all(ListNode(1, ListNode(2, ListNode(3, None))), 2))
    '[1 -> 3]'
    """
    if not node:
        return None
    
    if node.value == target:
        return list_remove_all(node.next, target)
    
    new_node = ListNode(node.value, list_remove_all(node.next, target))
    return new_node


# ============================================================
# BINARY TREE — Problems 6–7
# ============================================================
#
# PROVIDED (do not modify):

class BinaryTree:
    """A node in a binary tree.

    Attributes:
        value: the value stored at this node.
        left  (Optional[BinaryTree]): the left subtree, or None.
        right (Optional[BinaryTree]): the right subtree, or None.

    >>> BinaryTree(5)
    BinaryTree(5)
    >>> BinaryTree(1, BinaryTree(2), BinaryTree(3))
    BinaryTree(1, BinaryTree(2), BinaryTree(3))
    """

    def __init__(self, value, left: Optional["BinaryTree"] = None,
                 right: Optional["BinaryTree"] = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left is None and self.right is None:
            return f"BinaryTree({self.value!r})"
        return f"BinaryTree({self.value!r}, {self.left!r}, {self.right!r})"


class BinarySearchTree(BinaryTree):
    """A BST node. Inherits from BinaryTree.

    BST property: all values in the left subtree are strictly less than
    self.value; all values in the right subtree are strictly greater.

    insert() and contains() are provided — do not modify them.
    """

    def insert(self, val) -> None:
        """Insert val into the BST in-place. Duplicates are ignored."""
        if val < self.value:
            if self.left is None:
                self.left = BinarySearchTree(val)
            else:
                self.left.insert(val)
        elif val > self.value:
            if self.right is None:
                self.right = BinarySearchTree(val)
            else:
                self.right.insert(val)

    def contains(self, val) -> bool:
        """Return True if val is present in this BST."""
        if val == self.value:
            return True
        elif val < self.value:
            return self.left is not None and self.left.contains(val)
        else:
            return self.right is not None and self.right.contains(val)


# ------------------------------------------------------------------
# Problem 6 — preorder
# ------------------------------------------------------------------
def preorder(tree: Optional[BinaryTree]) -> list:
    """Return a list of all values in the tree using a preorder traversal:
    visit the current node FIRST, then the left subtree, then the right.
    Return an empty list if tree is None.

    Parameters:
        tree (Optional[BinaryTree]): the root of a binary tree, or None.

    Returns:
        list: values visited in preorder sequence.

    >>> preorder(None)
    []
    >>> preorder(BinaryTree(1))
    [1]
    >>> preorder(BinaryTree(2, BinaryTree(1), BinaryTree(3)))
    [2, 1, 3]
    >>> t = BinaryTree(4, BinaryTree(2, BinaryTree(1), BinaryTree(3)), BinaryTree(6, BinaryTree(5), BinaryTree(7)))
    >>> preorder(t)
    [4, 2, 1, 3, 6, 5, 7]
    """
    if not tree:
        return []
    
    return [tree.value] + preorder(tree.left) + preorder(tree.right)


# ------------------------------------------------------------------
# Problem 7 — bst_in_range
# ------------------------------------------------------------------
def bst_in_range(tree: Optional[BinarySearchTree], lo: int, hi: int) -> list:
    """Return a sorted list of all values in the BST that fall within
    the inclusive range [lo, hi].

    Use the BST property to prune the search:
        - If tree.value < lo, the current node and its entire left subtree
          cannot be in range — only recurse into the right subtree.
        - If tree.value > hi, the current node and its entire right subtree
          cannot be in range — only recurse into the left subtree.
        - Otherwise include tree.value and recurse on both subtrees.

    Parameters:
        tree (Optional[BinarySearchTree]): the BST root, or None.
        lo   (int): inclusive lower bound.
        hi   (int): inclusive upper bound.

    Returns:
        list: values in [lo, hi] in ascending order.

    >>> bst_in_range(None, 1, 10)
    []
    >>> t = BinarySearchTree(5)
    >>> t.insert(3)
    >>> t.insert(7)
    >>> t.insert(1)
    >>> t.insert(4)
    >>> t.insert(6)
    >>> t.insert(9)
    >>> bst_in_range(t, 3, 7)
    [3, 4, 5, 6, 7]
    >>> bst_in_range(t, 5, 5)
    [5]
    >>> bst_in_range(t, 8, 10)
    [9]
    >>> bst_in_range(t, 0, 2)
    [1]
    """
    if not tree:
        return []
    
    if tree.value > hi:
        return bst_in_range(tree.left, lo, hi)
    if tree.value < lo:
        return bst_in_range(tree.right, lo, hi)
    
    return bst_in_range(tree.left, lo, hi) + [tree.value] + bst_in_range(tree.right, lo, hi)

# ============================================================
# FILESYSTEM — Problem 8
# ============================================================
#
# PROVIDED (do not modify):

class FSNode:
    """Abstract base for a filesystem entry (file or directory)."""
    def __init__(self, name: str):
        self.name = name

    def is_file(self) -> bool:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError


class File(FSNode):
    """A file with a name and size in bytes.

    >>> File("data.csv", 1024).name
    'data.csv'
    >>> File("data.csv", 1024).size
    1024
    >>> File("data.csv", 1024).is_file()
    True
    """
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def is_file(self) -> bool:
        return True

    def __repr__(self) -> str:
        return f"File({self.name!r}, {self.size})"


class Directory(FSNode):
    """A directory that holds child FSNodes.

    >>> d = Directory("docs")
    >>> d.is_file()
    False
    """
    def __init__(self, name: str):
        super().__init__(name)
        self.children: list[FSNode] = []

    def add_child(self, child: FSNode) -> None:
        self.children.append(child)

    def is_file(self) -> bool:
        return False

    def __repr__(self) -> str:
        return f"Directory({self.name!r}, {self.children!r})"


# ------------------------------------------------------------------
# Problem 8 — fs_largest_file
# ------------------------------------------------------------------
def fs_largest_file(node: FSNode) -> Optional[File]:
    """Return the File with the most bytes in the filesystem subtree
    rooted at node. Return None if the subtree contains no files.
    If two files share the largest size, return the first one encountered
    in a depth-first traversal (children visited left to right).

    Parameters:
        node (FSNode): a File or Directory node.

    Returns:
        Optional[File]: the largest File, or None if no files exist.

    >>> fs_largest_file(File("a.txt", 300))
    File('a.txt', 300)
    >>> fs_largest_file(Directory("empty")) is None
    True
    >>> root = Directory("root")
    >>> root.add_child(File("small.txt", 100))
    >>> root.add_child(File("big.txt", 900))
    >>> root.add_child(File("medium.txt", 500))
    >>> fs_largest_file(root)
    File('big.txt', 900)
    >>> nested = Directory("root")
    >>> sub = Directory("sub")
    >>> sub.add_child(File("deep.py", 2000))
    >>> nested.add_child(File("top.py", 1500))
    >>> nested.add_child(sub)
    >>> fs_largest_file(nested)
    File('deep.py', 2000)
    """
    if node.is_file():
        return node
    
    if len(node.children) == 0:
        return None
    
    largest_child = File("placeholder", -1)
    for child in node.children:
        curr_child = fs_largest_file(child)
        if curr_child.size > largest_child.size:
            largest_child = curr_child
    
    return largest_child


# ============================================================
# BINARY NUMBER — Problem 9
# ============================================================
#
# PROVIDED (do not modify):

class BinaryNumber:
    """An unsigned binary number stored as a list of booleans (MSB first).

    >>> BinaryNumber([True, False, True]).bits
    [True, False, True]
    >>> BinaryNumber([True, False, True])
    BinaryNumber(101)
    """

    def __init__(self, bits: list[bool]):
        self.bits = bits

    def __repr__(self):
        digits = "".join("1" if b else "0" for b in self.bits)
        return f"BinaryNumber({digits})"

    def __eq__(self, other):
        if not isinstance(other, BinaryNumber):
            return NotImplemented
        return self.to_int() == other.to_int()

    def to_int(self) -> int:
        """Converts this BinaryNumber to its integer value.

        >>> BinaryNumber([True, False, True]).to_int()
        5
        >>> BinaryNumber([True, True, False]).to_int()
        6
        """
        total = 0
        for bit in self.bits:
            total = total * 2 + (1 if bit else 0)
        return total


# ------------------------------------------------------------------
# Problem 9 — binary_xor
# ------------------------------------------------------------------
def binary_xor(a: BinaryNumber, b: BinaryNumber) -> int:
    """Performs a bitwise XOR on two BinaryNumber objects and returns
    the result as a Python int.

    Bitwise XOR: a result bit is True (1) if the corresponding bits
    in a and b DIFFER, and False (0) if they are the SAME.

    If the two numbers have different lengths, pad the shorter one on
    the LEFT with False bits before performing the XOR.

    You may NOT use Python's built-in ^ operator or convert to int first.
    Compute the XOR bit-by-bit.

    Parameters:
        a (BinaryNumber): The first operand.
        b (BinaryNumber): The second operand.

    Returns:
        int: The integer value of (a XOR b).

    >>> binary_xor(BinaryNumber([True, False, True]), BinaryNumber([True, True, False]))
    3
    >>> binary_xor(BinaryNumber([True, False, True]), BinaryNumber([True, False, True]))
    0
    >>> binary_xor(BinaryNumber([False]), BinaryNumber([False]))
    0
    >>> binary_xor(BinaryNumber([True, True]), BinaryNumber([False, False, True, True]))
    0
    >>> binary_xor(BinaryNumber([True, False, True]), BinaryNumber([True, True]))
    6
    """
    len_a, len_b = len(a.bits), len(b.bits)
    padded_length = max(len_a, len_b)
    bits_a = [False] * (max(len_a, len_b) - len_a) + a.bits
    bits_b = [False] * (max(len_a, len_b) - len_b) + b.bits

    acc = 0
    bit_val = 2 ** (padded_length - 1)
    for i in range(padded_length):
        if bits_a[i] and not bits_b[i]:
            acc += bit_val
        elif not bits_a[i] and bits_b[i]:
            acc += bit_val
        bit_val //= 2
    
    return acc

# ============================================================
# NESTED STRUCTURES — Problem 10
# ============================================================

# ------------------------------------------------------------------
# Problem 10 — nested_list_depth
# ------------------------------------------------------------------
def nested_list_depth(lst) -> int:
    """Return the maximum nesting depth of a possibly-nested list.

    Rules:
        - A non-list value has depth 0.
        - A list has depth 1 + the maximum depth of its elements.
          (An empty list has depth 1, since max over empty = 0.)

    Parameters:
        lst: A possibly-nested list (or a non-list value).

    Returns:
        int: The maximum nesting depth.

    >>> nested_list_depth([])
    1
    >>> nested_list_depth([1, 2, 3])
    1
    >>> nested_list_depth([[1, 2], [3, 4]])
    2
    >>> nested_list_depth([1, [2, [3, [4]]]])
    4
    >>> nested_list_depth([[[], []]])
    3
    >>> nested_list_depth([1, "hello", 3.14])
    1
    """
    if not isinstance(lst, list):
        return 0
    
    max_nested_depth = 0
    for el in lst:
        curr_depth = nested_list_depth(el)
        if curr_depth > max_nested_depth:
            max_nested_depth = curr_depth
    
    return max_nested_depth + 1

# ============================================================
# To test a single problem, uncomment that problem's line below.
# ============================================================
if __name__ == "__main__":
    import doctest

    # --- Problem 1: Duration ---
    doctest.run_docstring_examples(Duration.total_seconds, globs=None, name="Duration.total_seconds")
    doctest.run_docstring_examples(Duration.__eq__, globs=None, name="Duration.__eq__")
    doctest.run_docstring_examples(Duration.__lt__, globs=None, name="Duration.__lt__")
    doctest.run_docstring_examples(Duration.__add__, globs=None, name="Duration.__add__")

    #--- Problem 2: Subscription ---
    doctest.run_docstring_examples(Subscription, globs=None, name="Subscription")

    #--- Problem 3: ScoreBoard ---
    doctest.run_docstring_examples(ScoreBoard.__init__, globs=None, name="ScoreBoard.__init__")
    doctest.run_docstring_examples(ScoreBoard.record, globs=None, name="ScoreBoard.record")
    doctest.run_docstring_examples(ScoreBoard.high_score, globs=None, name="ScoreBoard.high_score")
    doctest.run_docstring_examples(ScoreBoard.__str__, globs=None, name="ScoreBoard.__str__")

    #--- Problem 4: max_literal ---
    doctest.run_docstring_examples(max_literal, globs=None, name="max_literal")

    #--- Problem 5: list_remove_all ---
    doctest.run_docstring_examples(list_remove_all, globs=None, name="list_remove_all")

    #--- Problem 6: preorder ---
    doctest.run_docstring_examples(preorder, globs=None, name="preorder")

    #--- Problem 7: bst_in_range ---
    doctest.run_docstring_examples(bst_in_range, globs=None, name="bst_in_range")

    #--- Problem 8: fs_largest_file ---
    doctest.run_docstring_examples(fs_largest_file, globs=None, name="fs_largest_file")

    #--- Problem 9: binary_xor ---
    doctest.run_docstring_examples(binary_xor, globs=None, name="binary_xor")

    #--- Problem 10: nested_list_depth ---
    doctest.run_docstring_examples(nested_list_depth, globs=None, name="nested_list_depth")