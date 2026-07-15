def string_permutation_checker(str1: str, str2: str) -> bool:
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    return sorted(str1) == sorted(str2)
