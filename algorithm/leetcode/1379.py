# Definition for a binary tree node.
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        que=deque()
        que.append(cloned)
        while len(que) != 0 and que[-1].val != target.val:
            top=que.popleft()
            if top.left != None : 
                if top.left.val == target.val : 
                    return top.left
                else : que.append(top.left)
            if top.right != None : 
                if top.right.val == target.val : 
                    return top.right
                else : que.append(top.right)
        return que[-1]