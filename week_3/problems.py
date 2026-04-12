from numbers import Number
from math import sqrt

# ============================================================
# PROVIDED BASE CLASSES (do not modify)
# ============================================================

class Animal:
    """An animal with a name and sound."""
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} makes a sound."

    def describe(self) -> str:
        return f"I am {self.name}."

    def __str__(self) -> str:
        return f"Animal({self.name})"

    def __repr__(self) -> str:
        return f"Animal({self.name!r})"


class Vehicle:
    """A vehicle with a make and speed (in mph)."""
    def __init__(self, make: str, speed: int):
        self.make = make
        self.speed = speed

    def move(self) -> str:
        return f"{self.make} moves at {self.speed} mph."

    def fuel_type(self) -> str:
        return "gasoline"

    def __str__(self) -> str:
        return f"{self.make} ({self.speed} mph)"


class BankAccount:
    """A simple bank account with a balance."""
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        """Withdraw amount. Returns True if successful, False if insufficient funds."""
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def __str__(self) -> str:
        return f"{self.owner}: ${self.balance:.2f}"


class Shape:
    """Abstract base class for shapes."""
    def __init__(self):
        raise NotImplementedError("Shape is abstract; do not instantiate directly.")

    def area(self) -> float:
        raise NotImplementedError(f"Class {self.__class__} must define area()")

    def perimeter(self) -> float:
        raise NotImplementedError(f"Class {self.__class__} must define perimeter()")

    def describe(self) -> str:
        return f"I am a {self.__class__.__name__} with area {self.area():.2f}"


# ============================================================
# INHERITANCE AND OVERRIDING PROBLEMS (1–4)
# ============================================================

# Problem 1
class Dog(Animal):
    """
    A Dog is a kind of Animal.
    - Override speak() so it returns "<name> says: Woof!"
    - Add a new method fetch(item: str) -> str that returns
      "<name> fetches the <item>!"

    >>> d = Dog("Rex")
    >>> d.speak()
    'Rex says: Woof!'
    >>> d.describe()
    'I am Rex.'
    >>> d.fetch("ball")
    'Rex fetches the ball!'
    >>> str(d)
    'Animal(Rex)'
    """
    def speak(self) -> str:
        # YOUR CODE HERE
        pass

    def fetch(self, item: str) -> str:
        # YOUR CODE HERE
        pass


# Problem 2
class Cat(Animal):
    """
    A Cat is a kind of Animal.
    - Override speak() so it returns "<name> says: Meow!"
    - Override __str__ so it returns "Cat(<name>)" instead of "Animal(<name>)"
    - Add indoor: bool as a second __init__ parameter (default True).
      Store it as self.indoor.
    - Add a method is_indoor() -> bool that returns self.indoor.

    >>> c = Cat("Whiskers")
    >>> c.speak()
    'Whiskers says: Meow!'
    >>> str(c)
    'Cat(Whiskers)'
    >>> c.is_indoor()
    True
    >>> c2 = Cat("Tom", indoor=False)
    >>> c2.is_indoor()
    False
    >>> c.describe()
    'I am Whiskers.'
    """
    def __init__(self, name: str, indoor: bool = True):
        # YOUR CODE HERE
        pass

    def speak(self) -> str:
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        pass

    def is_indoor(self) -> bool:
        # YOUR CODE HERE
        pass


# Problem 3
class ElectricCar(Vehicle):
    """
    An ElectricCar is a kind of Vehicle.
    - Override fuel_type() to return "electric"
    - Override move() to return "<make> glides silently at <speed> mph."
    - Add a battery_level: int parameter to __init__ (after make and speed).
      Store it as self.battery_level (an integer percentage, 0–100).
    - Add charge(amount: int) -> None that increases battery_level by amount,
      but never above 100.

    >>> e = ElectricCar("Tesla", 120, 80)
    >>> e.fuel_type()
    'electric'
    >>> e.move()
    'Tesla glides silently at 120 mph.'
    >>> e.battery_level
    80
    >>> e.charge(30)
    >>> e.battery_level
    100
    >>> str(e)
    'Tesla (120 mph)'
    """
    def __init__(self, make: str, speed: int, battery_level: int):
        # YOUR CODE HERE
        pass

    def fuel_type(self) -> str:
        # YOUR CODE HERE
        pass

    def move(self) -> str:
        # YOUR CODE HERE
        pass

    def charge(self, amount: int) -> None:
        # YOUR CODE HERE
        pass


# Problem 4
class SavingsAccount(BankAccount):
    """
    A SavingsAccount is a kind of BankAccount with an interest rate.
    - Add interest_rate: float as a third __init__ parameter (a decimal, e.g. 0.05 for 5%).
      Store it as self.interest_rate.
    - Add apply_interest() -> None that increases balance by balance * interest_rate.
    - Override withdraw(amount) so that it also returns False if
      the balance after withdrawal would drop below 0.01 (i.e., a minimum balance of $0.01).
      Otherwise behave the same as BankAccount.withdraw.
    - Override __str__ to return "<owner> [Savings]: $<balance>" (formatted to 2 decimal places)

    >>> s = SavingsAccount("Alice", 100.0, 0.1)
    >>> s.apply_interest()
    >>> round(s.balance, 2)
    110.0
    >>> s.withdraw(109.99)
    True
    >>> s.withdraw(0.005) # minimum balance violated
    False
    >>> str(s)
    'Alice [Savings]: $0.01'
    """
    def __init__(self, owner: str, balance: float, interest_rate: float):
        # YOUR CODE HERE
        pass

    def apply_interest(self) -> None:
        # YOUR CODE HERE
        pass

    def withdraw(self, amount: float) -> bool:
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        pass


# ============================================================
# ABSTRACT CLASSES AND POLYMORPHISM PROBLEMS (5–7)
# ============================================================

# Problem 5
class Circle(Shape):
    """
    A concrete subclass of Shape representing a circle.
    - __init__(self, radius: float): do NOT call super().__init__().
      Store radius as self.radius.
    - area() returns pi * r^2  (use 3.14159 for pi)
    - perimeter() returns 2 * pi * r
    - __str__ returns "Circle(r=<radius>)"

    >>> c = Circle(5)
    >>> round(c.area(), 2)
    78.54
    >>> round(c.perimeter(), 2)
    31.42
    >>> c.describe()
    'I am a Circle with area 78.54'
    >>> str(c)
    'Circle(r=5)'
    """
    PI = 3.14159

    def __init__(self, radius: float):
        # YOUR CODE HERE
        pass

    def area(self) -> float:
        # YOUR CODE HERE
        pass

    def perimeter(self) -> float:
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        pass


# Problem 6
class Rectangle(Shape):
    """
    A concrete subclass of Shape representing a rectangle.
    - __init__(self, width: float, height: float): store both.
    - area() returns width * height
    - perimeter() returns 2 * (width + height)
    - __str__ returns "Rectangle(w=<width>, h=<height>)"

    >>> r = Rectangle(4, 6)
    >>> r.area()
    24
    >>> r.perimeter()
    20
    >>> str(r)
    'Rectangle(w=4, h=6)'
    >>> r.describe()
    'I am a Rectangle with area 24.00'
    """
    def __init__(self, width: float, height: float):
        # YOUR CODE HERE
        pass

    def area(self) -> float:
        # YOUR CODE HERE
        pass

    def perimeter(self) -> float:
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        pass


# Problem 7
def total_area(shapes: list) -> float:
    """
    Given a list of Shape objects (any mix of concrete subclasses),
    return the sum of all their areas.
    Returns 0.0 for an empty list.

    >>> total_area([])
    0.0
    >>> total_area([Rectangle(3, 4), Rectangle(2, 5)])
    22.0
    >>> shapes = [Circle(1), Rectangle(2, 3)]
    >>> round(total_area(shapes), 2)
    9.14
    """
    # YOUR CODE HERE
    pass


# ============================================================
# LISKOV SUBSTITUTION & INHERITING FROM BUILT-INS (8–10)
# ============================================================

# Problem 8
class FixedList(list):
    """
    A list subclass with a maximum allowed size.
    - __init__(self, max_size: int): store max_size; start with an empty list.
    - Override append(item) so that if len(self) >= max_size, it raises
      ValueError("List is full") instead of appending.
    - Add is_full() -> bool that returns True when len(self) == max_size.
    - All other list methods are inherited unchanged.

    >>> fl = FixedList(3)
    >>> fl.append(1)
    >>> fl.append(2)
    >>> fl.append(3)
    >>> fl.is_full()
    True
    >>> fl.append(4)
    Traceback (most recent call last):
        ...
    ValueError: List is full
    >>> len(fl)
    3
    >>> fl[0]
    1
    """
    def __init__(self, max_size: int):
        # YOUR CODE HERE
        pass

    def append(self, item) -> None:
        # YOUR CODE HERE
        pass

    def is_full(self) -> bool:
        # YOUR CODE HERE
        pass


# Problem 9
class DefaultDict(dict):
    """
    A dict subclass that returns a default value for missing keys instead of
    raising a KeyError.
    - __init__(self, default): store the default; start with an empty dict.
    - Override __getitem__(key) so that if key is not present, return self.default
      (do NOT insert the key into the dict).
    - Add set_default(new_default) -> None to change the default value.
    - All other dict methods are inherited unchanged.

    >>> d = DefaultDict(0)
    >>> d["a"] = 5
    >>> d["a"]
    5
    >>> d["b"]
    0
    >>> "b" in d
    False
    >>> d.set_default(99)
    >>> d["missing"]
    99
    """
    def __init__(self, default):
        # YOUR CODE HERE
        pass

    def __getitem__(self, key):
        # YOUR CODE HERE
        pass

    def set_default(self, new_default) -> None:
        # YOUR CODE HERE
        pass

# Problem 10
class ShapeCollection(list):
    """
    A list subclass that holds Shape objects and provides
    summary statistics about them.
    - No __init__ needed; inherit list's __init__ directly.
    - Add largest() -> Shape that returns the Shape with the greatest area.
      You may assume the list is non-empty when this is called.
    - Add total_perimeter() -> float that returns the sum of all shapes'
      perimeters. Returns 0.0 for an empty collection.
    - Override append(item) to raise TypeError("Only Shape objects allowed")
      if item is not an instance of Shape.
 
    >>> sc = ShapeCollection()
    >>> sc.append(Rectangle(2, 3))
    >>> sc.append(Rectangle(4, 5))
    >>> sc.total_perimeter()
    28.0
    >>> sc.largest().area()
    20
    >>> sc.append("not a shape")
    Traceback (most recent call last):
        ...
    TypeError: Only Shape objects allowed
    >>> len(sc)
    2
    """
    def append(self, item) -> None:
        # YOUR CODE HERE
        pass
 
    def largest(self) -> Shape:
        # YOUR CODE HERE
        pass
 
    def total_perimeter(self) -> float:
        # YOUR CODE HERE
        pass
 


# ============================================================
# Run doctests when this file is executed directly.
# Uncomment the line for the problem you want to test,
# then run this file. Comment it back out when done.
# ============================================================
if __name__ == "__main__":
    import doctest
    # doctest.run_docstring_examples(Dog,           globals(), verbose=True, name="Dog")
    # doctest.run_docstring_examples(Cat,           globals(), verbose=True, name="Cat")
    # doctest.run_docstring_examples(ElectricCar,   globals(), verbose=True, name="ElectricCar")
    # doctest.run_docstring_examples(SavingsAccount,globals(), verbose=True, name="SavingsAccount")
    # doctest.run_docstring_examples(Circle,        globals(), verbose=True, name="Circle")
    # doctest.run_docstring_examples(Rectangle,     globals(), verbose=True, name="Rectangle")
    # doctest.run_docstring_examples(total_area,    globals(), verbose=True, name="total_area")
    # doctest.run_docstring_examples(FixedList,     globals(), verbose=True, name="FixedList")
    # doctest.run_docstring_examples(DefaultDict,   globals(), verbose=True, name="DefaultDict")
    # doctest.run_docstring_examples(LoudDog,       globals(), verbose=True, name="LoudDog")
    # doctest.run_docstring_examples(ShapeCollection, globals(), verbose=True, name="ShapeCollection") #Problem 10