from __future__ import annotations
import doctest
from typing import Optional


# ============================================================
# BINARY TREE — Problems 1–3
# ============================================================
#
# A BinaryTree is a recursive data structure where each node
# holds a value and has an optional left and right child,
# each of which is itself a BinaryTree (or None).

class BinaryTree:
    """A node in a binary tree.

    Attributes:
        value: The value stored at this node.
        left (Optional[BinaryTree]): The left subtree, or None.
        right (Optional[BinaryTree]): The right subtree, or None.
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


# Problem 1
def tree_sum(tree: Optional[BinaryTree]) -> int:
    """Return the sum of all values stored in the binary tree.
    Return 0 if tree is None.

    Parameters:
        tree (Optional[BinaryTree]): The root of a binary tree of ints,
            or None.

    Returns:
        int: The sum of all node values.

    >>> tree_sum(None)
    0
    >>> tree_sum(BinaryTree(5))
    5
    >>> tree_sum(BinaryTree(1, BinaryTree(2), BinaryTree(3)))
    6
    >>> t = BinaryTree(10, BinaryTree(3, BinaryTree(1), BinaryTree(2)), BinaryTree(5))
    >>> tree_sum(t)
    21
    """
    # YOUR CODE HERE
    pass


# Problem 2
def tree_height(tree: Optional[BinaryTree]) -> int:
    """Return the height of the binary tree.
    The height of a single-node tree is 0.
    The height of None is -1.

    Parameters:
        tree (Optional[BinaryTree]): The root of a binary tree, or None.

    Returns:
        int: The height of the tree.

    >>> tree_height(None)
    -1
    >>> tree_height(BinaryTree(1))
    0
    >>> tree_height(BinaryTree(1, BinaryTree(2), None))
    1
    >>> t = BinaryTree(1, BinaryTree(2, BinaryTree(4), None), BinaryTree(3))
    >>> tree_height(t)
    2
    """
    # YOUR CODE HERE
    pass


# Problem 3
def inorder(tree: Optional[BinaryTree]) -> list:
    """Return a list of all values in the tree using an in-order traversal
    (left subtree, current node, right subtree).
    Return an empty list if tree is None.

    Parameters:
        tree (Optional[BinaryTree]): The root of a binary tree, or None.

    Returns:
        list: Values visited in in-order sequence.

    >>> inorder(None)
    []
    >>> inorder(BinaryTree(1))
    [1]
    >>> inorder(BinaryTree(2, BinaryTree(1), BinaryTree(3)))
    [1, 2, 3]
    >>> t = BinaryTree(4, BinaryTree(2, BinaryTree(1), BinaryTree(3)), BinaryTree(6, BinaryTree(5), BinaryTree(7)))
    >>> inorder(t)
    [1, 2, 3, 4, 5, 6, 7]
    """
    # YOUR CODE HERE
    pass


# ============================================================
# NESTED LIST — Problems 4–6
# ============================================================
#
# A NestedList is a recursive data structure where each node
# is either a Leaf (holding a single integer) or an Inner node
# (holding a list of child NestedList nodes).
#
# You must complete both classes before solving problems 4–6.

class NestedList:
    """Abstract base for a recursive nested-list structure."""

    def sum(self) -> int:
        """Return the sum of all integer values in this structure."""
        raise NotImplementedError

    def depth(self) -> int:
        """Return the maximum nesting depth.
        A Leaf has depth 0. An Inner node has depth 1 + max child depth.
        An Inner node with no children has depth 1.
        """
        raise NotImplementedError

    def flatten(self) -> list[int]:
        """Return a flat list of all integers in this structure, in order."""
        raise NotImplementedError


class Leaf(NestedList):
    """A leaf node holding a single integer value.

    Attributes:
        value (int): The integer stored at this leaf.
    """

    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f"Leaf({self.value!r})"

    # Problem 4 — implement sum, depth, flatten for Leaf
    def sum(self) -> int:
        """
        >>> Leaf(3).sum()
        3
        >>> Leaf(0).sum()
        0
        """
        # YOUR CODE HERE
        pass

    def depth(self) -> int:
        """
        >>> Leaf(3).depth()
        0
        """
        # YOUR CODE HERE
        pass

    def flatten(self) -> list[int]:
        """
        >>> Leaf(3).flatten()
        [3]
        """
        # YOUR CODE HERE
        pass


class Inner(NestedList):
    """An inner node holding a list of child NestedList nodes.

    Attributes:
        children (list[NestedList]): The child nodes (may be empty).
    """

    def __init__(self, children: list[NestedList]):
        self.children = children

    def __repr__(self):
        return f"Inner({self.children!r})"

    # Problem 5 — implement sum, depth, flatten for Inner
    def sum(self) -> int:
        """
        >>> Inner([Leaf(1), Leaf(2), Leaf(3)]).sum()
        6
        >>> Inner([]).sum()
        0
        >>> Inner([Inner([Leaf(1), Leaf(2)]), Leaf(3)]).sum()
        6
        """
        # YOUR CODE HERE
        pass

    def depth(self) -> int:
        """
        >>> Inner([Leaf(1), Leaf(2), Leaf(3)]).depth()
        1
        >>> Inner([]).depth()
        1
        >>> Inner([Inner([Leaf(1), Leaf(2)]), Leaf(3)]).depth()
        2
        """
        # YOUR CODE HERE
        pass

    def flatten(self) -> list[int]:
        """
        >>> Inner([Leaf(1), Leaf(2), Leaf(3)]).flatten()
        [1, 2, 3]
        >>> Inner([]).flatten()
        []
        >>> Inner([Inner([Leaf(1), Leaf(2)]), Leaf(3)]).flatten()
        [1, 2, 3]
        """
        # YOUR CODE HERE
        pass


# Problem 6
def nested_max(nl: NestedList) -> int:
    """Return the maximum integer value stored anywhere in the NestedList.
    You may assume the structure contains at least one Leaf.
    Use the flatten() method you implemented above.

    Parameters:
        nl (NestedList): A NestedList containing at least one Leaf.

    Returns:
        int: The maximum value found.

    >>> nested_max(Leaf(7))
    7
    >>> nested_max(Inner([Leaf(3), Leaf(9), Leaf(1)]))
    9
    >>> nested_max(Inner([Inner([Leaf(5), Leaf(2)]), Leaf(8), Inner([Leaf(4)])]))
    8
    """
    # YOUR CODE HERE (one or two lines using flatten)
    pass



# ============================================================
# BINARY SEARCH TREE — Problems 7–8
# ============================================================
#
# A BinarySearchTree inherits from BinaryTree and maintains the
# BST property: every value in the left subtree is less than
# the node's value, and every value in the right subtree is
# greater than the node's value.

class BinarySearchTree(BinaryTree):
    """A binary search tree node.

    Inherits from BinaryTree. All values must be comparable with < and >.
    The BST property must be maintained:
        - All values in the left subtree are strictly less than self.value.
        - All values in the right subtree are strictly greater than self.value.

    Use the inherited __init__ and __repr__ from BinaryTree.
    """

    def insert(self, val) -> None:
        """Insert val into the BST in the correct position, modifying the
        tree in place. If val is already present, do nothing.

        Parameters:
            val: A comparable value to insert.

        Returns:
            None

        >>> t = BinarySearchTree(5)
        >>> t.insert(3)
        >>> inorder(t)
        [3, 5]
        >>> t.insert(7)
        >>> t.insert(1)
        >>> t.insert(4)
        >>> inorder(t)
        [1, 3, 4, 5, 7]
        >>> t.insert(5)
        >>> inorder(t)
        [1, 3, 4, 5, 7]
        """
        # YOUR CODE HERE
        pass

    def contains(self, val) -> bool:
        """Return True if val is present anywhere in this BST.
        Use the BST property to search efficiently (do NOT traverse every node).

        Parameters:
            val: A comparable value to search for.

        Returns:
            bool: True if val is in the tree, False otherwise.

        >>> t = BinarySearchTree(5)
        >>> t.insert(3)
        >>> t.insert(7)
        >>> t.insert(1)
        >>> t.insert(4)
        >>> t.contains(1)
        True
        >>> t.contains(4)
        True
        >>> t.contains(6)
        False
        >>> t.contains(10)
        False
        """
        # YOUR CODE HERE
        pass


# Problem 7
def build_bst(values: list) -> Optional[BinarySearchTree]:
    """Build a BST by inserting values from the list left to right.
    Return None if the list is empty.

    Parameters:
        values (list): A list of comparable values.

    Returns:
        Optional[BinarySearchTree]: The resulting BST, or None if values is empty.

    >>> build_bst([]) is None
    True
    >>> inorder(build_bst([5]))
    [5]
    >>> t = build_bst([5, 3, 7, 1, 4])
    >>> inorder(t)
    [1, 3, 4, 5, 7]
    >>> t2 = build_bst([3, 1, 4, 1, 5, 9, 2, 6])
    >>> inorder(t2)
    [1, 2, 3, 4, 5, 6, 9]
    """
    # YOUR CODE HERE
    pass


# Problem 8
def is_valid_bst(tree: Optional[BinaryTree],
                 min_val=None, max_val=None) -> bool:
    """Return True if tree satisfies the BST property at every node.
    Return True if tree is None (an empty tree is a valid BST).
    Hint: Use the inorder function defined above

    Use the min_val and max_val parameters to track the allowed range
    for each subtree:
        - Every node's value must be strictly greater than min_val (if set).
        - Every node's value must be strictly less than max_val (if set).

    Parameters:
        tree (Optional[BinaryTree]): A binary tree to validate.
        min_val: The lower bound (exclusive) on allowable values, or None.
        max_val: The upper bound (exclusive) on allowable values, or None.

    Returns:
        bool: True if tree is a valid BST.

    >>> is_valid_bst(None)
    True
    >>> is_valid_bst(BinaryTree(5))
    True
    >>> is_valid_bst(BinaryTree(5, BinaryTree(3), BinaryTree(7)))
    True
    >>> is_valid_bst(BinaryTree(5, BinaryTree(7), BinaryTree(3)))
    False
    >>> is_valid_bst(BinaryTree(5, BinaryTree(3, BinaryTree(1), BinaryTree(4)), BinaryTree(7)))
    True
    >>> bad = BinaryTree(5, BinaryTree(3, BinaryTree(1), BinaryTree(6)), BinaryTree(7))
    >>> is_valid_bst(bad)
    False
    """
    # YOUR CODE HERE
    pass

# ============================================================
# FILESYSTEM — Problems 9-11
# ============================================================
#
# A filesystem is an N-ary tree where each node is either a
# File (a leaf with a name and size in bytes) or a Directory
# (an inner node with a name and a list of children, each of
# which is itself an FSNode).
#
# Example tree:
#
#   Directory("root")
#   ├── File("readme.txt", 200)
#   ├── File("notes.txt", 150)
#   └── Directory("src")
#       ├── File("main.py", 500)
#       └── File("util.py", 300)

class FSNode:
    """Abstract base for a filesystem entry (file or directory).

    Attributes:
        name (str): The name of this entry.
    """

    def __init__(self, name: str):
        self.name = name

    def is_file(self) -> bool:
        """Return True if this node is a File, False if it is a Directory."""
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError


class File(FSNode):
    """A leaf node representing a file with a fixed size.

    Attributes:
        name (str): The filename.
        size (int): The size of the file in bytes.

    >>> File("readme.txt", 200).name
    'readme.txt'
    >>> File("readme.txt", 200).size
    200
    >>> File("readme.txt", 200).is_file()
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
    """An inner node representing a directory that holds children.

    Attributes:
        name (str): The directory name.
        children (list[FSNode]): Files and subdirectories inside this directory.

    >>> d = Directory("src")
    >>> d.is_file()
    False
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.children: list[FSNode] = []

    #Problem 9 implement add child for FSNode
    def add_child(self, child: FSNode) -> None:
        """Add a file or subdirectory to this directory's children.

        >>> d = Directory("root")
        >>> d.add_child(File("readme.txt", 200))
        >>> d.add_child(File("notes.txt", 150))
        >>> len(d.children)
        2
        >>> d.children[0].name
        'readme.txt'
        """
        # YOUR CODE HERE
        pass

    def is_file(self) -> bool:
        return False

    def __repr__(self) -> str:
        return f"Directory({self.name!r}, {self.children!r})"


# Problem 10
def fs_total_size(node: FSNode) -> int:
    """Return the total size in bytes of all files reachable from node.
    If node is a File, return its size.
    If node is a Directory, return the sum of sizes of all files
    contained within it, recursively.

    Parameters:
        node (FSNode): A File or Directory node.

    Returns:
        int: Total size in bytes of all files under node.

    >>> fs_total_size(File("readme.txt", 200))
    200
    >>> d = Directory("src")
    >>> d.add_child(File("main.py", 500))
    >>> d.add_child(File("util.py", 300))
    >>> fs_total_size(d)
    800
    >>> root = Directory("root")
    >>> root.add_child(File("readme.txt", 200))
    >>> root.add_child(File("notes.txt", 150))
    >>> src = Directory("src")
    >>> src.add_child(File("main.py", 500))
    >>> src.add_child(File("util.py", 300))
    >>> root.add_child(src)
    >>> fs_total_size(root)
    1150
    >>> fs_total_size(Directory("empty"))
    0
    """
    # YOUR CODE HERE
    pass

# Problem 11
def fs_count_name(node: FSNode, target: str) -> int:
    """Return the number of files (not directories) anywhere in the
    filesystem subtree rooted at node whose name exactly matches target.

    Parameters:
        node (FSNode): The root of the filesystem subtree to search.
        target (str): The filename to count.

    Returns:
        int: The number of files with that name.

    >>> fs_count_name(File("readme.txt", 200), "readme.txt")
    1
    >>> fs_count_name(File("readme.txt", 200), "other.txt")
    0
    >>> fs_count_name(Directory("readme.txt"), "readme.txt")
    0
    >>> root = Directory("root")
    >>> src = Directory("src")
    >>> tests = Directory("tests")
    >>> root.add_child(File("readme.txt", 100))
    >>> root.add_child(src)
    >>> root.add_child(tests)
    >>> src.add_child(File("main.py", 500))
    >>> src.add_child(File("readme.txt", 50))
    >>> tests.add_child(File("main.py", 200))
    >>> tests.add_child(File("notes.txt", 80))
    >>> fs_count_name(root, "readme.txt")
    2
    >>> fs_count_name(root, "main.py")
    2
    >>> fs_count_name(root, "notes.txt")
    1
    >>> fs_count_name(root, "missing.txt")
    0
    """
    # YOUR CODE HERE
    pass


# To test a single problem, uncomment that problem's line below.
# ============================================================
if __name__ == "__main__":
    import doctest

    # --- Problem 1: tree_sum ---
    # doctest.run_docstring_examples(tree_sum, globs=None, name="tree_sum")

    # --- Problem 2: tree_height ---
    # doctest.run_docstring_examples(tree_height, globs=None, name="tree_height")

    # --- Problem 3: inorder ---
    # doctest.run_docstring_examples(inorder, globs=None, name="inorder")

    # --- Problem 4: Leaf (sum / depth / flatten) ---
    # doctest.run_docstring_examples(Leaf.sum, globs=None, name="Leaf.sum")
    # doctest.run_docstring_examples(Leaf.depth, globs=None, name="Leaf.depth")
    # doctest.run_docstring_examples(Leaf.flatten, globs=None, name="Leaf.flatten")

    # --- Problem 5: Inner (sum / depth / flatten) ---
    # doctest.run_docstring_examples(Inner.sum, globs=None, name="Inner.sum")
    # doctest.run_docstring_examples(Inner.depth, globs=None, name="Inner.depth")
    # doctest.run_docstring_examples(Inner.flatten, globs=None, name="Inner.flatten")

    # --- Problem 6: nested_max ---
    # doctest.run_docstring_examples(nested_max, globs=None, name="nested_max")

    # --- Problem 7: build_bst ---
    # doctest.run_docstring_examples(build_bst, globs=None, name="build_bst")

    # --- Problem 8: is_valid_bst ---
    # doctest.run_docstring_examples(is_valid_bst, globs=None, name="is_valid_bst")

    # --- Problem 9: FileSystem setup (FSNode.add_child) ---
    # doctest.run_docstring_examples(Directory.add_child, globs=None, name="Directory.add_child")

    # --- Problem 10: fs_total_size ---
    # doctest.run_docstring_examples(fs_total_size, globs=None, name="fs_total_size")

    # --- Problem 11: fs_count_name ---
    # doctest.run_docstring_examples(fs_count_name, globs=None, name="fs_count_name")