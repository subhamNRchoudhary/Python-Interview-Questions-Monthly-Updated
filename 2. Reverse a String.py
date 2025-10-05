def reverse_string(s):
    # Method 1: Slicing
    return s[::-1]
    
    # Method 2: Two pointers
    # chars = list(s)
    # left, right = 0, len(chars) - 1
    # while left < right:
    #     chars[left], chars[right] = chars[right], chars[left]
    #     left += 1
    #     right -= 1
    # return ''.join(chars)

# Example
print(reverse_string("hello"))  # Output: "olleh"