class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r_len = len(grid)
        c_len = len(grid[0])
        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= r_len or c >= c_len or (r,c) in visited or grid[r][c] == "0":
                return
            
            visited.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        islands = 0
        for r in range(r_len):
            for c in range(c_len):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    islands+=1
        return islands
        