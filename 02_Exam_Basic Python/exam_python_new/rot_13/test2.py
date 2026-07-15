def rot_13(text: str) -> str:
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    
    return result


print(rot_13("Hello, World!"))  # Output: "Uryyb, Jbeyq!"
print(rot_13("Uryyb, Jbeyq!"))  # Output: "Hello, World!"