# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        answer=[]
        inOrder(root,answer)
        return answer
        
        
def inOrder(node, answer):
    if node==None : return
    inOrder(node.left,answer)
    answer.append(node.val)
    inOrder(node.right,answer)
    