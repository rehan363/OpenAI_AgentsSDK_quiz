from typing import TypeVar, List

T = TypeVar('T')

def first_item(items: List[T]) ->T: #T can be any type (str, int)
    if items:
        return items[0] 
    raise ValueError("Empty List")

numbers = [4.3]
names = ["ali", "raza"]

print(first_item(numbers))
print(first_item(names))