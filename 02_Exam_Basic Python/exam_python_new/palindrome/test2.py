def is_palindrome(text: str) -> bool:
    copy = ""
    for char in text:
        if char.isalnum():
            copy += char.lower()
    return copy == copy[::-1]

print(is_palindrome("an a"))  # Output: True
print(is_palindrome("No 'x' in Nixon"))  # Output: True
print(is_palindrome("12321"))  # Output: True