class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hang = len(grid)
        lie = len(grid[0])
        areas = []
        for i in range(hang):
            for j in range(lie):
                if grid[i][j]:
                    areas.append(self.dfs(i, j, grid, hang, lie))
        if areas:
            return max(areas)
        else:
            return 0
    
    def dfs(self, i, j, grid, hang, lie):
        if 0 <= i < hang and 0 <= j < lie and grid[i][j]:
            grid[i][j] = 0
            return 1 + self.dfs(i - 1, j, grid, hang, lie) + self.dfs(i, j + 1, grid, hang, lie) + self.dfs(i + 1, j, grid, hang, lie) + self.dfs(i, j - 1, grid, hang, lie)
        return 0