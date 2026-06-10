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
        self.title = title 
        self.author = author
        self.year = year
        LibraryBook.books_created += 1

    def age(self, current_year: int) -> int:
        """Return the number of years since this book was published.

        >>> LibraryBook("X", "Y", 2000).age(2025)
        25
        >>> LibraryBook("X", "Y", 1965).age(2025)
        60
        """
        return current_year - self.year

    def __lt__(self, other: "LibraryBook") -> bool:
        """Return True if this book was published earlier than other.

        >>> LibraryBook("A", "X", 1990) < LibraryBook("B", "Y", 2000)
        True
        >>> LibraryBook("A", "X", 2000) < LibraryBook("B", "Y", 1990)
        False
        >>> LibraryBook("A", "X", 1990) < LibraryBook("B", "Y", 1990)
        False
        """
        return self.year < other.year

    def __str__(self) -> str:
        """Return 'LibraryBook(title, year)'.

        >>> str(LibraryBook("Dune", "Herbert", 1965))
        'LibraryBook(Dune, 1965)'
        """
        return f"LibraryBook({self.title}, {self.year})"


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
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def can_download(self, max_mb: float) -> bool:
        """Return True if this file fits within max_mb.

        >>> DigitalBook("X", "Y", 2000, 3.0).can_download(3.0)
        True
        >>> DigitalBook("X", "Y", 2000, 3.1).can_download(3.0)
        False
        """
        return self.file_size_mb <= max_mb

    def __str__(self) -> str:
        """Return 'DigitalBook(title, year, Xmb)'.

        >>> str(DigitalBook("Dune", "Herbert", 1965, 2.5))
        'DigitalBook(Dune, 1965, 2.5mb)'
        """
        return f"DigitalBook({self.title}, {self.year}, {self.file_size_mb}mb)"


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
    if not head:
        return None
    
    if not pred(head.val):
        return list_filter(head.next, pred)

    new_node = Node(head.val)
    new_node.next = list_filter(head.next, pred)

    return new_node


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
    if not head:
        return None
    
    new_node = Node(func(head.val))
    new_node.next = list_map(head.next, func)

    return new_node


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
    if not root:
        return BSTNode(val)
    
    if not root.right or root.left:
        if root.val == val:
            return root
        if root.val > val:
            root.left = BSTNode(val)
        else:
            root.right = BSTNode(val)
        return root
    
    curr_node = root
    while curr_node.left or curr_node.right:
        if curr_node.val == val:
            break
        if curr_node.val < val:
            if not curr_node.right:
                curr_node.right = BSTNode(val)
                break
            else:
                curr_node = curr_node.right
        else:
            if not curr_node.left:
                curr_node.left = BSTNode(val)
                break
            else:
                curr_node = curr_node.left

    return root


def bst_count_leaves(root) -> int:
    """Return the number of leaf nodes (no children) in the BST.

    >>> bst_count_leaves(None)
    0
    >>> bst_count_leaves(BSTNode(1))
    1
    >>> bst_count_leaves(BSTNode(5, BSTNode(3), BSTNode(7)))
    2
    """
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1

    return bst_count_leaves(root.left) + bst_count_leaves(root.right)


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
    if not root:
        return 0

    if root.val >= lo and root.val <= hi:
        return root.val + bst_range_sum(root.left, lo, hi) + bst_range_sum(root.right, lo, hi)
    return bst_range_sum(root.left, lo, hi) + bst_range_sum(root.right, lo, hi)


# ============================================================
# Run doctests when this file is executed directly
# ============================================================
if __name__ == "__main__":
    import doctest
    doctest.testmod()
