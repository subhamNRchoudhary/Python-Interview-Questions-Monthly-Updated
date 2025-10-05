def is_anagram(s1, s2):
    # Method 1: Using sorted
    return sorted(s1) == sorted(s2)
    
    # Method 2: Using frequency counter
    # if len(s1) != len(s2):
    #     return False
    # freq = {}
    # for char in s1:
    #     freq[char] = freq.get(char, 0) + 1
    # for char in s2:
    #     if char not in freq or freq[char] == 0:
    #         return False
    #     freq[char] -= 1
    # return True

# Example
print(is_anagram("listen", "silent"))  # Output: True