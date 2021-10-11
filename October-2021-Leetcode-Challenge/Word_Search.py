# To Do
# https://www.youtube.com/watch?v=Ia-UEYYR44s
class Solution:
    def exist(self, board, word) -> bool:
        m, n = len(board), len(board[0])
        cntr = []

        def identify_word(board, word, ival, jval, idx):

            if ival == m-1 and jval == n-1:
                if board[ival][jval] == word[idx]:
                    idx += 1
                    return 1
            if ival == m-1:
                return identify_word(board, word, ival+1, jval, idx)

            if jval == n-1:
                return identify_word(board, word, ival, jval+1, idx)

            if board[ival][jval] == word[idx]:
                idx += 1
                cntr.append(1)

            return max(identify_word(board, word, ival, jval+1, idx),
                       identify_word(board, word, ival+1, jval, idx))
        breakpoint()
        values = identify_word(board, word, 0, 0, 0)
        return values


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
sol = Solution()
print(sol.exist(board, word))
