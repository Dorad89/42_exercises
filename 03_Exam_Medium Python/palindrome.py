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



print(palindrome_cut("AABAC"))
print(palindrome_cut("aab"))  # Output: 1
print(palindrome_cut("a"))    # Output: 0
print(palindrome_cut("ab"))   # Output: 1
print(palindrome_cut("abc"))  # Output: 2
print(palindrome_cut("racecar"))
