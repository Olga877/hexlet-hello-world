print("Hello from python project!")
from more_itertools import flatten

coll = [(0, 1), (2, 3)]
# делаем коллекцию плоской
print(list(flatten(coll)))  # => [0, 1, 2, 3]
