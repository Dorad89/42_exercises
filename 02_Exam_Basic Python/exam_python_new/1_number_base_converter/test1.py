def number_base_converter(number: str, from_base: int, to_base: int) -> str:

    if (2 <= from_base <= 36 and 2 <= to_base <= 36):
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        try:
            nr = int(number, from_base)
        except:
            return "Error"

        if nr == 0:
            return "0"

        while nr > 0:
            result = digits[nr % to_base] + result
            nr //= to_base

        return result

    return "Error"
