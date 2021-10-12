# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        curr = -1
        while curr != 0:
            curr = guess(high)
            if curr == 0:
                return high
            if curr == -1:
                val = int((low+high)/2)
                high = val
            if curr == 1:
                val = int((low+high)/2)
                low = high
                high = high+val
