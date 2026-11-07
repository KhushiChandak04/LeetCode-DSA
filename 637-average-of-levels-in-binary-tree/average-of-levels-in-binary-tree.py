# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        q = deque([root]) #initilise a double ended queue and add root to it
        ans = []

        while q: #till the end of this double ended q
            total = 0
            size = len(q) #counts nodes at current level

            for i in range(size): #process all nodes at taht level
                node = q.popleft() #remove the first node
                total += node.val

                if node.left: #add left child to the queue, recursion used here
                    q.append(node.left)
                if node.right: #similarly add the right one here
                    q.append(node.right)
            
            ans.append(total/float(size)) #as the ans needs to be in floating pt decimal
        return ans