from typing import List, Dict, Tuple, Optional, Union, Callable, Any

def process_items(items: List[Union[int, str]]) -> Dict[str, List[Union[int, str]]]:
    result = {"numbers": [], "strings": []}
    for item in items:
        if isinstance(item, int):
            result["numbers"].append(item)
        elif isinstance(item, str):
            result["strings"].append(item)
    return result

def optional_example(value: Optional[int] = None) -> str:
    if value is None:
        return "No value provided"
    return f"Value is {value}"

def perform_operation(operation: Callable[[int, int], int], a: int, b: int) -> int:
    return operation(a, b)

print(perform_operation(lambda x, y: x + y, 1, 2)) # 3
print(process_items([1, 2, "a", "b", 3])) # {'numbers': [1, 2, 3], 'strings': ['a', 'b']}
print(optional_example()) # No value provided