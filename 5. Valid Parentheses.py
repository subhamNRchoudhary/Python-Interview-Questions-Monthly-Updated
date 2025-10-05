def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

# Example
print(is_valid_parentheses("()[]{}"))  # Output: True
print(is_valid_parentheses("([)]"))    # Output: False