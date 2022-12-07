# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        values = []
        dtf = head
        while dtf:
            values.append(dtf)
            dtf = dtf.next

        for c in values:
            c.next = None

        values = sorted(values, key=lambda val: val.val)

        link = values[0]
        del values[0]

        key = link
        for s in values:
            key.next = s
            key = key.next
        return link


"""TESTS:
1)Runtime 479 ms
Beats 92.63%
Memory 36.4 MB
Beats 54.74%


2)Runtime 804 ms
Beats 71.97%
Memory 36.4 MB
Beats 54.74%
"""
