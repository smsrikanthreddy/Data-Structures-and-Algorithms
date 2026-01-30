# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

def guess(num: int, val) -> int:
    if num < val:
        return -1
    elif num > val:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int, guess_val) -> int:
        # breakpoint()
        low = 0
        high = n
        while low <= high:
            mid = int((low+high)/2)
            curr = guess(mid, guess_val)
            if curr == -1:
                high = mid-1
            elif curr == 1:
                low = mid+1
            else:
                return mid


pc = Solution()
print(pc.guessNumber(10, 8))

# class Solution:
#     def guessNumber(self, n: int) -> int:
#         low = 1
#         high = n
#         while True:
#             mid = int((low+high)/2)
#             curr = guess(mid)
#             if curr == -1:
#                 high = mid-1
#             elif curr == 1:
#                 low = mid+1
#             else:
#                 return mid


# Recursion
# class Solution:
#     def guessNumber(self, n: int) -> int:
#         return self.guess_recursive(0, n)
#
#     def guess_recursive(self, low, high):
#         mid = int((low+high)/2)
#         curr = guess(mid)
#         if curr== -1:
#             return self.guess_recursive(low, mid-1)
#         elif curr == 1:
#             return self.guess_recursive(mid+1, high)
#         else:
#             return mid
