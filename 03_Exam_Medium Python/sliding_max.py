#Subject: Given an array and window size k,
#return the maximum of every contiguous window of length k,
#left to right.


#def sliding_w_m(ar, shift):
#	k = shift
#	n = len(ar)
#	i = 0
#	res = []
#	while (i < n):
#		if (n - i < k):
#			break
#		j = i
#		temp = []
#		while (j < i + k):
#			temp.append(ar[j])
#			j += 1
#		i += 1
#		res.append(max(temp))
#	return res

def sliding_w_m(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []

    return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]

from collections import deque

def sliding_w_m(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []

    dq = deque()          # holds indices, values decreasing
    result = []

    for i, val in enumerate(nums):
        # drop indices that fell out of the window
        if dq and dq[0] <= i - k:
            dq.popleft()
        # drop indices whose values can never be the max again
        while dq and nums[dq[-1]] <= val:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


print(sliding_w_m([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
print(sliding_w_m([1], 3))
print(sliding_w_m([1, 2, 3], 2))
print(sliding_w_m([1, 2], 8))
print(sliding_w_m([], 3))
