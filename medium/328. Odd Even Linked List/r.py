# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        chet = []
        nechet = []
        count = 0
        guy = head
        if not head:
            return
        if head and not head.next:
            return head
        while head:
            count += 1
            if count % 2 == 0:
                chet.append(head)
            else:
                nechet.append(head)
            head = head.next

        lead = nechet.pop(0)
        lead.next = None

        fake_lead = lead

        while nechet:
            new_order = nechet.pop(0)
            new_order.next = None
            fake_lead.next = new_order
            fake_lead = fake_lead.next

        while chet:
            new_order = chet.pop(0)
            new_order.next = None
            fake_lead.next = new_order
            fake_lead = fake_lead.next

        return lead


"""Runtime
54 ms
Beats
80.51%
Memory
16.8 MB"""
