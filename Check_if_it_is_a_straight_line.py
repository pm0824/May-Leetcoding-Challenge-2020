'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 
Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
'''

#Solution : If the point makes equal slope with first and second point then its collinear to them. 
            #In the same way by comparing the slope of each point we can find the set of collinear points.
            
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        l=len(coordinates)
        if(l<3):
            return True
        else:
            x1=coordinates[0][0]
            y1=coordinates[0][1]
            x2=coordinates[1][0]
            y2=coordinates[1][1]
            for i in range(2,l):
                if((coordinates[i][1] - y2)*(x2 - x1) != (y2 - y1)*(coordinates[i][0] - x2)):
                    return False
            return True  
