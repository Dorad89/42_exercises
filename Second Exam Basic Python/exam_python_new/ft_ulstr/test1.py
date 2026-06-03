def ft_ulstr(text: str) -> str:
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += char.lower()
        elif 'a' <= char <= 'z':
            result += char.upper()
        else:
            result += char
    
    return result

print(ft_ulstr("Hello World"))