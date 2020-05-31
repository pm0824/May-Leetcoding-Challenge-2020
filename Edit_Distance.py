'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
1. Insert a character
2. Delete a character
3. Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

#Solution : Using Dynamic Programming Time Complexity: O(m x n) Space: O(m x n)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m=len(word1)
        n=len(word2)
        dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
 
        for i in range(m + 1): 
            for j in range(n + 1): 
                if i == 0: 
                    dp[i][j] = j     
  
                elif j == 0: 
                    dp[i][j] = i   
  
                elif word1[i-1] == word2[j-1]: 
                    dp[i][j] = dp[i-1][j-1] 
            
                else: 
                    dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        return dp[m][n] 
        
        
        
        
        
