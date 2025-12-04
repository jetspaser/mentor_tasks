# Встроенные типы данных в Python

# Список всех immutable (неизменяемых)

# int (immutable) - это неизменяемый (immutable) тип данных для представления целых чисел в Python.
number: int = 10
print(type(number))
assert isinstance(number, int)

# str (immutable) - это неизменяемый (immutable) тип данных в Python, представляющий текстовые данные как последовательность символов Unicode
line: str = 'text'
print(type(line))
assert isinstance(line, str)

# float (immutable) - это неизменяемый (immutable) тип данных в Python, представляющий числа с плавающей точкой (дробные числа)
floating: float = 10.5
print(type(floating))
assert isinstance(floating, float)

# bool (immutable) - это неизменяемый (immutable) тип данных в Python, представляющий логические значения: True (истина) или False (ложь)
true_false: bool = True
print(type(true_false))
assert isinstance(true_false, bool)

# tuple (immutable) - "Кортеж — это неизменяемая (immutable) упорядоченная коллекция элементов в Python. Как список, но нельзя изменить после создания."
the_tuple: tuple = (42,)
print(type(the_tuple))
assert isinstance(the_tuple, tuple)

# frozenset (immutable) - это неизменяемый (immutable) тип данных в Python, представляющий неупорядоченную коллекцию уникальных элементов (как set, но нельзя изменять)
frozen: frozenset = frozenset([1, 2, 3])
print(type(frozen))
assert isinstance(frozen, frozenset)

# bytes (immutable) - это неизменяемый (immutable) тип данных в Python, представляющий последовательность байтов (сырые бинарные данные, числа 0-255)
byte: bytes = b"text"
print(type(byte))
assert isinstance(byte, bytes)


# Список всех mutable (изменяемых)

# list (mutable) - это изменяемый (mutable) тип данных в Python, представляющий упорядоченную коллекцию элементов с возможностью изменения
number: list = [1, 2, 3]
print(type(number))
assert isinstance(byte, bytes)

# dict (mutable) - это изменяемый (mutable) тип данных в Python, представляющий неупорядоченную коллекцию пар ключ-значение (ассоциативный массив)
user: dict[str, int] = {"name": "Илья", "age": 26}
print(type(user))
assert isinstance(byte, bytes)

# set (mutable) - это изменяемый (mutable) тип данных в Python, представляющий неупорядоченную коллекцию уникальных элементов.
collection: set[int] = {1, 2, 3, 3, 2}
print(type(collection))
assert isinstance(collection, set)

# bytearray (mutable)  - это изменяемый (mutable) тип данных в Python, представляющий изменяемую последовательность байтов (аналог bytes, но можно изменять)
byte_array: bytearray = bytearray(b"text")
print(type(bytearray))
assert isinstance(byte_array, bytearray)