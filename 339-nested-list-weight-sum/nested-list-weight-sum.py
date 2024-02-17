# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


# ex: [[1,1], 2, [1,1]]

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nested_list, depth):
            total_sum = 0
            for val in nested_list:
                if val.isInteger():
                    total_sum += val.getInteger() * depth
                else:
                    total_sum += dfs(val.getList(), depth + 1)
            return total_sum

        return dfs(nestedList, 1)




        # def dfs(cur_list, depth):
        #     curr_sum = 0

        #     for cur in cur_list:
        #         if cur.isInteger():
        #             curr_sum += cur.getInteger() * depth
        #         else:
        #             curr_sum += dfs(cur.getList(), depth + 1)
        #     return curr_sum

        # return dfs(nestedList, 1)






















        # def dfs(nested_list, depth):
        #     res = 0
        #     for cur in nested_list:
        #         if cur.isInteger():
        #             res += cur.getInteger() * depth
        #         else:
        #             res += dfs(cur.getList(), depth+1)
        #     return res

        # return dfs(nestedList, 1)

        # TIME = O(N) SPACE O(N)

        