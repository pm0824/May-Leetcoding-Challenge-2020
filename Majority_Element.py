'''

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

'''

#Solution:

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c= Counter(nums)                        #0. counting frequency of each number in array
        f= math.floor(len(nums)/2)              #1. calculating floor(n/2) where n is length of array
        for i in c:                             #2. using for loop finding the number with frequency greater than floor value
            if(c[i]>f):
                return i
                
                
                
