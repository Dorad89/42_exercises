def is_palindrome(text: str) -> bool:
    newstr = ""
    for char in text:
        if char.isalnum():
            newstr += char.lower()

    return newstr == newstr[::-1]


print(is_palindrome("A man a plan a canal Panama"))  # Output: True
print(is_palindrome("Hello"))  # Output: False
print(is_palindrome("an a"))  # Output: True
print(is_palindrome("No 'x' in Nixon"))  # Output: True
print(is_palindrome("12321"))  # Output: True
