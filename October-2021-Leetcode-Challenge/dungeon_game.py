class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        i, j = 0, 0
        m, n = len(dungeon), len(dungeon[0])
        sum_val = dungeon[0][0]
        print(sum_val)

        def dungeon_game(ival, jval):
            if ival < m and jval < m:
                if dungeon[ival+1][jval] < dungeon[ival][jval+1]:
                    sum_val = sum_val + dungeon[ival+1][jval]
                    dungeon_game(ival+1, jval)
                else:
                    sum_val = sum_val + dungeon[ival][jval+1]
                    dungeon_game(ival, jval+1)
            else:
                return sum_val

        print(dungeon_game(i, j))


dungeons_list = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
print(Solution.calculateMinimumHP(dungeons_list))
