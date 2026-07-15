def string_sculptor(text: str) -> str:
    result = ""
    index = 0
    for char in text:
        if char.isalpha():
            if index % 2 == 0:
                result += char.lower()
                index += 1
            elif index % 2 != 0:
                result += char.upper()
                index += 1
        else:
            result += char

    return result


print (string_sculptor("Heello/123 World"))
