'''

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

'''

#Solution 1 :  Time complexity is O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if(s.count(i)==1):
                return s.index(i)
                break
        return -1
        
#Solution 2: Avoids repeated checking of count by keeping track of visited chatacters

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = set()
        for i in range(len(s)):
            if s[i] not in c:
                c.add(s[i])
                if s.count(s[i]) == 1:
                    return i
        return -1
        

