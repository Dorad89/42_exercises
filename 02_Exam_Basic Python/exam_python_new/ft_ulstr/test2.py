
def ulstr(text: str) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            if 'a' <= char <= 'z':
                result += char.upper()
            elif 'A' <= char <= 'Z':
                result += char.lower()
        else:
            result += char
    return result


