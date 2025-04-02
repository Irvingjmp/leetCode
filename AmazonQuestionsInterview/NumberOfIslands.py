class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        number_of_rows, number_of_columns = len(grid), len(grid[0])
        number_of_islands = 0

        def depth_first_search(row, column):
            # Check boundaries and water
            if row < 0 or row >= number_of_rows or column < 0 or column >= number_of_columns or grid[row][column] == "0":
                return
            # Mark as visited
            grid[row][column] = "0"
            print(row,column)
            # Visit all neighboring cells (up, down, left, right)
            depth_first_search(row + 1, column)
            depth_first_search(row - 1, column)
            depth_first_search(row, column + 1)
            depth_first_search(row, column - 1)

        # Iterate through each cell of the grid
        for row in range(number_of_rows):
            for column in range(number_of_columns):
                if grid[row][column] == "1":
                    print("r,c",row,column)
                    number_of_islands += 1  # New island found
                    depth_first_search(row, column)  # Mark the whole island as visited
        print(grid)
        return number_of_islands

sol = Solution()

sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])