#Subject: Given a string,
#return the minimum number of cuts needed to partition it
#so that every piece is a palindrome.

def palindrome_cut(word: str) -> int:
    n = len(word)
    if n == 0:
        return 0

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    # pal[i][j] = True if word[i..j] is a palindrome
    pal = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            pal[i][j] = is_palindrome(word[i:j+1])

    dp = [0] * n
    for i in range(n):
        if pal[0][i]:
            dp[i] = 0
            continue
        dp[i] = i
        for j in range(1, i + 1):
            if pal[j][i]:
                dp[i] = min(dp[i], dp[j-1] + 1)

    return dp[n-1]

print(palindrome_cut("AABAC"))
print(palindrome_cut("aab"))  # Output: 1
print(palindrome_cut("a"))    # Output: 0
print(palindrome_cut("ab"))   # Output: 1
print(palindrome_cut("abc"))  # Output: 2
print(palindrome_cut("racecar"))
