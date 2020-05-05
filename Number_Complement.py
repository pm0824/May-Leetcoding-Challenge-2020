'''

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 
Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0

'''

#Solution 1 - Brute Force Method

binaryNum = '{0:b}'.format(num)
binaryNumFlipped = ''
for i in binaryNum:
	binaryNumFlipped += '1' if i == 0 else '0'
return int(binaryNumFlipped, 2)

#Solution 2 - 2^(no. of bits in binary of num) - 1 - num

class Solution:
    def findComplement(self, num: int) -> int:
        return 2**(len(bin(num))-2) + ~num      # ~num = -num-1
        
        
