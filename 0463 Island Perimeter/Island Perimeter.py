class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hang = len(grid)
        lie = len(grid[0])
        zhouchang = 0
        for i in range(hang):
            for j in range(lie):
                if grid[i][j] == 1:
                    zhouchang += 4
                    if j + 1 < lie:
                        if grid[i][j+1] == 1:
                            zhouchang -= 2
                    if i + 1 < hang:
                        if grid[i+1][j] == 1:
                            zhouchang -= 2
        return zhouchang