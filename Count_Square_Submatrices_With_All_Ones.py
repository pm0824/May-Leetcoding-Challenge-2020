'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 
Constraints:
1. 1 <= arr.length <= 300
2. 1 <= arr[0].length <= 300
3. 0 <= arr[i][j] <= 1

Solution: Using Dynamic Programming, it’s because we need an array to store the previous results while calculating all set of squares.
So basically we can start using the top-down approach.

'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        ans = [[0 for i in range(n)] for j in range(m)]
        count_squre = 0
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    ans[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:  
                    ans[i][j] = 0
                else:
                    ans[i][j] = matrix[i][j] + min(ans[i-1][j],ans[i-1][j-1],ans[i][j-1])
                count_squre += ans[i][j]
        print(ans)
        return count_squre
        
        
        

