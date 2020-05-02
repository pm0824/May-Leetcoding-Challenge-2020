'''
FIRST BAD VERSION
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
Example:
Given n = 5, and version = 4 is the first bad version.
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version. 


To reduce Number of calls Use Binary search Instead of Linear Search
Time Complexity : O(Log(n))
'''
class Solution:
   def firstBadVersion(self, n):
        left,right = 1,n            #Set boundries
        while right > left:          # While array is not empty
            # Search in middle (binary search)
            middle = (left+right)//2
            # If middle is bad, because we know array is sorted and everything to the right of firstbad is also bad, we can search everything under middle by setting right to middle
            if isBadVersion(middle): right = middle
            # Otherwise, we search directly over middle by setting left to middle + 1 (remember it is not middle because we already checked middle)
            else: left = middle + 1
        # Realize that we could return left or right because at this point they are equal (difference is 0)
        return left
