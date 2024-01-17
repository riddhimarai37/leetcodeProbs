# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeLists(self,list1,list2):
            if not list1 and not list2: return None
            elif not list1 and list2: return list2
            elif not list2 and list1: return list1

            dummy = start = ListNode(0,None)
            dummy.next = start

            while list1 and list2:
                if list1.val < list2.val:
                    start.next = list1
                    list1 = list1.next
                else:
                    start.next = list2
                    list2 = list2.next
                start = start.next

            if list1: 
                start.next = list1
            elif list2:
                start.next = list2

            return dummy.next



        if len(lists) == 0: 
            return None
        
        if len(lists) == 1:
            return lists[0]

        i = 1
        res = lists[0]

        while i < len(lists):
            # merge the two sorted lists 
            res = mergeLists(self, res, lists[i])
            i += 1

        return res

            
        