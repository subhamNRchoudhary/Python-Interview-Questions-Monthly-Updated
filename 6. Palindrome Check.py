def is_palindrome(s):
    # Clean the string
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check palindrome
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

# Example
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True