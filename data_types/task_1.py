# Встроенные типы данных в Python

# Список всех immutable (неизменяемых)

# int (immutable)
number: int = 10
print(type(number))
assert isinstance(number, int)

# str (immutable)
line: str = "text"
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

# tuple (immutable)
the_tuple: tuple[int, ...] = (42,)
print(type(the_tuple))
assert isinstance(the_tuple, tuple)

# frozenset (immutable)
frozen: frozenset[int] = frozenset([1, 2, 3])
print(type(frozen))
assert isinstance(frozen, frozenset)

# bytes (immutable)
byte: bytes = b"text"
print(type(byte))
assert isinstance(byte, bytes)


# Список всех mutable (изменяемых)

# list (mutable)
number: list[int] = [1, 2, 3]
print(type(number))
assert isinstance(number, list)

# dict (mutable)
user: dict[str, int] = {"name": "Илья", "age": 26}
print(type(user))
assert isinstance(user, dict)

# set (mutable)
collection: set[int] = {1, 2, 3, 3, 2}
print(type(collection))
assert isinstance(collection, set)

# bytearray (mutable)
byte_array: bytearray = bytearray(b"text")
print(type(bytearray))
assert isinstance(byte_array, bytearray)
