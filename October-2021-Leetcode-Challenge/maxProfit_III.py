class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        left = []
        right = []

        minLeft = prices[0]
        left = [0]*n
        for i in range(1, n):
            left[i] = max(left[i-1], (prices[i]-minLeft))
            minLeft = min(prices[i], minLeft)

        maxRight = prices[n-1]
        right = [0] * n
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], (maxRight-prices[i]))
            maxRight = max(prices[i], maxRight)

        result = 0
        for v1, v2 in zip(left, right):
            result = max(result, v1+v2)
        return result


class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        s1 = -prices[0]
        s2 = s4 = 0
        s3 = float('-inf')

        for i in range(1, n):
            s1 = max(s1, -prices[i])
            s2 = max(s2, s1+prices[i])
            s3 = max(s3, s2-prices[i])
            s4 = max(s4, s3+prices[i])

        return s4


ins = Solution()
data = [3, 3, 5, 0, 0, 3, 1, 4]
print(ins.maxProfit(data))
