# Leetcode Problem 1411: Number of Ways to Paint N × 3 Grid
# Difficulty: Hard
"""
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

Example 1:


Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.
Example 2:

Input: n = 5000
Output: 30228214
 

Constraints:

n == grid.length
1 <= n <= 5000
"""

# Code:
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base case for n = 1
        diff = 6   # all three cells different
        same = 6   # first and third same
        
        for _ in range(2, n + 1):
            new_diff = (diff * 2 + same * 2) % MOD
            new_same = (diff * 2 + same * 3) % MOD
            diff, same = new_diff, new_same
        
        return (diff + same) % MOD