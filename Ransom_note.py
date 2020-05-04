'''

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l=[0]*26          #list for counting occurences of 26 chars in magazine
        for i in magazine:
            l[ord(i)-ord('a')]+=1
        for i in ransomNote:
            if(l[ord(i)-ord('a')]==0):    #if occurence is 0 then return false
                return False
            l[ord(i)-ord('a')]-=1         #decrement counter if char is present
        return True
                
