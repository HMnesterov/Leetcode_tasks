# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        count = 0
        if not head:
            return
        if not head.next:
            return head
        all_of_nodes = []
        new_head = head
        times_out = []
        while new_head:
            count += 1
            times_out.append(new_head)
            new_head = new_head.next
            if count % k == 0:
                all_of_nodes.extend(times_out[::-1])
                times_out = []
        else:
            if times_out:
                all_of_nodes.extend(times_out)
        new_link = all_of_nodes[0]
        new_link.next = None
        helper = new_link
        del all_of_nodes[0]
        while all_of_nodes:
            link = all_of_nodes[0]
            link.next = None
            del all_of_nodes[0]
            helper.next = link
            helper = helper.next
        return new_link

"""TESTS:
1)Runtime 96 ms
Beats 58.98%
Memory 15.4 MB
Beats 12.2%
"""