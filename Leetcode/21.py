# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         result = list(0)
#         head = result

#         while list1 and list2:
#             if list1.val <= list2.val:
#                 head.next = list1
#                 list1 = list1.next
#             else:
#                 head.next = list2
#                 list2 = list2.next
#             head = head.next
        
#         if list1:
#             head.next = list1
#         if list2:
#             head.next = list2

#         return result

# demo = Solution()
# value = mergeTwoLists([1,2,4],[1,2,3])
# print(value)
