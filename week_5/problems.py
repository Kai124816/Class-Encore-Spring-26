import doctest
from abc import ABC, abstractmethod

# ============================================================
# OBJECT-ORIENTED RECURSION, MAGIC METHODS,
# CLASS VARIABLES, AND INHERITANCE PROBLEMS (1–10)
# ============================================================

# ------------------------------------------------------------
# Background: Expression Tree
# Problems 1–4 share these node classes.
# ------------------------------------------------------------

class Expr(ABC):
    """Abstract base class for all expression nodes."""

    @abstractmethod
    def eval(self) -> int:
        """Evaluate the expression and return its integer value."""
        ...

    @abstractmethod
    def __str__(self) -> str:
        """Return a human-readable string representation."""
        ...


class Lit(Expr):
    """A literal integer value, e.g. Lit(5) represents the number 5."""

    def __init__(self, value: int):
        self.value = value

    def __str__(self) -> str:
        return f"Lit({self.value})"

    def eval(self) -> int:
        return self.value


class BinOp(Expr):
    """Abstract base for binary operations (two child expressions)."""

    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    @abstractmethod
    def op_symbol(self) -> str:
        """Return the operator symbol, e.g. '+', '-', '*'."""
        ...

    def __str__(self) -> str:
        return f"({self.left} {self.op_symbol()} {self.right})"


class Add(BinOp):
    """Represents addition: left + right."""

    def op_symbol(self) -> str:
        return "+"

    def eval(self) -> int:
        """
        >>> Add(Lit(3), Lit(4)).eval()
        7
        >>> Add(Add(Lit(1), Lit(2)), Lit(3)).eval()
        6
        """
        return self.left.eval() + self.right.eval()


class Mul(BinOp):
    """Represents multiplication: left * right."""

    def op_symbol(self) -> str:
        return "*"

    def eval(self) -> int:
        """
        >>> Mul(Lit(3), Lit(4)).eval()
        12
        >>> Mul(Add(Lit(2), Lit(3)), Lit(5)).eval()
        25
        """
        return self.left.eval() * self.right.eval()


# ------------------------------------------------------------
# Problem 1
# ------------------------------------------------------------
def count_nodes(expr: Expr) -> int:
    """
    Returns the total number of nodes in the expression tree.
    A Lit node counts as 1. A BinOp node counts as 1 plus the
    counts of its two children.

    >>> count_nodes(Lit(7))
    1
    >>> count_nodes(Add(Lit(1), Lit(2)))
    3
    >>> count_nodes(Mul(Add(Lit(1), Lit(2)), Lit(3)))
    5
    >>> count_nodes(Add(Mul(Lit(2), Lit(3)), Add(Lit(4), Lit(5))))
    7
    """
    # YOUR CODE HERE
    pass
    

# ------------------------------------------------------------
# Problem 2
# ------------------------------------------------------------
def tree_depth(expr: Expr) -> int:
    """
    Returns the depth of the expression tree (the length of the
    longest path from the root to a leaf).
    A single Lit node has depth 1.

    >>> tree_depth(Lit(5))
    1
    >>> tree_depth(Add(Lit(1), Lit(2)))
    2
    >>> tree_depth(Mul(Add(Lit(1), Lit(2)), Lit(3)))
    3
    >>> tree_depth(Add(Mul(Lit(2), Add(Lit(3), Lit(4))), Lit(1)))
    4
    """
    # YOUR CODE HERE
    pass


# ------------------------------------------------------------
# Problem 3
# ------------------------------------------------------------
def collect_literals(expr: Expr) -> list[int]:
    """
    Returns a list of all literal values in the expression tree,
    gathered left-to-right (in-order traversal of leaves).

    >>> collect_literals(Lit(7))
    [7]
    >>> collect_literals(Add(Lit(1), Lit(2)))
    [1, 2]
    >>> collect_literals(Mul(Add(Lit(3), Lit(1)), Add(Lit(4), Lit(1))))
    [3, 1, 4, 1]
    """
    # YOUR CODE HERE
    pass


# ------------------------------------------------------------
# Problem 4
# ------------------------------------------------------------
def substitute(expr: Expr, old_val: int, new_val: int) -> Expr:
    """
    Returns a NEW expression tree where every Lit node whose value
    equals old_val is replaced by a Lit node with value new_val.
    The original tree must not be modified.

    >>> str(substitute(Lit(3), 3, 10))
    'Lit(10)'
    >>> str(substitute(Lit(5), 3, 10))
    'Lit(5)'
    >>> str(substitute(Add(Lit(3), Lit(3)), 3, 10))
    '(Lit(10) + Lit(10))'
    >>> str(substitute(Mul(Add(Lit(2), Lit(3)), Lit(3)), 3, 0))
    '((Lit(2) + Lit(0)) * Lit(0))'
    """
    # YOUR CODE HERE
    pass

# ============================================================
# Background: Linked List
# Problems 5–7 share a recursive linked-list structure.
# ============================================================

class ListNode:
    """
    A single node in a singly-linked list.
    __str__ shows the list from this node onward.

    >>> str(ListNode(1, ListNode(2, ListNode(3, None))))
    '[1 -> 2 -> 3]'
    >>> str(ListNode(42, None))
    '[42]'
    """

    def __init__(self, value: int, next: "ListNode | None"):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        parts = []
        node = self
        while node is not None:
            parts.append(str(node.value))
            node = node.next
        return "[" + " -> ".join(parts) + "]"


# ------------------------------------------------------------
# Problem 5
# ------------------------------------------------------------
def list_sum(node: "ListNode | None") -> int:
    """
    Recursively returns the sum of all values in the linked list.
    Returns 0 for an empty list (None).

    >>> list_sum(None)
    0
    >>> list_sum(ListNode(5, None))
    5
    >>> list_sum(ListNode(1, ListNode(2, ListNode(3, None))))
    6
    >>> list_sum(ListNode(10, ListNode(20, ListNode(30, None))))
    60
    """
    # YOUR CODE HERE
    pass


# ------------------------------------------------------------
# Problem 6
# ------------------------------------------------------------
def list_max(node: "ListNode | None") -> "int | None":
    """
    Recursively returns the maximum value in the linked list.
    Returns None for an empty list.

    >>> list_max(None) is None
    True
    >>> list_max(ListNode(7, None))
    7
    >>> list_max(ListNode(3, ListNode(9, ListNode(1, None))))
    9
    >>> list_max(ListNode(5, ListNode(5, ListNode(5, None))))
    5
    """
    # YOUR CODE HERE
    pass

# ------------------------------------------------------------
# Problem 7
# ------------------------------------------------------------
def list_count(node: "ListNode | None", target: int) -> int:
    """
    Recursively returns the number of times target appears
    in the linked list. Returns 0 for an empty list (None).
 
    >>> list_count(None, 5)
    0
    >>> list_count(ListNode(3, None), 3)
    1
    >>> list_count(ListNode(1, ListNode(2, ListNode(1, None))), 1)
    2
    >>> list_count(ListNode(4, ListNode(4, ListNode(4, None))), 4)
    3
    >>> list_count(ListNode(1, ListNode(2, ListNode(3, None))), 9)
    0
    """
    # YOUR CODE HERE
    pass
   

# ============================================================
# Background: Vector / Matrix Hierarchy
# Problems 8–10 use class variables
# and inheritance with an abstract LinearObject base.
# ============================================================
 
class LinearObject:
    """
    Abstract base class for linear-algebra objects (vectors and matrices).
    Tracks the total number of LinearObject instances ever created
    in the class variable `instance_count`.
    """
 
    instance_count: int = 0  # counts ALL LinearObject subclass instances
 
    def __init__(self):
        LinearObject.instance_count += 1
 
    @abstractmethod
    def scale(self, factor: float) -> "LinearObject":
        """Return a NEW object with every element multiplied by factor."""
        ...
 
    @abstractmethod
    def __str__(self) -> str:
        """Return a human-readable string representation."""
        ...
 
    def __eq__(self, other: object) -> bool:
        """
        Two LinearObjects are equal if they are the same type AND
        contain the same elements (compared with ==).
        """
        if type(self) is not type(other):
            return False
        return str(self) == str(other)
 

# ------------------------------------------------------------
# Problem 8 — Vector
# ------------------------------------------------------------
class Vector(LinearObject):
    """
    A 1-D vector storing a list of floats.
 
    Students must implement:
        __init__   — store elements; call super().__init__()
        magnitude  — square root of sum of squared elements
        dot        — dot product with another Vector of the same length;
                     raise ValueError if lengths differ
        scale      — return a NEW Vector with each element multiplied
                     by factor (do NOT modify self)
        __eq__     — True if other is a Vector with identical elements
        __add__    — return a NEW Vector with element-wise sums;
                     raise ValueError if lengths differ
 
    >>> v = Vector([3.0, 4.0])
    >>> str(v)
    'Vector([3.0, 4.0])'
    >>> v.magnitude()
    5.0
    >>> v.dot(Vector([1.0, 2.0]))
    11.0
    >>> str(v.scale(2.0))
    'Vector([6.0, 8.0])'
    >>> Vector([1.0, 2.0]) == Vector([1.0, 2.0])
    True
    >>> Vector([1.0, 2.0]) == Vector([1.0, 3.0])
    False
    >>> Vector([1.0, 2.0]) == Matrix([[1.0, 2.0]])
    False
    >>> str(Vector([1.0, 2.0]) + Vector([3.0, 4.0]))
    'Vector([4.0, 6.0])'
    >>> str(Vector([0.0, 0.0]) + Vector([5.0, 5.0]))
    'Vector([5.0, 5.0])'
    >>> Vector([1.0, 2.0]) + Vector([1.0, 2.0, 3.0])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ValueError: ...
    """
 
    def __init__(self, elements: list[float]):
        # YOUR CODE HERE
        pass
 
    def magnitude(self) -> float:
        """Return the Euclidean magnitude (length) of the vector."""
        # YOUR CODE HERE
        pass
 
    def dot(self, other: "Vector") -> float:
        """
        Return the dot product of self and other.
        Raise ValueError if the vectors have different lengths.
        """
        # YOUR CODE HERE
        pass
 
    def scale(self, factor: float) -> "Vector":
        # YOUR CODE HERE
        pass
 
    def __eq__(self, other: object) -> bool:
        """True if other is a Vector with identical elements."""
        # YOUR CODE HERE
        pass
 
    def __add__(self, other: "Vector") -> "Vector":
        """
        Return a NEW Vector with element-wise sums.
        Raise ValueError if the vectors have different lengths.
        """
        # YOUR CODE HERE
        pass
 
    def __str__(self) -> str:
        return f"Vector({self.elements})"  
 
 
# ------------------------------------------------------------
# Problem 9 — Matrix
# ------------------------------------------------------------
class Matrix(LinearObject):
    """
    A 2-D matrix storing a list of rows, where each row is a list of floats.
    You may assume all rows have the same length.
 
    Students must implement:
        __init__     — store rows; call super().__init__()
        num_rows     — return the number of rows
        num_cols     — return the number of columns (length of first row,
                       or 0 if there are no rows)
        transpose    — return a NEW Matrix that is the transpose of self
                       (rows become columns); do NOT modify self
        scale        — return a NEW Matrix with every element multiplied
                       by factor; do NOT modify self
        __eq__       — True if other is a Matrix of the same type with
                       identical rows
        __add__      — return a NEW Matrix with element-wise sums;
                       raise ValueError if dimensions differ
 
    >>> m = Matrix([[1.0, 2.0], [3.0, 4.0]])
    >>> str(m)
    'Matrix([[1.0, 2.0], [3.0, 4.0]])'
    >>> m.num_rows()
    2
    >>> m.num_cols()
    2
    >>> str(m.scale(2.0))
    'Matrix([[2.0, 4.0], [6.0, 8.0]])'
    >>> Matrix([[1.0, 2.0], [3.0, 4.0]]) == Matrix([[1.0, 2.0], [3.0, 4.0]])
    True
    >>> Matrix([[1.0, 2.0], [3.0, 4.0]]) == Matrix([[1.0, 2.0], [3.0, 5.0]])
    False
    >>> Matrix([[1.0, 2.0], [3.0, 4.0]]) == Vector([1.0, 2.0])
    False
    >>> str(Matrix([[1.0, 2.0], [3.0, 4.0]]) + Matrix([[5.0, 6.0], [7.0, 8.0]]))
    'Matrix([[6.0, 8.0], [10.0, 12.0]])'
    >>> str(Matrix([[0.0, 0.0], [0.0, 0.0]]) + Matrix([[1.0, 2.0], [3.0, 4.0]]))
    'Matrix([[1.0, 2.0], [3.0, 4.0]])'
    >>> Matrix([[1.0, 2.0]]) + Matrix([[1.0, 2.0], [3.0, 4.0]])  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    ValueError: ...
    """
 
    def __init__(self, rows: list[list[float]]):
        # YOUR CODE HERE
        pass
 
    def num_rows(self) -> int:
        # YOUR CODE HERE
        pass
 
    def num_cols(self) -> int:
       # YOUR CODE HERE
        pass
 
    def scale(self, factor: float) -> "Matrix":
        # YOUR CODE HERE
        pass
        
    def __eq__(self, other: object) -> bool:
        """True if other is a Matrix of the same type with identical rows."""
        # YOUR CODE HERE
        pass
 
    def __add__(self, other: "Matrix") -> "Matrix":
        """
        Return a NEW Matrix with element-wise sums.
        Raise ValueError if the dimensions differ.
        """
        # YOUR CODE HERE
        pass  
 
    def __str__(self) -> str:
        return f"Matrix({self.rows})"

 
# ============================================================
# Problem 10 — Greatest Magnitude
# ============================================================
def greatest_magnitude(vectors: list[Vector]) -> Vector:
    """
    Takes in a list of vectors and returns the vector with the
    greatest magnitude in the list. If two vectors have the same
    magnitude the one that came first is returned.
 
    >>> str(greatest_magnitude([Vector([3.0, 4.0])]))
    'Vector([3.0, 4.0])'
    >>> str(greatest_magnitude([Vector([1.0, 0.0]), Vector([3.0, 4.0]), Vector([1.0, 2.0])]))
    'Vector([3.0, 4.0])'
    >>> str(greatest_magnitude([Vector([3.0, 4.0]), Vector([0.0, 5.0])]))
    'Vector([3.0, 4.0])'
    >>> str(greatest_magnitude([Vector([1.0, 1.0]), Vector([1.0, 1.0])]))
    'Vector([1.0, 1.0])'
    """
    # YOUR CODE HERE
    pass
 
 
# ============================================================
# Run doctests when this file is executed directly.
# To test a single problem, comment out the others below.
# ============================================================
if __name__ == "__main__":
    import doctest
 
    # --- Problem 1: Add.eval / Mul.eval ---
    # doctest.run_docstring_examples(Add.eval, globs=None, name="Add.eval")
    # doctest.run_docstring_examples(Mul.eval, globs=None, name="Mul.eval")
 
    # --- Problem 1: count_nodes ---
    # doctest.run_docstring_examples(count_nodes, globs=None, name="count_nodes")
 
    # --- Problem 2: tree_depth ---
    # doctest.run_docstring_examples(tree_depth, globs=None, name="tree_depth")
 
    # --- Problem 3: collect_literals ---
    # doctest.run_docstring_examples(collect_literals, globs=None, name="collect_literals")
 
    # --- Problem 4: substitute ---
    # doctest.run_docstring_examples(substitute, globs=None, name="substitute")
 
    # --- Problem 5: list_sum ---
    # doctest.run_docstring_examples(list_sum, globs=None, name="list_sum")
 
    # --- Problem 6: list_max ---
    # doctest.run_docstring_examples(list_max, globs=None, name="list_max")
 
    # --- Problem 7: list_count ---
    # doctest.run_docstring_examples(list_count, globs=None, name="list_count")
 
    # --- Problem 8: Vector ---
    # doctest.run_docstring_examples(Vector, globs=None, name="Vector")
 
    # --- Problem 9: Matrix ---
    # doctest.run_docstring_examples(Matrix, globs=None, name="Matrix")
 
    # --- Problem 10: Greatest Magnitude ---
    # doctest.run_docstring_examples(greatest_magnitude, globs=None, name="greatest_magnitude")