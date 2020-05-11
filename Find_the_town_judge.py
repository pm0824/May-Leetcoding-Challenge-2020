'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
1.The town judge trusts nobody.
2.Everybody (except for the town judge) trusts the town judge.
3.There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:
Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 2:
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 3:
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 
Note:
1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
'''
#Solution 1: By claculating indegree and outdegree of directed graph

def findJudge(self, N, trust):
        d = [0] * (N + 1)
        for i, j in trust:
            d[i] -= 1
            d[j] += 1
        for i in range(1, N + 1):
            if d[i] == N - 1:
                return i
        return -1
        
#Solution 2: Using set...more efficient

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            return 1

        trusters={t[0] for t in trust}
        trustedCount = Counter([t[1] for t in trust])
        judgeset = trustedCount.keys() - trusters
        if len(judgeset) == 0:
            return -1
        judge = judgeset.pop()
        if trustedCount[judge] == N-1:
            return judge
        return -1
        
        
        



