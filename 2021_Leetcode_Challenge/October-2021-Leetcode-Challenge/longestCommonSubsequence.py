class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Recursion
        # m = len(text1)
        # n = len(text2)
        #
        # def lcs(i, j):
        #     if i >= m or j >= n:
        #         return 0
        #     elif text1[i] == text2[j]:
        #         return 1 + lcs(i+1, j+1)
        #     else:
        #         return max(lcs(i+1, j), lcs(i, j+1))
        #
        # return lcs(0, 0)

        # DP
        m = len(text1)
        n = len(text2)

        # create an array of mxn
        # arr = [[None]*(n+1)]*(m+1)
        arr = [[None]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    arr[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    arr[i][j] = arr[i-1][j-1]+1
                else:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])

        # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
        # print(arr)
        return arr[m][n]


text1 = "ezupkr"
text2 = "ubmrapg"
text1 = "oxcpqrsvwf"
text2 = "shmtulqrypy"
text1 = "abcde"
text2 = "ace"

lcs = Solution()
print(lcs.longestCommonSubsequence(text1, text2))
