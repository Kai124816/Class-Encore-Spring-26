from __future__ import annotations
import doctest
from typing import Optional


# ============================================================
# BINARY NUMBER CLASS — Problems 1–5, 9
# ============================================================
#
# A binary number is a number expressed in base 2, using only
# the digits 0 and 1. For example:
#   - The integer 5 in binary is 101  (1*4 + 0*2 + 1*1)
#   - The integer 6 in binary is 110  (1*4 + 1*2 + 0*1)
#
# In our BinaryNumber class, we store the binary digits as a
# list of booleans, where:
#   - False represents 0
#   - True  represents 1
#
# The list is stored with the MOST SIGNIFICANT BIT (MSB) first.
# For example, the number 5 (binary 101) is stored as:
#   [True, False, True]
#
# We support the following operations:
#   - Translate to int           (Problem 1)
#   - Greater-than comparison    (Problem 2)
#   - Less-than comparison       (Problem 3)
#   - Left shift / Right shift   (Problem 4)
#   - Log base 2                 (Problem 5)
#   - Add two binary numbers     (Problem 9)

class BinaryNumber:
    """A binary number stored as a list of booleans (MSB first).

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

    # Problem 1
    def to_int(self) -> int:
        """Translates this BinaryNumber to its integer equivalent.

        The MSB is at index 0. Each bit b at position i (from the right)
        contributes b * 2^i to the total.

        Returns:
            int: The integer value of this binary number.

        >>> BinaryNumber([False]).to_int()
        0
        >>> BinaryNumber([True]).to_int()
        1
        >>> BinaryNumber([True, False, True]).to_int()
        5
        >>> BinaryNumber([True, True, False]).to_int()
        6
        >>> BinaryNumber([True, False, False, False]).to_int()
        8
        """
        # YOUR CODE HERE
        pass

    # Problem 2
    def __gt__(self, other: BinaryNumber) -> bool:
        """Returns True if this BinaryNumber is strictly greater than other.

        Hint: Convert both to integers and compare.

        >>> BinaryNumber([True, False, True]) > BinaryNumber([True, True])
        True
        >>> BinaryNumber([True, True]) > BinaryNumber([True, False, True])
        False
        >>> BinaryNumber([True, True]) > BinaryNumber([True, True])
        False
        """
        # YOUR CODE HERE
        pass

    # Problem 3
    def __lt__(self, other: BinaryNumber) -> bool:
        """Returns True if this BinaryNumber is strictly less than other.

        Hint: Convert both to integers and compare.

        >>> BinaryNumber([True, False, True]) < BinaryNumber([True, True])
        False
        >>> BinaryNumber([True, True]) < BinaryNumber([True, False, True])
        True
        >>> BinaryNumber([True, True]) < BinaryNumber([True, True])
        False
        """
        # YOUR CODE HERE
        pass

    # Problem 4
    def __lshift__(self, n: int) -> BinaryNumber:
        """Returns a new BinaryNumber shifted LEFT by n positions.

        Left-shifting by 1 appends a False (0) to the right, which
        is equivalent to multiplying by 2.

        Parameters:
            n (int): Number of positions to shift left (non-negative).

        Returns:
            BinaryNumber: A new BinaryNumber representing the shifted value.

        >>> BinaryNumber([True, False, True]) << 1
        BinaryNumber(1010)
        >>> BinaryNumber([True, False, True]) << 2
        BinaryNumber(10100)
        >>> BinaryNumber([True]) << 3
        BinaryNumber(1000)
        """
        # YOUR CODE HERE
        pass

    def __rshift__(self, n: int) -> BinaryNumber:
        """Returns a new BinaryNumber shifted RIGHT by n positions.

        Right-shifting by 1 removes the last bit, which is equivalent
        to integer division by 2. If all bits are shifted away, return
        BinaryNumber([False]) (i.e. 0).

        Parameters:
            n (int): Number of positions to shift right (non-negative).

        Returns:
            BinaryNumber: A new BinaryNumber representing the shifted value.

        >>> BinaryNumber([True, False, True]) >> 1
        BinaryNumber(10)
        >>> BinaryNumber([True, False, True]) >> 2
        BinaryNumber(1)
        >>> BinaryNumber([True, False, True]) >> 3
        BinaryNumber(0)
        """
        # YOUR CODE HERE
        pass


# Problem 4 (continued): Int to BinaryNumber
def int_to_binary(n: int) -> BinaryNumber:
    """Converts a non-negative integer into a BinaryNumber.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        BinaryNumber: The binary representation of n.

    Hint: Repeatedly divide n by 2 and collect remainders.
          Remember that the remainders come out LSB-first.

    >>> int_to_binary(0)
    BinaryNumber(0)
    >>> int_to_binary(1)
    BinaryNumber(1)
    >>> int_to_binary(5)
    BinaryNumber(101)
    >>> int_to_binary(6)
    BinaryNumber(110)
    >>> int_to_binary(8)
    BinaryNumber(1000)
    """
    # Special case: 0 has no remainder when divided, so handle it directly.
    if n == 0:
        return BinaryNumber([False])
 
    bits = []  # remainders collected here, LSB-first
 
    # YOUR CODE HERE: loop while n > 0.
    # Each iteration: append (n % 2 == 1) to bits, then set n = n // 2.
    # Hint: after the loop, bits is in the wrong order — reverse it!
 
    return BinaryNumber(bits)


# Problem 5
def log_base_2(b: BinaryNumber) -> int:
    """Returns the floor of log base 2 of the given BinaryNumber.

    Recall that log2(x) answers: "2 to what power equals x?"
    For example:
        log2(8)  = 3  because 2^3 = 8
        log2(5)  = 2  because 2^2 = 4 <= 5 < 8 = 2^3  (floor)
        log2(1)  = 0  because 2^0 = 1

    The result is always rounded DOWN (floor).

    Parameters:
        b (BinaryNumber): A BinaryNumber with value >= 1.

    Returns:
        int: The floor of log2 of b's integer value.

    Hint: Think about what the number of bits in a binary number
          tells you about its log base 2.

    >>> log_base_2(BinaryNumber([True]))
    0
    >>> log_base_2(BinaryNumber([True, False]))
    1
    >>> log_base_2(BinaryNumber([True, False, True]))
    2
    >>> log_base_2(BinaryNumber([True, False, False, False]))
    3
    """
    # YOUR CODE HERE
    pass


# ============================================================
# QUEUE CLASS — Problems 6–8
# ============================================================
#
# A queue is a data structure that follows the
# FIFO (First-In, First-Out) principle — think of it like a
# line of people waiting at a coffee shop. The first person
# to join the line is the first person to be served.
#
# Key operations:
#   enqueue  — Add an item to the BACK of the queue
#   dequeue  — Remove and return the item from the FRONT
#   peek     — Look at the front item WITHOUT removing it
#
# Example:
#   Start:        queue = []
#   enqueue("A"): queue = ["A"]
#   enqueue("B"): queue = ["A", "B"]
#   enqueue("C"): queue = ["A", "B", "C"]
#   dequeue():    returns "A", queue = ["B", "C"]
#   peek():       returns "B", queue = ["B", "C"]  (unchanged)

class Queue:
    """A FIFO queue.

    >>> q = Queue()
    >>> q.is_empty()
    True
    >>> len(q)
    0
    """

    def __init__(self):
        self._data = []

    def is_empty(self) -> bool:
        """Returns True if the queue has no elements."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Returns the number of elements in the queue."""
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue(front={self._data})"

    # Problem 6
    def enqueue(self, item) -> None:
        """Adds item to the BACK of the queue.

        Parameters:
            item: Any value to add to the queue.

        Returns:
            None

        >>> q = Queue()
        >>> q.enqueue(1)
        >>> q.enqueue(2)
        >>> q.enqueue(3)
        >>> len(q)
        3
        >>> q.is_empty()
        False
        """
        # YOUR CODE HERE
        pass

    # Problem 7
    def dequeue(self):
        """Removes and returns the item from the FRONT of the queue.
        Raises an IndexError if the queue is empty.

        Returns:
            The front item of the queue.

        >>> q = Queue()
        >>> q.enqueue("A")
        >>> q.enqueue("B")
        >>> q.enqueue("C")
        >>> q.dequeue()
        'A'
        >>> q.dequeue()
        'B'
        >>> len(q)
        1
        """
        # YOUR CODE HERE
        pass

    # Problem 8
    def peek(self):
        """Returns the item at the FRONT of the queue WITHOUT removing it.
        Raises an IndexError if the queue is empty.

        Returns:
            The front item of the queue.

        >>> q = Queue()
        >>> q.enqueue(10)
        >>> q.enqueue(20)
        >>> q.peek()
        10
        >>> len(q)
        2
        >>> q.dequeue()
        10
        >>> q.peek()
        20
        """
        # YOUR CODE HERE
        pass


# Problem 9
def add_binary(a: BinaryNumber, b: BinaryNumber) -> BinaryNumber:
    """Returns a new BinaryNumber representing the sum of a and b.

    You may NOT convert to int, add, then convert back.
    Instead, implement binary addition directly using the following rules:

    Binary addition works column by column from right to left, just like
    decimal addition — but with a carry that triggers at 2 instead of 10:

        0 + 0 = 0,  carry 0
        0 + 1 = 1,  carry 0
        1 + 0 = 1,  carry 0
        1 + 1 = 0,  carry 1   (2 in binary is 10)
        1 + 1 + 1 (carry) = 1, carry 1

    Example:
          1 0 1   (5)
        + 0 1 1   (3)
        -------
          1 0 0 0  (8)

    Parameters:
        a (BinaryNumber): The first operand.
        b (BinaryNumber): The second operand.

    Returns:
        BinaryNumber: The sum a + b as a BinaryNumber.

    >>> add_binary(BinaryNumber([True, False, True]), BinaryNumber([True, True]))
    BinaryNumber(1000)
    >>> add_binary(BinaryNumber([True]), BinaryNumber([True]))
    BinaryNumber(10)
    >>> add_binary(BinaryNumber([False]), BinaryNumber([False]))
    BinaryNumber(0)
    >>> add_binary(BinaryNumber([True, True, True]), BinaryNumber([True]))
    BinaryNumber(1000)
    """
    # Pad the shorter list with False on the LEFT so both are the same length.
    # Example: [True, True] and [True, False, True]
    #       -> [False, True, True] and [True, False, True]
    len_a, len_b = len(a.bits), len(b.bits)
    bits_a = [False] * (max(len_a, len_b) - len_a) + a.bits
    bits_b = [False] * (max(len_a, len_b) - len_b) + b.bits

    result = []  # will hold the answer bits, built right-to-left
    carry = False

    # YOUR CODE HERE: iterate over bits_a and bits_b from RIGHT to LEFT.
    # At each position, compute the sum of the two bits plus the carry,
    # then determine the result bit and the new carry.
    # Hint: think of True as 1 and False as 0.

    # After the loop, don't forget to prepend the carry if it's still True!

    return BinaryNumber(result)


# Problem 10
def dict_depth(d: dict) -> int:
    """Returns the depth of a nested dictionary.

    The depth is defined as the length of the longest chain of nested
    dictionaries. A dictionary with no nested dict values has depth 1.
    An empty dict also has depth 1.

    Parameters:
        d (dict): A dictionary that may contain other dictionaries as values.

    Returns:
        int: The maximum nesting depth.

    Examples:
        {}                       -> depth 1
        {"a": 1}                 -> depth 1   (value is not a dict)
        {"a": {"b": 2}}          -> depth 2
        {"a": {"b": {"c": 3}}}   -> depth 3
        {"a": 1, "b": {"c": 2}}  -> depth 2   (take the deeper branch)

    >>> dict_depth({})
    1
    >>> dict_depth({"a": 1, "b": 2})
    1
    >>> dict_depth({"a": {"b": 2}})
    2
    >>> dict_depth({"a": {"b": {"c": 3}}})
    3
    >>> dict_depth({"x": 1, "y": {"z": {"w": 4}}, "v": {"u": 0}})
    3
    """
    # YOUR CODE HERE
    pass


# ============================================================
# To test a single problem, uncomment that problem's line below.
# ============================================================
if __name__ == "__main__":
    import doctest

    # --- Problem 1: BinaryNumber.to_int ---
    # doctest.run_docstring_examples(BinaryNumber.to_int, globs=None, name="BinaryNumber.to_int")

    # --- Problem 2: BinaryNumber.__gt__ ---
    # doctest.run_docstring_examples(BinaryNumber.__gt__, globs=None, name="BinaryNumber.__gt__")

    # --- Problem 3: BinaryNumber.__lt__ ---
    # doctest.run_docstring_examples(BinaryNumber.__lt__, globs=None, name="BinaryNumber.__lt__")

    # --- Problem 4: BinaryNumber.__lshift__, __rshift__, int_to_binary ---
    # doctest.run_docstring_examples(BinaryNumber.__lshift__, globs=None, name="BinaryNumber.__lshift__")
    # doctest.run_docstring_examples(BinaryNumber.__rshift__, globs=None, name="BinaryNumber.__rshift__")
    # doctest.run_docstring_examples(int_to_binary, globs=None, name="int_to_binary")

    # --- Problem 5: log_base_2 ---
    # doctest.run_docstring_examples(log_base_2, globs=None, name="log_base_2")

    # --- Problem 6: Queue.enqueue ---
    # doctest.run_docstring_examples(Queue.enqueue, globs=None, name="Queue.enqueue")

    # --- Problem 7: Queue.dequeue ---
    # doctest.run_docstring_examples(Queue.dequeue, globs=None, name="Queue.dequeue")

    # --- Problem 8: Queue.peek ---
    # doctest.run_docstring_examples(Queue.peek, globs=None, name="Queue.peek")

    # --- Problem 9: add_binary ---
    # doctest.run_docstring_examples(add_binary, globs=None, name="add_binary")

    # --- Problem 10: dict_depth ---
    # doctest.run_docstring_examples(dict_depth, globs=None, name="dict_depth")