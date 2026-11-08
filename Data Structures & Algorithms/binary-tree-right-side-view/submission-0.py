# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None: return res
        queue = collections.deque()
        queue.append(root)
        while queue: 
            right = None
            for i in range(len(queue)): 
                curr = queue.popleft()
                right = curr.val
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            res.append(right)
        return res
