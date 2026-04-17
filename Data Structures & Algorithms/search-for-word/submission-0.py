class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        n = len(word)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c,i):
            if i == n:
                return True
            if (r,c) in path or r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]:
                return False
            path.add((r, c))
            for dx, dy in directions:
                if dfs(r+dx, c+dy, i+1):
                    return True
            path.remove((r,c))
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False
