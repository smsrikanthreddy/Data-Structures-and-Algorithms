class Solution:
    def dfs(self, i, j, board):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != "O":
            return
        board[i][j] = "I"
        self.dfs(i+1, j, board)
        self.dfs(i, j+1, board)
        self.dfs(i-1, j, board)
        self.dfs(i, j-1, board)

    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        for i in range(row):
            self.dfs(i, 0, board)
            self.dfs(i, col-1, board)
        for j in range(col):
            self.dfs(0, j, board)
            self.dfs(row-1, j, board)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "I":
                    board[i][j] = "O"


ins = Solution()
board = [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]
board = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"], [
    "X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"], ["X", "X", "O", "X", "O"]]
print(ins.solve(board))
