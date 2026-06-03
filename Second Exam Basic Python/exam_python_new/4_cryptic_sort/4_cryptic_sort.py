def cryptic_sort(strings: list[str]) -> list:
    return sorted(strings, key=lambda s:
                           (len(s), s.lower(), sum(char in "aeiouAEIOU" for char in s)))

# Example
print(cryptic_sort(["A", "banana", "grape", "kiwi", "oArange"]))
print(cryptic_sort(["a", "e", "b", "o", "u"]))
print(cryptic_sort(["Arsen", "arsen", "ARSEN"]))
print(cryptic_sort(["aaa", "AAA", "bbb", "BBB"]))