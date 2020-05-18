'''
Find All Anagrams in a String
Solution
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Solution: We make a sliding window, whose size is same as length of the template(in this case, it is p). 
In each loop, we check if the sub-string in this window matches the template, then slide the window.
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        result=[]
        if(len(s)<len(p)):
            return result
        x=0
        pc= Counter(p)
        sc= Counter(s[x:len(p)-1])
        
        for i in range(len(p)-1,len(s)):
            sc[s[i]]+=1
            if sc==pc:
                result.append(x)
            sc[s[x]]-=1
            if(sc[s[x]]==0):
                del sc[s[x]]
            x+=1
        return result
        
        
        
