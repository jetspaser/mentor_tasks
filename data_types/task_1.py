# Встроенные типы данных в Python

# Список всех immutable (неизменяемых)

# int (immutable)
number: int = 10
print(type(number))
assert isinstance(number, int)

# str (immutable)
line: str = 'text'
print(type(line))
assert isinstance(line, str)

# float (immutable)
floating: float = 10.5
print(type(floating))
assert isinstance(floating, float)

# bool (immutable)
true_false: bool = True
print(type(true_false))
assert isinstance(true_false, bool)

# tuple (immutable) - "Кортеж — это неизменяемая (immutable) упорядоченная коллекция элементов в Python. Как список, но нельзя изменить после создания."
the_tuple: tuple = (42,)
print(type(the_tuple))
assert isinstance(the_tuple, tuple)

# frozenset (immutable)
n_frozenset = frozenset([1, 2, 3])
print(type(n_frozenset))

# bytes (immutable)
n_bytes = b"hello"
print(type(n_bytes))


# Список всех mutable (изменяемых)

# list (mutable)
number: list = [1, 2, 3]
print(type(number))

# dict (mutable)
user: dict[str, int] = {"name": "Илья", "age": 26}
print(type(user))

# set (mutable)
n_bytes = b"hello"
print(type(n_bytes))

# bytearray (mutable)
n_bytes = b"hello"
print(type(n_bytes))