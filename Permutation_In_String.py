'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
 
Note:
1.The input strings only contain lower case letters.
2.The length of both given strings is in range [1, 10,000].
'''
#Solution: Using sliding window algorithm and matching frequency of substring

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s2)<len(s1)):
            return False
        x=0
        s1c= Counter(s1)
        s2c= Counter(s2[x:len(s1)-1])
        
        for i in range(len(s1)-1,len(s2)):
            s2c[s2[i]]+=1
            if s2c==s1c:
                return True
            s2c[s2[x]]-=1
            if(s2c[s2[x]]==0):
                del s2c[s2[x]]
            x+=1
        return False
        
        
        
