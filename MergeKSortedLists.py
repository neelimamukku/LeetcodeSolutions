# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq as hp

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        hp.heapify(h)
        for i in lists:
            temp = i
            while temp != None:
                hp.heappush(h,temp.val)
                temp = temp.next
        if h == []:
            return None
        res = ListNode(hp.heappop(h),None)
        prev = res
        while h != []:
            temp = ListNode(hp.heappop(h),None)  
            prev.next = temp
            prev = temp
        return res
