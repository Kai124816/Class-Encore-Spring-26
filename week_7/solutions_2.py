from __future__ import annotations
import doctest
from typing import Optional


# ============================================================
# BINARY SEARCH TREE WITH STUDENT OBJECTS — Problems 1–4
# ============================================================
#
# A BSTNode holds a Student object. Students are ordered by
# their average test score (ascending). Ties are broken
# alphabetically by name (a < b means a comes first / left).

class Student:
    """A student with a name and a list of test scores.

    >>> Student("Alice", [80, 90, 100]).average()
    90.0
    >>> Student("Bob", [70, 75]).average()
    72.5
    >>> Student("Alice", [90])
    Student('Alice', avg=90.0)
    """

    def __init__(self, name: str, scores: list[int]):
        self.name = name
        self.scores = scores

    def average(self) -> float:
        """Returns the average test score for this student."""
        return sum(self.scores) / len(self.scores)

    def __repr__(self):
        return f"Student({self.name!r}, avg={self.average():.1f})"


class BSTNode:
    """A single node in a binary search tree of Students.

    Ordering rule:
      - A student with a LOWER average goes LEFT.
      - A student with a HIGHER average goes RIGHT.
      - On a tie in average, the student whose name comes
        EARLIER alphabetically goes LEFT.

    Attributes:
        student  (Student)            : the Student stored here
        left     (Optional[BSTNode])  : left subtree
        right    (Optional[BSTNode])  : right subtree

    >>> BSTNode(Student("Alice", [90])).student
    Student('Alice', avg=90.0)
    """

    def __init__(self, student: Student):
        self.student = student
        self.left:  Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

    def __repr__(self):
        return f"BSTNode({self.student!r})"

    # ----------------------------------------------------------
    # Helper – do NOT modify
    # ----------------------------------------------------------
    def _comes_before(self, a: Student, b: Student) -> bool:
        """True if student a should go to the LEFT of student b."""
        if a.average() != b.average():
            return a.average() < b.average()
        return a.name < b.name

# Problem 1
def insert(root: BSTNode, student: Student) -> None:
    """Insert a new Student into the BST rooted at root.

    Use BST ordering rules (lower average → left, higher average → right,
    alphabetical tiebreak) and insert recursively.
    Duplicate students (same name AND same average) are not inserted.

    Parameters:
        root (BSTNode): the root of the BST
        student (Student): the student to insert

    Returns:
        None

    >>> root = BSTNode(Student("Alice", [90]))
    >>> insert(root, Student("Bob", [80]))
    >>> insert(root, Student("Carol", [95]))
    >>> root.student
    Student('Alice', avg=90.0)
    >>> root.left.student
    Student('Bob', avg=80.0)
    >>> root.right.student
    Student('Carol', avg=95.0)
    >>> r2 = BSTNode(Student("Zara", [85]))
    >>> insert(r2, Student("Mia", [85]))
    >>> r2.left.student.name
    'Mia'
    >>> insert(root, Student("Alice", [90]))
    >>> count_students(root)
    3
    """
    if not root:
        root = BSTNode(student)
        return
    
    if root.student.average() == student.average() and root.student.name == student.name:
        return

    if root._comes_before(student, root.student):
        if root.left:
            insert(root.left, student)
        else:
            root.left = BSTNode(student)
    else:
        if root.right:
            insert(root.right, student)
        else:
            root.right = BSTNode(student)
    return

# Problem 2
def find_student(root: BSTNode, name: str) -> Optional[Student]:
    """Search the BST for a student with the given name.

    Because the tree is ordered by average (not name), you CANNOT use
    BST ordering to prune the search -- you must visit every node.

    Parameters:
        root (BSTNode): the root of the BST
        name (str): the name to search for

    Returns:
        Optional[Student]: the matching Student, or None if not found.

    >>> root = BSTNode(Student("Alice", [90]))
    >>> insert(root, Student("Bob", [80]))
    >>> insert(root, Student("Carol", [95]))
    >>> find_student(root, "Bob")
    Student('Bob', avg=80.0)
    >>> find_student(root, "Carol")
    Student('Carol', avg=95.0)
    >>> find_student(root, "Dave") is None
    True
    >>> find_student(root, "Alice")
    Student('Alice', avg=90.0)
    """
    if not root:
        return None
    
    if root.student.name == name:
        return root.student
    
    left_found = find_student(root.left, name)
    if left_found:
        return left_found
    
    right_found = find_student(root.right, name)
    if right_found:
        return right_found
    
    return None  

# Problem 3
def count_students(root: BSTNode) -> int:
    """Return the total number of students stored in the BST.

    Parameters:
        root (BSTNode): the root of the BST

    Returns:
        int: the number of nodes in the tree

    >>> count_students(BSTNode(Student("Alice", [90])))
    1
    >>> root = BSTNode(Student("Alice", [90]))
    >>> insert(root, Student("Bob", [80]))
    >>> insert(root, Student("Carol", [95]))
    >>> count_students(root)
    3
    >>> insert(root, Student("Dave", [85]))
    >>> count_students(root)
    4
    """
    if not root:
        return 0
    
    return 1 + count_students(root.left) + count_students(root.right)

# Problem 4
def find_above_threshold(root: BSTNode, threshold: float) -> list[Student]:
    """Return a list of all Students whose average score is STRICTLY
    greater than threshold, sorted in ascending order of average.

    Parameters:
        root (BSTNode): the root of the BST
        threshold (float): the minimum average (exclusive)

    Returns:
        list[Student]: students with average > threshold, sorted ascending

    >>> root = BSTNode(Student("Alice", [90]))
    >>> insert(root, Student("Bob", [70]))
    >>> insert(root, Student("Carol", [95]))
    >>> insert(root, Student("Dave", [85]))
    >>> [s.name for s in find_above_threshold(root, 88)]
    ['Alice', 'Carol']
    >>> [s.name for s in find_above_threshold(root, 94)]
    ['Carol']
    >>> find_above_threshold(root, 100)
    []
    >>> [s.name for s in find_above_threshold(root, 60)]
    ['Bob', 'Dave', 'Alice', 'Carol']
    """
    results = []

    if root.left and root.left.student.average() > threshold:
        results += find_above_threshold(root.left, threshold)

    if root.student.average() > threshold:
        results.append(root.student)

    if root.right:
        results += find_above_threshold(root.right, threshold)

    return results


# ============================================================
# MATRIX CLASS — Problems 5–8, 10
# ============================================================
#
# A Matrix wraps a list of lists of numbers (all rows the same length).
# The constructor makes a deep copy so external mutation has no effect.

class Matrix:
    """A 2-D matrix backed by a list of lists.

    Attributes:
        rows (list[list[int|float]]): matrix data where rows[i][j] is
            the element in row i, column j.

    >>> Matrix([[1, 2], [3, 4]])
    Matrix([[1, 2], [3, 4]])
    >>> Matrix([[1, 2], [3, 4]]).num_rows()
    2
    >>> Matrix([[1, 2], [3, 4]]).num_cols()
    2
    """

    def __init__(self, rows: list[list]):
        self.rows = [row[:] for row in rows]

    def num_rows(self) -> int:
        return len(self.rows)

    def num_cols(self) -> int:
        return len(self.rows[0]) if self.rows else 0

    def __repr__(self):
        return f"Matrix({self.rows!r})"

    # Problem 5
    def __eq__(self, other: object) -> bool:
        """Return True if other is a Matrix with identical dimensions
        and every corresponding element is equal.

        >>> Matrix([[1, 2], [3, 4]]) == Matrix([[1, 2], [3, 4]])
        True
        >>> Matrix([[1, 2], [3, 4]]) == Matrix([[1, 2], [3, 5]])
        False
        >>> Matrix([[1, 2]]) == Matrix([[1, 2], [3, 4]])
        False
        >>> Matrix([[1, 2], [3, 4]]) == "not a matrix"
        False
        """
        if not isinstance(other, Matrix):
            return False
        if self.num_rows() != other.num_rows():
            return False
        
        for i in range(len(self.rows)):
            if self.rows[i] != other.rows[i]:
                return False
        return True
            
    # Problem 6
    def __add__(self, other: Matrix) -> Matrix:
        """Return a new Matrix that is the element-wise sum of self and other.
        Raise ValueError if the matrices do not have the same dimensions.

        >>> Matrix([[1, 2], [3, 4]]) + Matrix([[5, 6], [7, 8]])
        Matrix([[6, 8], [10, 12]])
        >>> Matrix([[0, 0], [0, 0]]) + Matrix([[1, 2], [3, 4]])
        Matrix([[1, 2], [3, 4]])
        >>> Matrix([[1, 2]]) + Matrix([[3, 4], [5, 6]]) # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
            ...
        ValueError: Matrix dimensions do not match for addition.
        """
        if self.num_rows() != other.num_rows() or self.num_cols() != other.num_cols():
            raise ValueError("Matrix dimensions do not match for addition.")
        
        new_rows = [[0 for _ in range(self.num_cols())] for _ in range(self.num_rows())]

        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                new_rows[i][j] = self.rows[i][j] + other.rows[i][j]
        
        return Matrix(new_rows)

    # Problem 7
    def __mul__(self, other: Matrix) -> Matrix:
        """Return the matrix product self @ other.

        The result at position (i, j) is the dot product of row i of self
        with column j of other. Raise ValueError if dimensions are incompatible
        (self.num_cols() must equal other.num_rows()).

        >>> Matrix([[1, 2], [3, 4]]) * Matrix([[5, 6], [7, 8]])
        Matrix([[19, 22], [43, 50]])
        >>> Matrix([[1, 0], [0, 1]]) * Matrix([[3, 4], [5, 6]])
        Matrix([[3, 4], [5, 6]])
        >>> Matrix([[1, 2, 3]]) * Matrix([[4], [5], [6]])
        Matrix([[32]])
        >>> Matrix([[1, 2]]) * Matrix([[1, 2], [3, 4], [5, 6]]) # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
            ...
        ValueError: Matrix dimensions incompatible for multiplication.
        """
        if self.num_cols() != other.num_rows():
            raise ValueError("Matrix dimensions incompatible for multiplication.")
        
        result = [[0 for _ in range(other.num_cols())] for _ in range(self.num_rows())]

        # Iterate through rows of A
        for i in range(self.num_rows()):
            # Iterate through columns of B
            for j in range(other.num_cols()):
                # Iterate through rows of B
                for k in range(other.num_rows()):
                    result[i][j] += self.rows[i][k] * other.rows[k][j]
        
        return Matrix(result)

    # Problem 8
    def count_nonzero(self) -> int:
        """Return the number of elements that are NOT equal to zero.

        >>> Matrix([[1, 0, 3], [0, 0, 6]]).count_nonzero()
        3
        >>> Matrix([[0, 0], [0, 0]]).count_nonzero()
        0
        >>> Matrix([[1, 2], [3, 4]]).count_nonzero()
        4
        """
        count = 0
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                if self.rows[i][j] != 0:
                    count += 1
        return count

    def sparsity(self) -> float:
        """Return the fraction of elements that ARE zero as a float in [0.0, 1.0].

        sparsity = (number of zero elements) / (total elements)
        Returns 0.0 for an empty matrix.

        >>> Matrix([[1, 0, 3], [0, 0, 6]]).sparsity()
        0.5
        >>> Matrix([[0, 0], [0, 0]]).sparsity()
        1.0
        >>> Matrix([[1, 2], [3, 4]]).sparsity()
        0.0
        """
        total_elements = self.num_rows() * self.num_cols()
        return (total_elements - self.count_nonzero()) / total_elements

    def is_sparse(self, threshold: float = 0.5) -> bool:
        """Return True if sparsity() is STRICTLY greater than threshold.

        The default threshold is 0.5 (more than half the elements are zero).

        >>> Matrix([[1, 0, 0], [0, 0, 0]]).is_sparse()
        True
        >>> Matrix([[1, 0], [1, 1]]).is_sparse()
        False
        >>> Matrix([[1, 0, 0, 0], [0, 0, 0, 0]]).is_sparse(0.6)
        True
        >>> Matrix([[1, 0], [0, 1]]).is_sparse(0.5)
        False
        """
        return self.sparsity() > threshold

    # Problem 9
    def transpose(self) -> Matrix:
        """Return a NEW Matrix that is the transpose of self.

        The transpose swaps rows and columns: result.rows[i][j] = self.rows[j][i].
        The original matrix must NOT be modified.

        >>> Matrix([[1, 2, 3], [4, 5, 6]]).transpose()
        Matrix([[1, 4], [2, 5], [3, 6]])
        >>> Matrix([[1, 2], [3, 4]]).transpose()
        Matrix([[1, 3], [2, 4]])
        >>> Matrix([[5]]).transpose()
        Matrix([[5]])
        >>> m = Matrix([[1, 2, 3]])
        >>> m.transpose()
        Matrix([[1], [2], [3]])
        >>> m
        Matrix([[1, 2, 3]])
        """
        new_rows = [[0 for _ in range(self.num_rows())] for _ in range(self.num_cols())]
        
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                new_rows[j][i] = self.rows[i][j]
        
        return Matrix(new_rows)

# ============================================================
# To test a single problem, uncomment that problem's line below.
# ============================================================
if __name__ == "__main__":
    import doctest

    # --- Problem 1: insert ---
    doctest.run_docstring_examples(insert, globs=None, name="insert")

    # --- Problem 2: find_student ---
    doctest.run_docstring_examples(find_student, globs=None, name="find_student")

    # --- Problem 3: count_students ---
    doctest.run_docstring_examples(count_students, globs=None, name="count_students")

    # --- Problem 4: find_above_threshold ---
    doctest.run_docstring_examples(find_above_threshold, globs=None, name="find_above_threshold")

    # --- Problem 5: Matrix.__eq__ ---
    doctest.run_docstring_examples(Matrix.__eq__, globs=None, name="Matrix.__eq__")

    # --- Problem 6: Matrix.__add__ ---
    doctest.run_docstring_examples(Matrix.__add__, globs=None, name="Matrix.__add__")

    # --- Problem 7: Matrix.__mul__ ---
    doctest.run_docstring_examples(Matrix.__mul__, globs=None, name="Matrix.__mul__")

    # --- Problem 8: Matrix sparsity ---
    doctest.run_docstring_examples(Matrix.count_nonzero, globs=None, name="Matrix.count_nonzero")
    doctest.run_docstring_examples(Matrix.sparsity, globs=None, name="Matrix.sparsity")
    doctest.run_docstring_examples(Matrix.is_sparse, globs=None, name="Matrix.is_sparse")

    # --- Problem 9: Matrix.transpose ---
    doctest.run_docstring_examples(Matrix.transpose, globs=None, name="Matrix.transpose")