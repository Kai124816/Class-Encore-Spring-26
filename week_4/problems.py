import doctest

# ============================================================
# WEEK 4 PROBLEMS — Chapter 2: Deeper Inheritance,
# Magic Methods, Class Variables, and Polymorphism
# ============================================================

# ============================================================
# PROVIDED BASE CLASSES (do not modify)
# ============================================================

class Employee:
    """A base class representing an employee."""
    def __init__(self, name: str, base_salary: float):
        self.name = name
        self.base_salary = base_salary

    def annual_salary(self) -> float:
        return self.base_salary

    def summary(self) -> str:
        return f"{self.name} earns ${self.annual_salary():,.2f}/year."

    def __str__(self) -> str:
        return f"Employee({self.name})"


class Instrument:
    """A musical instrument with a name and a way to play it."""
    def __init__(self, name: str):
        self.name = name

    def play(self) -> str:
        return f"{self.name} makes a sound."

    def __str__(self) -> str:
        return f"Instrument({self.name})"


class LibraryItem:
    """An item that can be checked out of a library."""
    def __init__(self, title: str, item_id: int):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def check_out(self) -> None:
        self.checked_out = True

    def return_item(self) -> None:
        self.checked_out = False

    def is_available(self) -> bool:
        return not self.checked_out

    def __str__(self) -> str:
        status = "available" if self.is_available() else "checked out"
        return f'"{self.title}" [{status}]'


# ============================================================
# MULTI-LEVEL INHERITANCE (1–3)
# ============================================================

# Problem 1
class Manager(Employee):
    """
    A Manager is an Employee who earns a bonus on top of their base salary.
    - Add bonus: float as a third __init__ parameter. Store as self.bonus.
    - Use super().__init__ to set name and base_salary.
    - Override annual_salary() to return base_salary + bonus.
    - Override __str__ to return "Manager(<name>)".

    >>> m = Manager("Dana", 80000, 15000)
    >>> m.annual_salary()
    95000
    >>> m.summary()
    'Dana earns $95,000.00/year.'
    >>> str(m)
    'Manager(Dana)'
    >>> m.name
    'Dana'
    """
    def __init__(self, name: str, base_salary: float, bonus: float):
        # YOUR CODE HERE (use super().__init__ to set name and base_salary)
        pass

    def annual_salary(self) -> float:
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        pass


# Problem 2
class Director(Manager):
    """
    A Director is a Manager who also has a stock_grant (float) added on top.
    - Add stock_grant: float as a fourth __init__ parameter. Store as self.stock_grant.
    - Use super().__init__ to set name, base_salary, and bonus.
    - Override annual_salary() to return base_salary + bonus + stock_grant.
      Hint: call super().annual_salary() and add stock_grant — do NOT repeat
      the base_salary + bonus logic from Manager.
    - Override __str__ to return "Director(<name>)".

    >>> d = Director("Lee", 120000, 25000, 50000)
    >>> d.annual_salary()
    195000
    >>> d.summary()
    'Lee earns $195,000.00/year.'
    >>> str(d)
    'Director(Lee)'
    >>> d.bonus
    25000
    """
    def __init__(self, name: str, base_salary: float, bonus: float, stock_grant: float):
        # YOUR CODE HERE (use super().__init__ to set name, base_salary, and bonus)
        pass

    def annual_salary(self) -> float:
        # YOUR CODE HERE (call super().annual_salary() and add stock_grant)
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        pass


# Problem 3
class ElectricGuitar(Instrument):
    """
    An ElectricGuitar is an Instrument that can be amplified.
    - Add amp_volume: int (0–10) as a second __init__ parameter. Store as self.amp_volume.
    - Use super().__init__ to set name.
    - Override play() to return "<name> shreds at volume <amp_volume>."
    - Add turn_up(amount: int) -> None that increases amp_volume by amount,
      but never above 10.
    - Add turn_down(amount: int) -> None that decreases amp_volume by amount,
      but never below 0.
    - Override __str__ to return "ElectricGuitar(<name>, vol=<amp_volume>)".

    >>> g = ElectricGuitar("Stratocaster", 5)
    >>> g.play()
    'Stratocaster shreds at volume 5.'
    >>> g.turn_up(3)
    >>> g.amp_volume
    8
    >>> g.turn_up(5)  # should cap at 10
    >>> g.amp_volume
    10
    >>> g.turn_down(4)
    >>> g.amp_volume
    6
    >>> g.turn_down(100)  # should floor at 0
    >>> g.amp_volume
    0
    >>> str(g)
    'ElectricGuitar(Stratocaster, vol=0)'
    """
    def __init__(self, name: str, amp_volume: int):
        # YOUR CODE HERE (use super().__init__)
        pass

    def play(self) -> str:
        # YOUR CODE HERE
        pass

    def turn_up(self, amount: int) -> None:
        # YOUR CODE HERE
        pass

    def turn_down(self, amount: int) -> None:
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        pass


# ============================================================
# MAGIC METHODS: __eq__, __lt__, __len__, __add__ (4–6)
# ============================================================

# Problem 4
class Book(LibraryItem):
    """
    A Book is a LibraryItem with an author and page count.
    - Add author: str and pages: int as additional __init__ parameters
      (after title and item_id). Store both. Use super().__init__.
    - Override __str__ to return '"<title>" by <author> [<status>]'.
    - Implement __eq__(other) -> bool: two Books are equal if they have
      the same title AND author (item_id does not matter).
    - Implement __lt__(other) -> bool: a Book is "less than" another
      if it has fewer pages. This lets Books be compared and sorted by length.

    >>> b1 = Book("Dune", 101, "Frank Herbert", 412)
    >>> b2 = Book("Dune", 202, "Frank Herbert", 412)
    >>> b3 = Book("Foundation", 303, "Isaac Asimov", 255)
    >>> b1 == b2
    True
    >>> b1 == b3
    False
    >>> b3 < b1
    True
    >>> b1 < b3
    False
    >>> str(b1)
    '"Dune" by Frank Herbert [available]'
    >>> b1.check_out()
    >>> str(b1)
    '"Dune" by Frank Herbert [checked out]'
    """
    def __init__(self, title: str, item_id: int, author: str, pages: int):
        # YOUR CODE HERE (use super().__init__)
        pass

    def __eq__(self, other) -> bool:
        # YOUR CODE HERE
        pass

    def __lt__(self, other) -> bool:
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        pass


# Problem 5
class Playlist:
    """
    A Playlist holds a list of song title strings and supports
    len(), equality comparison, and concatenation.
    - __init__(self, name: str, songs: list[str] = None):
      store name and a COPY of songs (default to empty list if None).
    - __len__() -> int: returns the number of songs.
    - __eq__(other) -> bool: two Playlists are equal if they have the
      same songs in the same order (name does not matter).
    - __add__(other) -> Playlist: returns a NEW Playlist whose name is
      "<self.name>+<other.name>" and whose songs are self's songs
      followed by other's songs.
    - __str__: returns "Playlist(<name>, <n> songs)".

    >>> p1 = Playlist("Morning", ["Song A", "Song B"])
    >>> p2 = Playlist("Evening", ["Song A", "Song B"])
    >>> p3 = Playlist("Night", ["Song C"])
    >>> len(p1)
    2
    >>> p1 == p2
    True
    >>> p1 == p3
    False
    >>> combined = p1 + p3
    >>> len(combined)
    3
    >>> str(combined)
    'Playlist(Morning+Night, 3 songs)'
    >>> str(p1)
    'Playlist(Morning, 2 songs)'
    """
    def __init__(self, name: str, songs: list = None):
        # YOUR CODE HERE
        pass

    def __len__(self) -> int:
        # YOUR CODE HERE
        pass

    def __eq__(self, other) -> bool:
        # YOUR CODE HERE
        pass

    def __add__(self, other: "Playlist") -> "Playlist":
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        pass


# Problem 6
class Temperature:
    """
    Represents a temperature in Celsius. Supports comparison operators
    and conversion to Fahrenheit.
    - __init__(self, celsius: float): store as self.celsius.
    - to_fahrenheit() -> float: returns celsius * 9/5 + 32.
    - __eq__(other) -> bool: True if both have the same celsius value.
    - __lt__(other) -> bool: True if self.celsius < other.celsius.
    - __le__(other) -> bool: True if self is less than or equal to other.
    - __str__: returns "<celsius>°C".

    >>> t1 = Temperature(100)
    >>> t2 = Temperature(0)
    >>> t3 = Temperature(100)
    >>> t1.to_fahrenheit()
    212.0
    >>> t2.to_fahrenheit()
    32.0
    >>> t1 == t3
    True
    >>> t1 == t2
    False
    >>> t2 < t1
    True
    >>> t1 < t2
    False
    >>> t1 <= t3
    True
    >>> str(t2)
    '0°C'
    """
    def __init__(self, celsius: float):
        # YOUR CODE HERE
        pass

    def to_fahrenheit(self) -> float:
        # YOUR CODE HERE
        pass

    def __eq__(self, other) -> bool:
        # YOUR CODE HERE
        pass

    def __lt__(self, other) -> bool:
        # YOUR CODE HERE
        pass

    def __le__(self, other) -> bool:
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        pass


# ============================================================
# CLASS VARIABLES AND INSTANCE TRACKING (7–8)
# ============================================================

# Problem 7
class Robot:
    """
    A Robot has a name and tracks how many Robot instances have been
    created using a CLASS variable (shared across all instances).
    - CLASS variable: count = 0 (incremented each time __init__ runs).
    - __init__(self, name: str): store name; increment Robot.count.
    - robot_count() -> int: a regular method that returns Robot.count.
    - __str__: returns "Robot(<name>)".

    >>> Robot.count = 0  # reset for testing
    >>> Robot.count
    0
    >>> r1 = Robot("R2D2")
    >>> r2 = Robot("C3PO")
    >>> Robot.count
    2
    >>> r1.robot_count()
    2
    >>> r3 = Robot("HAL")
    >>> r2.robot_count()
    3
    >>> str(r1)
    'Robot(R2D2)'
    """
    count = 0  # class variable — do not move this

    def __init__(self, name: str):
        # YOUR CODE HERE
        pass

    def robot_count(self) -> int:
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE
        pass


# Problem 8
class Voter:
    """
    A Voter can cast a vote for a candidate. The class tracks all votes
    cast across all instances in a CLASS variable.
    - CLASS variable: votes = {}  (maps candidate name -> vote count)
    - __init__(self, name: str): store name. Mark this voter as not yet voted.
    - vote(candidate: str) -> None: if this voter hasn't voted yet,
      add 1 to votes[candidate] (creating the key if needed) and mark
      them as having voted. If they have already voted, do nothing.
    - has_voted() -> bool: returns whether this voter has voted.
    - results() -> dict: a regular method that returns the votes dict.

    Note: votes is shared across ALL Voter instances.

    >>> Voter.votes = {}  # reset for testing
    >>> v1 = Voter("Alice")
    >>> v2 = Voter("Bob")
    >>> v3 = Voter("Carol")
    >>> v1.has_voted()
    False
    >>> v1.vote("Candidate A")
    >>> v2.vote("Candidate B")
    >>> v3.vote("Candidate A")
    >>> v1.vote("Candidate B")  # already voted — should do nothing
    >>> v1.has_voted()
    True
    >>> v1.results() == {"Candidate A": 2, "Candidate B": 1}
    True
    """
    votes = {}  # class variable — do not move this

    def __init__(self, name: str):
        # YOUR CODE HERE
        pass

    def vote(self, candidate: str) -> None:
        # YOUR CODE HERE
        pass

    def has_voted(self) -> bool:
        # YOUR CODE HERE
        pass

    def results(self) -> dict:
        # YOUR CODE HERE
        pass


# ============================================================
# CHALLENGE PROBLEMS (9–10)
# ============================================================

# Problem 9 (Challenge)
class Vector2D:
    """
    Represents a 2D mathematical vector with x and y components.
    Implement the following magic methods:
    - __init__(self, x: float, y: float): store x and y.
    - __add__(other) -> Vector2D: vector addition — returns a new Vector2D
      whose x is self.x + other.x and y is self.y + other.y.
    - __mul__(scalar: float) -> Vector2D: scalar multiplication — returns a
      new Vector2D whose components are each multiplied by scalar.
    - __eq__(other) -> bool: True if both x and y components are equal.
    - __len__() -> int: returns the number of components, which is always 2.
      Note: __len__ must return an int.
    - __str__: returns "Vector2D(<x>, <y>)".
 
    >>> v1 = Vector2D(1, 2)
    >>> v2 = Vector2D(3, 4)
    >>> v3 = v1 + v2
    >>> str(v3)
    'Vector2D(4, 6)'
    >>> v4 = v1 * 3
    >>> str(v4)
    'Vector2D(3, 6)'
    >>> v1 == Vector2D(1, 2)
    True
    >>> v1 == v2
    False
    >>> str(v1)
    'Vector2D(1, 2)'
    >>> str(Vector2D(0, 0) + Vector2D(5, -3))
    'Vector2D(5, -3)'
    """
    def __init__(self, x: float, y: float):
        # YOUR CODE HERE
        pass
 
    def __add__(self, other: "Vector2D") -> "Vector2D":
        # YOUR CODE HERE
        pass
 
    def __mul__(self, scalar: float) -> "Vector2D":
        # YOUR CODE HERE
        pass
 
    def __eq__(self, other) -> bool:
        # YOUR CODE HERE
        pass
 
    def __str__(self) -> str:
        # YOUR CODE HERE
        pass


# Problem 10 (Challenge)
def highest_earner(employees: list) -> "Employee":
    """
    Given a list of Employee objects (any mix of Employee, Manager,
    and Director), return the one with the highest annual_salary().
    You may assume the list is non-empty.
    Use polymorphism — do NOT use isinstance() or type() checks.

    >>> e = Employee("Sam", 60000)
    >>> m = Manager("Dana", 80000, 15000)
    >>> d = Director("Lee", 120000, 25000, 50000)
    >>> highest_earner([e, m, d]) == d
    True
    >>> highest_earner([e, m]).name
    'Dana'
    >>> highest_earner([e]).name
    'Sam'
    """
    # YOUR CODE HERE
    pass


# ============================================================
# Run doctests when this file is executed directly.
# Uncomment the line for the problem you want to test.
# ============================================================
if __name__ == "__main__":
    import doctest
    # doctest.run_docstring_examples(Manager,        globals(), name="Manager")        # Problem 1
    # doctest.run_docstring_examples(Director,       globals(), name="Director")       # Problem 2
    # doctest.run_docstring_examples(ElectricGuitar, globals(), name="ElectricGuitar") # Problem 3
    # doctest.run_docstring_examples(Book,           globals(), name="Book")           # Problem 4
    # doctest.run_docstring_examples(Playlist,       globals(), name="Playlist")       # Problem 5
    # doctest.run_docstring_examples(Temperature,    globals(), name="Temperature")    # Problem 6
    # doctest.run_docstring_examples(Robot,          globals(), name="Robot")          # Problem 7
    # doctest.run_docstring_examples(Voter,          globals(), name="Voter")          # Problem 8
    # doctest.run_docstring_examples(Vector2D,        globals(), name="Vector2D")      # Problem 9
    # doctest.run_docstring_examples(highest_earner, globals(), name="highest_earner") # Problem 10
 