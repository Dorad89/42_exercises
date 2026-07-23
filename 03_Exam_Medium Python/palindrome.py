#Subject: Given a string,
#return the minimum number of cuts needed to partition it
#so that every piece is a palindrome.

def is_palindrome(word: str) -> bool:
	return word == word[::-1]
def palindrome_cut(word: str) -> int:
	cuts = 0
	i = 0
	while i < len(word):
		for j in range(len(word), i, -1):
			if is_palindrome(word[i:j]):
				if j != len(word):
					cuts += 1
				i = j
				break
	return cuts


#Claude version
def palindrome_cut(word: str) -> int:
    n = len(word)
    if n == 0:
        return 0

    # pal[i][j] = True if word[i..j] is a palindrome
    pal = [[False] * n for _ in range(n)]
    for i in range(n):
        pal[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if word[i] == word[j] and (length == 2 or pal[i+1][j-1]):
                pal[i][j] = True

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
