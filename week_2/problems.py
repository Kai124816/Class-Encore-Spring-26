import doctest

# ============================================================
# WEEK 2 PROBLEMS — Chapter 1: Objects, Classes, and Methods
# ============================================================

# Problem 1
class Point:
    """
    Represents a point in 2D space with x and y coordinates.

    >>> p = Point(3, 4) # doctest: +SKIP
    >>> p.x # doctest: +SKIP
    3 
    >>> p.y # doctest: +SKIP
    4
    >>> print(p) # doctest: +SKIP
    Point(3, 4)
    >>> p2 = Point(0, 0) # doctest: +SKIP
    >>> print(p2) # doctest: +SKIP
    Point(0, 0)
    """
    def __init__(self, x: float, y: float):
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        # Should return a string like "Point(3, 4)"
        pass


# Problem 2
class Point:
    """
    Extends Problem 1's Point with a distance_to method.

    >>> p1 = Point(0, 0) # doctest: +SKIP
    >>> p2 = Point(3, 4) # doctest: +SKIP
    >>> p1.distance_to(p2) # doctest: +SKIP
    5.0
    >>> p2.distance_to(p1) # doctest: +SKIP
    5.0
    >>> p1.distance_to(p1) # doctest: +SKIP
    0.0
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other: "Point") -> float:
        """Returns the Euclidean distance between self and other."""
        # YOUR CODE HERE
        # Hint: you may use ** for exponentiation and import math for math.sqrt,
        # or use ** 0.5
        pass


# Problem 3
class Rectangle:
    """
    Represents an axis-aligned rectangle by its top-left corner Point
    and its width and height.

    >>> r = Rectangle(Point(1, 2), 5, 3) # doctest: +SKIP
    >>> r.width # doctest: +SKIP
    5
    >>> r.height # doctest: +SKIP
    3
    >>> r.area() # doctest: +SKIP
    15
    >>> r.perimeter() # doctest: +SKIP
    16
    >>> print(r) # doctest: +SKIP
    Rectangle(Point(1, 2), width=5, height=3)
    """
    def __init__(self, corner: "Point", width: float, height: float):
        # YOUR CODE HERE
        pass

    def area(self) -> float:
        """Returns the area of the rectangle."""
        # YOUR CODE HERE
        pass

    def perimeter(self) -> float:
        """Returns the perimeter of the rectangle."""
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        # Should return e.g. "Rectangle(Point(1, 2), width=5, height=3)"
        pass


# Problem 4
class BankAccount:
    """
    Represents a simple bank account with a balance.
    Deposits must be positive. Withdrawals must be positive and
    cannot exceed the current balance (do nothing if they would).

    >>> acct = BankAccount("Alice", 100) # doctest: +SKIP
    >>> acct.owner # doctest: +SKIP
    'Alice'
    >>> acct.balance # doctest: +SKIP
    100
    >>> acct.deposit(50) # doctest: +SKIP
    >>> acct.balance # doctest: +SKIP
    150
    >>> acct.withdraw(30) # doctest: +SKIP
    >>> acct.balance # doctest: +SKIP
    120
    >>> acct.withdraw(200) # doctest: +SKIP
    # should do nothing — insufficient funds
    >>> acct.balance # doctest: +SKIP
    120
    >>> print(acct)  # doctest: +SKIP
    BankAccount(owner=Alice, balance=120)
    """
    def __init__(self, owner: str, balance: float = 0):
        # YOUR CODE HERE
        pass

    def deposit(self, amount: float) -> None:
        """Add amount to balance. Does nothing if amount <= 0."""
        # YOUR CODE HERE
        pass

    def withdraw(self, amount: float) -> None:
        """Subtract amount from balance if possible. Does nothing if
        amount <= 0 or amount > balance."""
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        # Should return e.g. "BankAccount(owner=Alice, balance=120)"
        pass


# Problem 5
class Student:
    """
    Represents a student with a name and a list of grades.
    Grades are added one at a time. The average is the mean
    of all grades added so far; return 0.0 if no grades have been added.

    >>> s = Student("Bo")  # doctest: +SKIP
    >>> s.name  # doctest: +SKIP
    'Bo'
    >>> s.average()  # doctest: +SKIP
    0.0
    >>> s.add_grade(90)  # doctest: +SKIP
    >>> s.add_grade(80)  # doctest: +SKIP
    >>> s.add_grade(100)  # doctest: +SKIP
    >>> s.average()  # doctest: +SKIP
    90.0
    >>> print(s)  # doctest: +SKIP
    Student(Bo, grades=[90, 80, 100])
    """
    def __init__(self, name: str):
        # YOUR CODE HERE
        pass

    def add_grade(self, grade: float) -> None:
        """Appends grade to this student's list of grades."""
        # YOUR CODE HERE
        pass

    def average(self) -> float:
        """Returns the mean of all grades, or 0.0 if none."""
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        # Should return e.g. "Student(Bo, grades=[90, 80, 100])"
        pass


# Problem 6
class Counter:
    """
    A simple counter that starts at a given value and can be
    incremented, decremented, or reset.

    >>> c = Counter()  # doctest: +SKIP
    >>> c.count  # doctest: +SKIP
    0
    >>> c.increment()  # doctest: +SKIP
    >>> c.increment()  # doctest: +SKIP
    >>> c.count  # doctest: +SKIP
    2 
    >>> c.decrement()  # doctest: +SKIP
    >>> c.count  # doctest: +SKIP
    1 
    >>> c.reset()  # doctest: +SKIP
    >>> c.count  # doctest: +SKIP
    0
    >>> c2 = Counter(10)  # doctest: +SKIP
    >>> c2.count  # doctest: +SKIP
    10
    >>> c2.reset()  # doctest: +SKIP
    >>> c2.count  # doctest: +SKIP
    0
    """
    def __init__(self, start: int = 0):
        # YOUR CODE HERE
        pass

    def increment(self) -> None:
        """Adds 1 to the count."""
        # YOUR CODE HERE
        pass

    def decrement(self) -> None:
        """Subtracts 1 from the count."""
        # YOUR CODE HERE
        pass

    def reset(self) -> None:
        """Resets count to 0."""
        # YOUR CODE HERE
        pass


# Problem 7
class Circle:
    """
    Represents a circle defined by a center Point and a radius.
    Provides area, circumference, and a method to check whether
    a given Point lies inside the circle (strictly, not on the edge).

    >>> import math 
    >>> center = Point(0, 0)  # doctest: +SKIP
    >>> c = Circle(center, 5)  # doctest: +SKIP
    >>> c.radius  # doctest: +SKIP
    5
    >>> round(c.area(), 4)  # doctest: +SKIP
    78.5398
    >>> round(c.circumference(), 4)  # doctest: +SKIP
    31.4159
    >>> c.contains(Point(3, 4))  # doctest: +SKIP
    # exactly on the edge → not inside
    False
    >>> c.contains(Point(0, 0))  # doctest: +SKIP  
    # center is inside
    True
    >>> c.contains(Point(6, 0))  # doctest: +SKIP 
    # outside
    False
    """
    def __init__(self, center: "Point", radius: float):
        # YOUR CODE HERE
        pass

    def area(self) -> float:
        """Returns π * r²."""
        # YOUR CODE HERE
        # Hint: import math and use math.pi
        pass

    def circumference(self) -> float:
        """Returns 2 * π * r."""
        # YOUR CODE HERE
        pass

    def contains(self, p: "Point") -> bool:
        """Returns True if p is strictly inside this circle."""
        # YOUR CODE HERE
        # Hint: use the center's distance_to method
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        # Should return e.g. "Circle(center=Point(0, 0), radius=5)"
        pass


# Problem 8
class Fraction:
    """
    Represents a fraction (numerator / denominator) and supports
    addition with another Fraction. The result should be stored in
    lowest terms (use the provided gcd helper).
    Assume denominator is always a positive integer.

    >>> a = Fraction(1, 2) # doctest: +SKIP
    >>> a.numerator  # doctest: +SKIP
    1
    >>> a.denominator  # doctest: +SKIP
    2
    >>> print(a)  # doctest: +SKIP
    1/2
    >>> b = Fraction(1, 3)  # doctest: +SKIP
    >>> c = a.add(b)  # doctest: +SKIP
    >>> print(c)  # doctest: +SKIP
    5/6
    >>> d = Fraction(2, 4) # doctest: +SKIP
    >>> print(d) # doctest: +SKIP     
    # stored in lowest terms
    1/2
    >>> e = Fraction(3, 6).add(Fraction(1, 6)) # doctest: +SKIP
    >>> print(e) # doctest: +SKIP
    2/3
    """
    def _gcd(self, a: int, b: int) -> int:
        """Returns the greatest common divisor of a and b."""
        while b:
            a, b = b, a % b
        return a

    def __init__(self, numerator: int, denominator: int):
        # YOUR CODE HERE
        # Reduce to lowest terms using self._gcd before storing
        pass

    def add(self, other: "Fraction") -> "Fraction":
        """Returns a new Fraction equal to self + other, in lowest terms."""
        # YOUR CODE HERE
        # Recall: a/b + c/d = (a*d + b*c) / (b*d)
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        # Should return e.g. "1/2"
        pass


# ============================================================
# Run doctests when this file is executed directly
# ============================================================
if __name__ == "__main__":
    import doctest
    doctest.testmod()