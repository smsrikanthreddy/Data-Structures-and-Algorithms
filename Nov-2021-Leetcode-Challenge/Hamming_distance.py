class Solution:
    # Method 1
    # TC -
    # SC -
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        setBits = 0

        while (x > 0):
            setBits += x & 1
            x >>= 1

        return setBits
