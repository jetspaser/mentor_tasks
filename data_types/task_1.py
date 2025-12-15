# Встроенные типы данных в Python

# Список всех immutable (неизменяемых)

# int (immutable) - неизменяемый тип данных для представления целых чисел
number: int = 10
print(type(number))
assert isinstance(number, int)

# str (immutable) - неизменяемый тип данных для представления строк (Unicode)
line: str = "text"
print(type(line))
assert isinstance(line, str)

# float (immutable) - неизменяемый тип данных для чисел с плавающей точкой
floating: float = 10.5
print(type(floating))
assert isinstance(floating, float)

# bool (immutable) - неизменяемый тип данных для логических значений
true_false: bool = True
print(type(true_false))
assert isinstance(true_false, bool)

# tuple (immutable) - неизменяемая упорядоченная коллекция элементов
the_tuple: tuple[int, ...] = (42,)
print(type(the_tuple))
assert isinstance(the_tuple, tuple)

# frozenset (immutable) - неизменяемая коллекция уникальных элементов
frozen: frozenset[int] = frozenset([1, 2, 3])
print(type(frozen))
assert isinstance(frozen, frozenset)

# bytes (immutable) - неизменяемая последовательность байтов
byte: bytes = b"text"
print(type(byte))
assert isinstance(byte, bytes)

# range (immutable) - неизменяемый тип данных для представления последовательности чисел
numbers_range: range = range(10)
print(type(numbers_range))
assert isinstance(numbers_range, range)


# Список всех mutable (изменяемых)

# list (mutable) - изменяемая упорядоченная коллекция элементов
number: list[int] = [1, 2, 3]
print(type(number))
assert isinstance(number, list)

# dict (mutable) - изменяемая, но упорядоченная коллекция пар ключ-значение
user: dict[str, int] = {"name": "Илья", "age": 26}
print(type(user))
assert isinstance(user, dict)

# set (mutable) - изменяемая неупорядоченная коллекция уникальных элементов
collection: set[int] = {1, 2, 3, 3, 2}
print(type(collection))
assert isinstance(collection, set)

# bytearray (mutable) - изменяемая последовательность байтов
byte_array: bytearray = bytearray(b"text")
print(type(bytearray))
assert isinstance(byte_array, bytearray)

