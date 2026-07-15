def pattern_tracker(text: str) -> int:
    count = 0
    for n in range(len(text) - 1):
        if text[n].isdigit() and text[n + 1].isdigit():
            if int(text[n + 1]) == int(text[n]) + 1:
                count += 1
    return count


print(pattern_tracker("01234567"))
