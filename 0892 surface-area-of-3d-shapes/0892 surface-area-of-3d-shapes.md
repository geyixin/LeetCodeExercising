# 892 surface-area-of-3d-shapes(三维形体的表面积)

+ [题目链接](https://leetcode-cn.com/problems/surface-area-of-3d-shapes/)
+ 跟我之前做的[463岛屿面积](https://github.com/geyixin/LeetCodeExercising/tree/master/0463%20Island%20Perimeter)差不多，不多说了，直接附上代码


```
class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        len_grid = len(grid)
        for i in range(len_grid):
            for j in range(len_grid):
                if grid[i][j] != 0:
                    res += grid[i][j] * 4 + 2
                if i > 0:
                    res -= min(grid[i][j], grid[i-1][j])*2
                if j > 0:
                    res -= min(grid[i][j], grid[i][j-1])*2
        return res
```


```
class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        chang = len(grid)
        kuan = len(grid[0])
        for i in range(chang):
            for j in range(kuan):
                if grid[i][j] != 0:
                    res += grid[i][j] * 4 + 2
                    print(i,j,res)
                    if j + 1 < kuan:
                        if grid[i][j+1] != 0:
                            res -= min(grid[i][j], grid[i][j+1]) * 2
                            print(i,j,res)
                    if i + 1 < chang:
                        if grid[i+1][j] != 0:
                            res -= min(grid[i][j], grid[i+1][j]) * 2
                            print(i,j,res)
        return res
```

