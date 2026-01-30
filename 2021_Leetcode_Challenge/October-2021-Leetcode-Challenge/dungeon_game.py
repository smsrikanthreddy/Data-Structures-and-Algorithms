class Solution:
    def calculateMinimumHP(self, dungeon):
        # Recursion
        # def dungeon_game(dungeon, ival, jval):
        #
        #     if ival == len(dungeon)-1 and jval == len(dungeon[0])-1:
        #         if dungeon[ival][jval] > 0:
        #             return 1
        #         else:
        #             return -dungeon[ival][jval] + 1
        #
        #     if ival == len(dungeon)-1:
        #         return max(1, dungeon_game(dungeon, ival, jval + 1) - dungeon[ival][jval])
        #
        #     if jval == len(dungeon[0])-1:
        #         return max(1, dungeon_game(dungeon, ival + 1, jval) - dungeon[ival][jval])
        #
        #     return max(1, min(dungeon_game(dungeon, ival + 1, jval) - dungeon[ival][jval],
        #                       dungeon_game(dungeon, ival, jval + 1) - dungeon[ival][jval]))
        # output_val = dungeon_game(dungeon, 0, 0)
        # print("output value is:-", output_val)

        # DP Top Down
        # TC - O(mn)
        # SC - O(mn)
        # m = len(dungeon)
        # n = len(dungeon[0])
        # dp = [[None]*(n+1) for i in range(m+1)]
        #
        # def dungeon_game(dungeon, ival, jval, dp):
        #
        #     if ival == len(dungeon)-1 and jval == len(dungeon[0])-1:
        #         if dungeon[ival][jval] > 0:
        #             return 1
        #         else:
        #             return -dungeon[ival][jval] + 1
        #     if dp[ival][jval] is not None:
        #         return dp[ival][jval]
        #
        #     if ival == len(dungeon)-1:
        #         dp[ival][jval] = max(1, dungeon_game(
        #             dungeon, ival, jval + 1, dp) - dungeon[ival][jval])
        #         return dp[ival][jval]
        #
        #     if jval == len(dungeon[0])-1:
        #         dp[ival][jval] = max(1, dungeon_game(
        #             dungeon, ival + 1, jval, dp) - dungeon[ival][jval])
        #         return dp[ival][jval]
        #
        #     dp[ival][jval] = max(1, min(dungeon_game(dungeon, ival + 1, jval, dp) - dungeon[ival][jval],
        #                                 dungeon_game(dungeon, ival, jval + 1, dp) - dungeon[ival][jval]))
        #     return dp[ival][jval]
        # return dungeon_game(dungeon, 0, 0, dp)

        # DP Bottom Up
        # TC - O(mn)
        # SC - O(mn)

        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0]*(n+1) for i in range(m+1)]

        if dungeon[m-1][n-1] > 0:
            dp[m-1][n-1] = 1
        else:
            dp[m-1][n-1] = abs(dungeon[m-1][n-1]) + 1

        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
        for i in range(2, -1, -1):
            dp[m - 1][i] = max(dp[m - 1][i + 1] - dungeon[m - 1][i], 1)
        '''
        fill the table in bottom-up fashion
        '''
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                min_points_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(min_points_on_exit - dungeon[i][j], 1)

        return dp[0][0]

        # method 2 - dp bottom up
        m, n = len(d), len(d[0])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    d[i][j] = max(1, -d[i][j] + 1)
                elif i < m-1 and j < n-1:
                    d[i][j] = max(1, min(-d[i][j] + d[i+1][j], -d[i][j] + d[i][j+1]))
                elif i < m-1:
                    d[i][j] = max(1, -d[i][j] + d[i+1][j])
                else:
                    d[i][j] = max(1, -d[i][j] + d[i][j+1])
        return d[0][0]


dungeons_list = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
dungeons_list = [[0]]
dung = Solution()
print(dung.calculateMinimumHP(dungeons_list))
