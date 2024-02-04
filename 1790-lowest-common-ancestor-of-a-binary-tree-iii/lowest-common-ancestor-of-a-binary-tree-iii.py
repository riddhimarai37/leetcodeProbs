"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""



class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_ptr = p
        q_ptr = q

        while p_ptr != q_ptr:
            if p_ptr.parent:
                p_ptr = p_ptr.parent
            else:
                p_ptr = q

            if q_ptr.parent:
                q_ptr = q_ptr.parent
            else:
                q_ptr = p

        return p_ptr























        # p_ptr = p
        # q_ptr = q

        # while p_ptr != q_ptr:
        #     if p_ptr:
        #         p_ptr = p_ptr.parent
        #     else: 
        #         p_ptr = q
        #     if q_ptr:
        #         q_ptr = q_ptr.parent
        #     else:
        #         q_ptr = p
        
        # return p_ptr

        # O(N) Time; O(1) Space

        # Explanation: we need to eventually reach the shared lowest common ancestor
        # if q and p are separate distances away from the lca, if we continue going up the tree
        # and swap pointers when reaching null; we eventually reach a point where the pointers 
        # converge and the parents equal each other; giving us the lca
        




        


        