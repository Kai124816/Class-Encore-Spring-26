from __future__ import annotations
import doctest
from typing import Optional


# ============================================================
# BINARY NUMBER BASE CLASS
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
# Additional attributes:
#   - num_bits  : the number of bits used to represent this number
#   - range     : a tuple (min_val, max_val) of integers this
#                 representation can hold. For an UNSIGNED n-bit
#                 number, range = (0, 2**n - 1).
#
# Supported operations (already implemented for you — do NOT modify):
#   - to_int        : convert to a Python int
#   - __gt__        : greater-than comparison (without using to_int)
#   - __lt__        : less-than comparison    (without using to_int)
#   - __lshift__    : left shift  (multiply by 2^n)
#   - __rshift__    : right shift (integer divide by 2^n)

class BinaryNumber:
    """An unsigned binary number stored as a list of booleans (MSB first).

    Attributes:
        bits     (list[bool])  : the binary digits, MSB first
        num_bits (int)         : number of bits
        range    (tuple[int,int]) : (min representable, max representable)

    >>> BinaryNumber([True, False, True]).bits
    [True, False, True]
    >>> BinaryNumber([True, False, True]).num_bits
    3
    >>> BinaryNumber([True, False, True]).range
    (0, 7)
    >>> BinaryNumber([True, False, True])
    BinaryNumber(101)
    """

    def __init__(self, bits: list[bool]):
        self.bits = bits
        self.num_bits = len(bits)
        self.range = (0, 2 ** self.num_bits - 1)

    def __repr__(self):
        digits = "".join("1" if b else "0" for b in self.bits)
        return f"BinaryNumber({digits})"

    def __eq__(self, other):
        if not isinstance(other, BinaryNumber):
            return NotImplemented
        return self.to_int() == other.to_int()

    def to_int(self) -> int:
        """Converts this BinaryNumber to its non-negative integer value.

        The MSB is at index 0. Bit at position i from the right contributes
        bit * 2**i to the total.

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
        total = 0
        for bit in self.bits:
            total = total * 2 + (1 if bit else 0)
        return total

    def __gt__(self, other: BinaryNumber) -> bool:
        """Returns True if this BinaryNumber is strictly greater than other.

        Compares bit-by-bit from left to right WITHOUT using to_int().

        >>> BinaryNumber([True, False, True]) > BinaryNumber([True, True])
        True
        >>> BinaryNumber([True, True]) > BinaryNumber([True, False, True])
        False
        >>> BinaryNumber([True, True]) > BinaryNumber([True, True])
        False
        """
        # Pad the shorter number on the left with False bits so lengths match.
        n = max(len(self.bits), len(other.bits))
        a = [False] * (n - len(self.bits)) + self.bits
        b = [False] * (n - len(other.bits)) + other.bits
        for x, y in zip(a, b):
            if x != y:
                return x and not y   # True > False means self is larger here
        return False  # equal

    def __lt__(self, other: BinaryNumber) -> bool:
        """Returns True if this BinaryNumber is strictly less than other.

        Compares bit-by-bit from left to right WITHOUT using to_int().

        >>> BinaryNumber([True, False, True]) < BinaryNumber([True, True])
        False
        >>> BinaryNumber([True, True]) < BinaryNumber([True, False, True])
        True
        >>> BinaryNumber([True, True]) < BinaryNumber([True, True])
        False
        """
        n = max(len(self.bits), len(other.bits))
        a = [False] * (n - len(self.bits)) + self.bits
        b = [False] * (n - len(other.bits)) + other.bits
        for x, y in zip(a, b):
            if x != y:
                return not x and y
        return False

    def __lshift__(self, n: int) -> BinaryNumber:
        """Returns a new BinaryNumber shifted LEFT by n positions.

        Left-shifting by 1 appends a False (0) to the right (multiply by 2).

        >>> BinaryNumber([True, False, True]) << 1
        BinaryNumber(1010)
        >>> BinaryNumber([True, False, True]) << 2
        BinaryNumber(10100)
        >>> BinaryNumber([True]) << 3
        BinaryNumber(1000)
        """
        return BinaryNumber(self.bits + [False] * n)

    def __rshift__(self, n: int) -> BinaryNumber:
        """Returns a new BinaryNumber shifted RIGHT by n positions.

        Right-shifting by 1 removes the last bit (integer divide by 2).
        If all bits are shifted away, return BinaryNumber([False]) (i.e. 0).

        >>> BinaryNumber([True, False, True]) >> 1
        BinaryNumber(10)
        >>> BinaryNumber([True, False, True]) >> 2
        BinaryNumber(1)
        >>> BinaryNumber([True, False, True]) >> 3
        BinaryNumber(0)
        """
        remaining = self.bits[:-n] if n < len(self.bits) else []
        return BinaryNumber(remaining) if remaining else BinaryNumber([False])


# ============================================================
# SIGNED BINARY NUMBER CLASS — Problems 1–5
# ============================================================
#
# Signed binary numbers use TWO'S COMPLEMENT representation.
# In an n-bit two's complement number:
#   - The MSB (leftmost bit) is the SIGN BIT.
#       0 → positive (or zero)
#       1 → negative
#   - The value of a negative number is computed as:
#       -(2^(n-1)) + (value of the remaining n-1 bits)
#
# Examples with 4 bits:
#   0101 →  5   (sign bit 0; remaining 101 = 5)
#   1011 → -5   (sign bit 1; -(2^3) + 011 = -8 + 3 = -5)
#   1000 → -8   (most negative 4-bit value)
#   0111 →  7   (most positive 4-bit value)
#
# For an n-bit signed number:
#   range = (-2^(n-1), 2^(n-1) - 1)
#
# SignedBinaryNumber INHERITS from BinaryNumber.
# You must override the constructor, to_int, __gt__, __lt__,
# __lshift__, and __rshift__ to account for the sign bit and
# two's complement semantics.

class SignedBinaryNumber(BinaryNumber):
    """A signed two's complement binary number (MSB is the sign bit).

    Attributes:
        bits     (list[bool])     : the binary digits, MSB (sign bit) first
        num_bits (int)            : number of bits
        range    (tuple[int,int]) : (-(2^(n-1)), 2^(n-1) - 1)

    >>> SignedBinaryNumber([False, True, False, True]).bits
    [False, True, False, True]
    >>> SignedBinaryNumber([False, True, False, True]).num_bits
    4
    >>> SignedBinaryNumber([False, True, False, True]).range
    (-8, 7)
    >>> SignedBinaryNumber([False, True, False, True])
    SignedBinaryNumber(0101)
    """

    # ------------------------------------------------------------------
    # Problem 1 — Constructor
    # ------------------------------------------------------------------
    def __init__(self, bits: list[bool]):
        """Initialises a SignedBinaryNumber.

        Sets:
            self.bits     — the list of boolean bits (MSB/sign bit first)
            self.num_bits — number of bits (length of bits)
            self.range    — tuple (min_val, max_val) for an n-bit signed number
                            min_val = -(2 ** (n - 1))
                            max_val =   2 ** (n - 1) - 1

        Parameters:
            bits (list[bool]): At least one bit; the first is the sign bit.

        >>> SignedBinaryNumber([False, True, False, True]).num_bits
        4
        >>> SignedBinaryNumber([False, True, False, True]).range
        (-8, 7)
        >>> SignedBinaryNumber([True, False, False, False]).range
        (-8, 7)
        >>> SignedBinaryNumber([True]).range
        (-1, 0)
        """
        super().__init__(bits)
        min_val = -(2 ** (self.num_bits - 1))
        max_val = (2 ** (self.num_bits - 1)) - 1
        self.range = (min_val, max_val)

    def __repr__(self):
        digits = "".join("1" if b else "0" for b in self.bits)
        return f"SignedBinaryNumber({digits})"

    def __eq__(self, other):
        if not isinstance(other, SignedBinaryNumber):
            return NotImplemented
        return self.to_int() == other.to_int()

    # ------------------------------------------------------------------
    # Problem 2 — to_int (two's complement)
    # ------------------------------------------------------------------
    def to_int(self) -> int:
        """Converts this SignedBinaryNumber to its signed integer value
        using two's complement.

        If the sign bit (self.bits[0]) is False, the value is non-negative
        and equals the unsigned value of the remaining bits.

        If the sign bit is True, the value is:
            -(2 ** (n - 1)) + (unsigned value of the remaining n-1 bits)

        Returns:
            int: The signed integer value.

        >>> SignedBinaryNumber([False, True, False, True]).to_int()
        5
        >>> SignedBinaryNumber([True, False, True, True]).to_int()
        -5
        >>> SignedBinaryNumber([True, False, False, False]).to_int()
        -8
        >>> SignedBinaryNumber([False, True, True, True]).to_int()
        7
        >>> SignedBinaryNumber([False]).to_int()
        0
        >>> SignedBinaryNumber([True]).to_int()
        -1
        """
        acc = 0
        signed_val = self.range[0] * self.bits[0]
        bit_val = 1

        for i in range(0, self.num_bits - 1):
            reversed_idx = (i * -1) - 1
            if self.bits[reversed_idx]:
                acc += bit_val
            bit_val *= 2

        return signed_val + acc


    # ------------------------------------------------------------------
    # Problem 3 — __gt__ (without using to_int)
    # ------------------------------------------------------------------
    def __gt__(self, other: SignedBinaryNumber) -> bool:
        """Returns True if this SignedBinaryNumber is strictly greater than other.

        Rules (do NOT call to_int):
          1. A non-negative number (sign bit = 0) is always greater than a
             negative number (sign bit = 1).
          2. If both are non-negative, compare the remaining bits left-to-right;
             the first differing bit determines which is larger (True > False).
          3. If both are negative, compare the remaining bits left-to-right;
             the first differing bit determines which is larger (True > False
             means the magnitude is bigger, so the value is MORE NEGATIVE,
             i.e. SMALLER). Therefore for two negatives: False > True bit-wise.

        Hint: After handling the sign-bit cases, you can reuse the same
              bit-by-bit comparison logic from BinaryNumber.__gt__, but
              invert the result for the both-negative case.

        >>> SignedBinaryNumber([False, True, False, True]) > SignedBinaryNumber([True, False, True, True])
        True
        >>> SignedBinaryNumber([True, False, True, True]) > SignedBinaryNumber([False, True, False, True])
        False
        >>> SignedBinaryNumber([False, True, True, True]) > SignedBinaryNumber([False, True, False, True])
        True
        >>> SignedBinaryNumber([True, True, True, True]) > SignedBinaryNumber([True, False, True, True])
        True
        >>> SignedBinaryNumber([False, True, False, True]) > SignedBinaryNumber([False, True, False, True])
        False
        """
        if self.bits[0] != other.bits[0]:
            return self.bits[0] == False
        
        for i in range(1, self.num_bits):
            if self.bits[i] != other.bits[i]:
                return self.bits[i] == True
        
        return False
        
    # ------------------------------------------------------------------
    # Problem 4 — __lt__ (without using to_int)
    # ------------------------------------------------------------------
    def __lt__(self, other: SignedBinaryNumber) -> bool:
        """Returns True if this SignedBinaryNumber is strictly less than other.

        Mirror of __gt__: self < other is equivalent to other > self.

        >>> SignedBinaryNumber([False, True, False, True]) < SignedBinaryNumber([True, False, True, True])
        False
        >>> SignedBinaryNumber([True, False, True, True]) < SignedBinaryNumber([False, True, False, True])
        True
        >>> SignedBinaryNumber([False, True, False, False]) < SignedBinaryNumber([False, True, False, True])
        True
        >>> SignedBinaryNumber([False, True, False, True]) < SignedBinaryNumber([False, True, False, True])
        False
        """
        if self.bits[0] != other.bits[0]:
            return self.bits[0] == True
        
        for i in range(1, len(self.bits)):
            if self.bits[i] != other.bits[i]:
                return self.bits[0] == False
        
        return False

    # ------------------------------------------------------------------
    # Problem 5 — __lshift__ and __rshift__
    # ------------------------------------------------------------------
    def __lshift__(self, n: int) -> SignedBinaryNumber:
        """Returns a new SignedBinaryNumber shifted LEFT by n positions.

        The sign bit is preserved: the first bit of self.bits stays as
        the sign bit of the result. The n least-significant bits become 0
        (False), and the n bits just below the sign bit are discarded.

        In other words:
          result bits = [sign_bit] + self.bits[1:-n] + [False] * n
        If n >= num_bits - 1, all magnitude bits are discarded and the
        result is [sign_bit] + [False] * (num_bits - 1).

        Parameters:
            n (int): Number of positions to shift left (non-negative).

        Returns:
            SignedBinaryNumber: A new object of the same bit-width.

        >>> SignedBinaryNumber([False, True, False, True]) << 1
        SignedBinaryNumber(0010)
        >>> SignedBinaryNumber([False, True, False, True]) << 2
        SignedBinaryNumber(0100)
        >>> SignedBinaryNumber([True, False, True, True]) << 1
        SignedBinaryNumber(1110)
        >>> SignedBinaryNumber([False, True, False, True]) << 3
        SignedBinaryNumber(0000)
        """
        signed_bit = [self.bits[0]]
        non_signed_bits = self.bits[1:]

        for i in range(n):
            non_signed_bits.pop(0)

        for i in range(n):
            non_signed_bits.append(False)
        
        return SignedBinaryNumber(signed_bit + non_signed_bits)
        

    def __rshift__(self, n: int) -> SignedBinaryNumber:
        """Returns a new SignedBinaryNumber shifted RIGHT by n positions
        (arithmetic right shift — the sign bit is copied into the vacated
        positions on the left).

        result bits = [sign_bit] * (n + 1) + self.bits[1:num_bits - n]
        If n >= num_bits - 1, all magnitude bits are gone and the result is
        [sign_bit] * num_bits.

        Parameters:
            n (int): Number of positions to shift right (non-negative).

        Returns:
            SignedBinaryNumber: A new object of the same bit-width.

        >>> SignedBinaryNumber([False, True, False, True]) >> 1
        SignedBinaryNumber(0010)
        >>> SignedBinaryNumber([True, False, True, True]) >> 1
        SignedBinaryNumber(1101)
        >>> SignedBinaryNumber([True, False, True, True]) >> 3
        SignedBinaryNumber(1111)
        >>> SignedBinaryNumber([False, True, True, True]) >> 2
        SignedBinaryNumber(0001)
        """
        signed_bit = self.bits[0]
        new_bits = [signed_bit] * (n + 1)

        for i in range(1, self.num_bits - n):
            new_bits.append(self.bits[i])
        
        return SignedBinaryNumber(new_bits)


# ============================================================
# STANDALONE FUNCTIONS — Problems 6–10
# ============================================================

# ------------------------------------------------------------------
# Problem 6 — Bitwise AND (returns int)
# ------------------------------------------------------------------
def binary_and(a: BinaryNumber, b: BinaryNumber) -> int:
    """Performs a bitwise AND on two BinaryNumber objects and returns the
    result as a Python int.

    Bitwise AND: a bit in the result is True (1) only if the corresponding
    bit is True in BOTH a and b.

    If the two numbers have different lengths, pad the shorter one on the
    LEFT with False bits before performing the AND.

    You may NOT use Python's built-in & operator or convert to int first.
    Compute the AND bit-by-bit.

    Parameters:
        a (BinaryNumber): The first operand.
        b (BinaryNumber): The second operand.

    Returns:
        int: The integer value of (a AND b).

    >>> binary_and(BinaryNumber([True, False, True]), BinaryNumber([True, True, False]))
    4
    >>> binary_and(BinaryNumber([True, False, True]), BinaryNumber([False, True, False]))
    0
    >>> binary_and(BinaryNumber([False]), BinaryNumber([False]))
    0
    >>> binary_and(BinaryNumber([True, True]), BinaryNumber([False, False, True, True]))
    3
    >>> binary_and(BinaryNumber([True, False, True]), BinaryNumber([True, True]))
    1
    """
    max_bits = max(a.num_bits, b.num_bits)
    
    a_bits = [False for _ in range(max_bits - a.num_bits)] + a.bits
    b_bits = [False for _ in range(max_bits - b.num_bits)] + b.bits

    acc = 0
    bit_val = 1

    for i in range(max_bits):
        reversed_idx = (i * -1) - 1
        if a_bits[reversed_idx] and b_bits[reversed_idx]:
            acc += bit_val
        bit_val *= 2

    return acc

# ------------------------------------------------------------------
# Problem 7 — Bitwise OR (returns int)
# ------------------------------------------------------------------
def binary_or(a: BinaryNumber, b: BinaryNumber) -> int:
    """Performs a bitwise OR on two BinaryNumber objects and returns the
    result as a Python int.

    Bitwise OR: a bit in the result is True (1) if the corresponding bit
    is True in EITHER a or b (or both).

    If the two numbers have different lengths, pad the shorter one on the
    LEFT with False bits before performing the OR.

    You may NOT use Python's built-in | operator or convert to int first.
    Compute the OR bit-by-bit.

    Parameters:
        a (BinaryNumber): The first operand.
        b (BinaryNumber): The second operand.

    Returns:
        int: The integer value of (a OR b).

    >>> binary_or(BinaryNumber([True, False, True]), BinaryNumber([False, True, False]))
    7
    >>> binary_or(BinaryNumber([True, False, False]), BinaryNumber([False, False, True]))
    5
    >>> binary_or(BinaryNumber([False]), BinaryNumber([False]))
    0
    >>> binary_or(BinaryNumber([True, True]), BinaryNumber([False, False, False, False]))
    3
    >>> binary_or(BinaryNumber([True, False, True]), BinaryNumber([True, True]))
    7
    """
    max_bits = max(a.num_bits, b.num_bits)
    
    a_bits = [False for _ in range(max_bits - a.num_bits)] + a.bits
    b_bits = [False for _ in range(max_bits - b.num_bits)] + b.bits

    acc = 0
    bit_val = 1

    for i in range(max_bits):
        reversed_idx = (i * -1) - 1
        if a_bits[reversed_idx] or b_bits[reversed_idx]:
            acc += bit_val
        bit_val *= 2

    return acc


# ------------------------------------------------------------------
# Problem 8 — exists_in_nested_list
# ------------------------------------------------------------------
def exists_in_nested_list(lst, target) -> bool:
    """Returns True if target exists anywhere in a (possibly nested) list.

    The input may contain individual elements or other lists (which may
    themselves be nested to any depth).

    Parameters:
        lst    : A possibly nested list of elements.
        target : The value to search for.

    Returns:
        bool: True if target is found anywhere in lst, False otherwise.

    >>> exists_in_nested_list([], 1)
    False
    >>> exists_in_nested_list([1, 2, 3], 2)
    True
    >>> exists_in_nested_list([1, 2, 3], 5)
    False
    >>> exists_in_nested_list([1, [2, [3, [4]]]], 4)
    True
    >>> exists_in_nested_list([1, [2, [3, [4]]]], 5)
    False
    >>> exists_in_nested_list([[["hello"], "world"]], "hello")
    True
    >>> exists_in_nested_list([[1, 2], [3, [4, 5]]], 5)
    True
    """
    for el in lst:
        if isinstance(el, list):
            if exists_in_nested_list(el, target):
                return True
        elif el == target:
            return True
    
    return False


# ------------------------------------------------------------------
# Problem 9 — nested_list_sum
# ------------------------------------------------------------------
def nested_list_sum(lst) -> int:
    """Returns the sum of all integers found anywhere in a nested list.

    The input may contain integers or other (possibly nested) lists of
    integers.  Non-integer, non-list elements should be ignored.

    Parameters:
        lst: A possibly nested list of integers and lists.

    Returns:
        int: The sum of all integers in lst at any depth.

    >>> nested_list_sum([])
    0
    >>> nested_list_sum([1, 2, 3])
    6
    >>> nested_list_sum([1, [2, 3], 4])
    10
    >>> nested_list_sum([[1, [2]], [3, [4, [5]]]])
    15
    >>> nested_list_sum([1, "skip", [2, None, [3]]])
    6
    """
    acc = 0

    for el in lst:
        if isinstance(el, list):
            acc += nested_list_sum(el)
        elif isinstance(el, int):
            acc += el

    return acc


# ------------------------------------------------------------------
# Problem 10 — nested_dict_keys
# ------------------------------------------------------------------
def nested_dict_keys(d: dict) -> list:
    """Returns a flat list of ALL keys found at any depth of a nested
    dictionary (a dictionary whose values may themselves be dictionaries).

    Keys are returned in the order they are encountered (top-level first,
    then depth-first into nested dictionaries).

    Non-dict values are ignored — only dictionary keys are collected.

    Parameters:
        d (dict): A (possibly nested) dictionary.

    Returns:
        list: All keys at every level of nesting, in encounter order.

    >>> nested_dict_keys({})
    []
    >>> nested_dict_keys({"a": 1, "b": 2})
    ['a', 'b']
    >>> nested_dict_keys({"a": {"b": {"c": 3}}})
    ['a', 'b', 'c']
    >>> nested_dict_keys({"x": 1, "y": {"z": 2, "w": {"v": 3}}, "u": 4})
    ['x', 'y', 'z', 'w', 'v', 'u']
    >>> nested_dict_keys({"a": 1, "b": {"c": 2}, "d": {"e": {"f": 3}}})
    ['a', 'b', 'c', 'd', 'e', 'f']
    """
    keys = []

    for key in d.keys():
        val = d[key]
        keys.append(key)
        if isinstance(val, dict):
            keys += nested_dict_keys(val)
    
    return keys


# ============================================================
# To test a single problem, uncomment that problem's line below.
# ============================================================
if __name__ == "__main__":
    import doctest

    # --- BinaryNumber base class ---
    doctest.run_docstring_examples(BinaryNumber, globs=None, name="BinaryNumber")
    doctest.run_docstring_examples(BinaryNumber.to_int, globs=None, name="BinaryNumber.to_int")

    # --- Problem 1: SignedBinaryNumber.__init__ ---
    doctest.run_docstring_examples(SignedBinaryNumber.__init__, globs=None, name="SignedBinaryNumber.__init__")

    # --- Problem 2: SignedBinaryNumber.to_int ---
    doctest.run_docstring_examples(SignedBinaryNumber.to_int, globs=None, name="SignedBinaryNumber.to_int")

    # --- Problem 3: SignedBinaryNumber.__gt__ ---
    doctest.run_docstring_examples(SignedBinaryNumber.__gt__, globs=None, name="SignedBinaryNumber.__gt__")

    # --- Problem 4: SignedBinaryNumber.__lt__ ---
    doctest.run_docstring_examples(SignedBinaryNumber.__lt__, globs=None, name="SignedBinaryNumber.__lt__")

    # --- Problem 5: SignedBinaryNumber.__lshift__ / __rshift__ ---
    doctest.run_docstring_examples(SignedBinaryNumber.__lshift__, globs=None, name="SignedBinaryNumber.__lshift__")
    doctest.run_docstring_examples(SignedBinaryNumber.__rshift__, globs=None, name="SignedBinaryNumber.__rshift__")

    # --- Problem 6: binary_and ---
    doctest.run_docstring_examples(binary_and, globs=None, name="binary_and")

    # --- Problem 7: binary_or ---
    doctest.run_docstring_examples(binary_or, globs=None, name="binary_or")

    # --- Problem 8: exists_in_nested_list ---
    doctest.run_docstring_examples(exists_in_nested_list, globs=None, name="exists_in_nested_list")

    # --- Problem 9: nested_list_sum ---
    doctest.run_docstring_examples(nested_list_sum, globs=None, name="nested_list_sum")

    # --- Problem 10: nested_dict_keys ---
    doctest.run_docstring_examples(nested_dict_keys, globs=None, name="nested_dict_keys")