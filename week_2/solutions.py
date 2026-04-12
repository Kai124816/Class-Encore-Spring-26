import doctest
import math

# ============================================================
# WEEK 2 PROBLEMS — Chapter 1: Objects, Classes, and Methods
# ============================================================

# Problem 1
class Point:
    """
    Represents a point in 2D space with x and y coordinates.

    >>> p = Point(3, 4)
    >>> p.x
    3
    >>> p.y
    4
    >>> print(p)
    Point(3, 4)
    >>> p2 = Point(0, 0)
    >>> print(p2)
    Point(0, 0)
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


# Problem 2
class Point:
    """
    Extends Problem 1's Point with a distance_to method.

    >>> p1 = Point(0, 0)
    >>> p2 = Point(3, 4)
    >>> p1.distance_to(p2)
    5.0
    >>> p2.distance_to(p1)
    5.0
    >>> p1.distance_to(p1)
    0.0
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other: "Point") -> float:
        """Returns the Euclidean distance between self and other."""
        a = (other.x - self.x)
        a_squared = a * a

        b = (other.y - self.y)
        b_squared = b * b

        c_squared = a_squared + b_squared
        return c_squared ** 0.5

        
# Problem 3
class Rectangle:
    """
    Represents an axis-aligned rectangle by its top-left corner Point
    and its width and height.

    >>> r = Rectangle(Point(1, 2), 5, 3)
    >>> r.width
    5
    >>> r.height
    3
    >>> r.area()
    15
    >>> r.perimeter()
    16
    >>> print(r)
    Rectangle(Point(1, 2), width=5, height=3)
    """
    def __init__(self, corner: "Point", width: float, height: float):
        self.corner = Point(corner.x, corner.y)
        self.width = width
        self.height = height

    def area(self) -> float:
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Returns the perimeter of the rectangle."""
        return (2 * self.height) + (2 * self.width)

    def __str__(self) -> str:
        return f"Rectangle({str(self.corner)}, width={self.width}, height={self.height})"


# Problem 4
class BankAccount:
    """
    Represents a simple bank account with a balance.
    Deposits must be positive. Withdrawals must be positive and
    cannot exceed the current balance (do nothing if they would).

    >>> acct = BankAccount("Alice", 100)
    >>> acct.owner
    'Alice'
    >>> acct.balance
    100
    >>> acct.deposit(50)
    >>> acct.balance
    150
    >>> acct.withdraw(30)
    >>> acct.balance
    120
    >>> acct.withdraw(200)  # should do nothing — insufficient funds
    >>> acct.balance
    120
    >>> print(acct)
    BankAccount(owner=Alice, balance=120)
    """
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add amount to balance. Does nothing if amount <= 0."""
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Subtract amount from balance if possible. Does nothing if
        amount <= 0 or amount > balance."""
        if amount <= self.balance:
            self.balance -= amount


    def __str__(self) -> str:
        return f"BankAccount(owner={self.owner}, balance={self.balance})"


# Problem 5
class Student:
    """
    Represents a student with a name and a list of grades.
    Grades are added one at a time. The average is the mean
    of all grades added so far; return 0.0 if no grades have been added.

    >>> s = Student("Bo")
    >>> s.name
    'Bo'
    >>> s.average()
    0.0
    >>> s.add_grade(90)
    >>> s.add_grade(80)
    >>> s.add_grade(100)
    >>> s.average()
    90.0
    >>> print(s)
    Student(Bo, grades=[90, 80, 100])
    """
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add_grade(self, grade: float) -> None:
        """Appends grade to this student's list of grades."""
        self.grades.append(grade)

    def average(self) -> float:
        """Returns the mean of all grades, or 0.0 if none."""
        if len(self.grades) == 0:
            return 0.0
        
        total_sum = 0.0
        for grade in self.grades:
            total_sum += grade

        return total_sum / len(self.grades)
            
    def __str__(self) -> str:
        return f"Student({self.name}, grades={str(self.grades)})"
        


# Problem 6
class Counter:
    """
    A simple counter that starts at a given value and can be
    incremented, decremented, or reset.

    >>> c = Counter()
    >>> c.count
    0
    >>> c.increment()
    >>> c.increment()
    >>> c.count
    2
    >>> c.decrement()
    >>> c.count
    1
    >>> c.reset()
    >>> c.count
    0
    >>> c2 = Counter(10)
    >>> c2.count
    10
    >>> c2.reset()
    >>> c2.count
    0
    """
    def __init__(self, start: int = 0):
        self.count = start

    def increment(self) -> None:
        """Adds 1 to the count."""
        self.count += 1

    def decrement(self) -> None:
        """Subtracts 1 from the count."""
        self.count -= 1

    def reset(self) -> None:
        """Resets count to 0."""
        self.count = 0


# Problem 7
class Circle:
    """
    Represents a circle defined by a center Point and a radius.
    Provides area, circumference, and a method to check whether
    a given Point lies inside the circle (strictly, not on the edge).

    >>> import math
    >>> center = Point(0, 0)
    >>> c = Circle(center, 5)
    >>> c.radius
    5
    >>> round(c.area(), 4)
    78.5398
    >>> round(c.circumference(), 4)
    31.4159
    >>> c.contains(Point(3, 4))   # exactly on the edge → not inside
    False
    >>> c.contains(Point(0, 0))   # center is inside
    True
    >>> c.contains(Point(6, 0))   # outside
    False
    """
    def __init__(self, center: "Point", radius: float):
        self.center = Point(center.x, center.y)
        self.radius = radius

    def area(self) -> float:
        """Returns π * r²."""
        return math.pi * (self.radius**2)

    def circumference(self) -> float:
        """Returns 2 * π * r."""
        return 2 * math.pi * self.radius
        
    def contains(self, p: "Point") -> bool:
        """Returns True if p is strictly inside this circle."""
        return self.center.distance_to(p) < self.radius

    def __str__(self) -> str:
        # YOUR CODE HERE
        # Should return e.g. "Circle(center=Point(0, 0), radius=5)"
        f"Circle(center={str(self.center)}, radius={self.radius}"
        

# Problem 8
class Fraction:
    """
    Represents a fraction (numerator / denominator) and supports
    addition with another Fraction. The result should be stored in
    lowest terms (use the provided gcd helper).
    Assume denominator is always a positive integer.

    >>> a = Fraction(1, 2)
    >>> a.numerator
    1
    >>> a.denominator
    2
    >>> print(a)
    1/2
    >>> b = Fraction(1, 3)
    >>> c = a.add(b)
    >>> print(c)
    5/6
    >>> d = Fraction(2, 4)
    >>> print(d)        # stored in lowest terms
    1/2
    >>> e = Fraction(3, 6).add(Fraction(1, 6))
    >>> print(e)
    2/3
    """
    def _gcd(self, a: int, b: int) -> int:
        """Returns the greatest common divisor of a and b."""
        while b:
            a, b = b, a % b
        return a

    def __init__(self, numerator: int, denominator: int):
        gcd = self._gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def add(self, other: "Fraction") -> "Fraction":
        """Returns a new Fraction equal to self + other, in lowest terms."""
        new_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        return Fraction(new_numerator, new_denominator)


    def __str__(self) -> str:
        # YOUR CODE HERE
        # Should return e.g. "1/2"
        return f"{self.numerator}/{self.denominator}"


# ============================================================
# Run doctests when this file is executed directly
# ============================================================
if __name__ == "__main__":
    import doctest
    doctest.testmod()