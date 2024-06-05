# Delete Middle Element from Stack

This section explains the `delete_middle_element` function, which deletes the middle element from a stack implemented using the `Stack` class.

## Function: `delete_middle_element`

### Description

Deletes the middle element of the stack. If the stack has an even number of elements, it removes the element at index `n/2` (0-based index).

### Arguments

- `stack` (Stack): The stack from which the middle element will be deleted.

## Internal Helper Function: delete_recursively

This is a helper function used by delete_middle_element to delete the middle element using recursion.

### delete_recursively Arguments

- `stack` (Stack): The stack from which the middle element will be deleted.
- `current_index` (int): The current index being processed.
- `middle_index` (int): The index of the middle element.

```python
def delete_middle_element(stack):
    def delete_recursively(stack, current_index, middle_index):
        if stack.is_empty():
            return
        top = stack.pop()
        if current_index != middle_index:
            delete_recursively(stack, current_index + 1, middle_index)
            stack.push(top)

    if stack.is_empty():
        return
    middle_index = stack.size() // 2
    delete_recursively(stack, 0, middle_index)
```

## White Board

![White Board](./Stack,%20Queue.jpg)

![White Board](./Stack,%20Queue%20(1).jpg)
