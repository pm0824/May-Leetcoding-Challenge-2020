'''

Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false

'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (str(num ** 0.5))[-1] == '0':        #if num= 16  str('4.0')[-1] is '0'    
            return True
        return False
        
        
        
