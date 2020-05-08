'''

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

'''
#Solution : 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        print("root",root)
        treeDict = {}
        tree = [(root, 0, 0)]           #list with tuple having node, parent and depth
        print("first tree",tree)
        while tree:
            node, parent, depth = tree.pop(0)
            print("node",node)
            if node is not None:
                treeDict[node.val] = (parent, depth) 
                print("treedict",treeDict)
                tree.append((node.left, node.val, depth+1))
                tree.append((node.right, node.val, depth+1))
                print("tree", tree)
          
        #checking in dict whether parents are different and level is same   
        return treeDict[x][1] == treeDict[y][1] and treeDict[x][0] != treeDict[y][0]
        
'''
Stdout
root TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: None}, right: TreeNode{val: 3, left: None, right: None}}
first tree [(TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: None}, right: TreeNode{val: 3, left: None, right: None}}, 0, 0)]
node TreeNode{val: 1, left: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: None}, right: TreeNode{val: 3, left: None, right: None}}
treedict {1: (0, 0)}
tree [(TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: None}, 1, 1), (TreeNode{val: 3, left: None, right: None}, 1, 1)]
node TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: None}
treedict {1: (0, 0), 2: (1, 1)}
tree [(TreeNode{val: 3, left: None, right: None}, 1, 1), (TreeNode{val: 4, left: None, right: None}, 2, 2), (None, 2, 2)]
node TreeNode{val: 3, left: None, right: None}
treedict {1: (0, 0), 2: (1, 1), 3: (1, 1)}
tree [(TreeNode{val: 4, left: None, right: None}, 2, 2), (None, 2, 2), (None, 3, 2), (None, 3, 2)]
node TreeNode{val: 4, left: None, right: None}
treedict {1: (0, 0), 2: (1, 1), 3: (1, 1), 4: (2, 2)}
tree [(None, 2, 2), (None, 3, 2), (None, 3, 2), (None, 4, 3), (None, 4, 3)]
node None
node None
node None
node None
node None
'''
 
        
