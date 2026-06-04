# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        # save left.prev
        ptr = dummy
        for _ in range(left-1):
            ptr = ptr.next
        left_prev = ptr
        # print(left_prev.val)

        # save right.next
        ptr = left_prev
        for _ in range(right-left+2):
            ptr = ptr.next
        right_next = ptr
        # print(right_next.val)

        # 1->2->3->4->5
        # 1  4->3->2  5
        # 1->4->3->2->5

        # reverse 2->3->4
        # left_prev = 1, right_next = 5

        prev = left_prev
        curr = left_prev.next
        first_curr = curr
        # print(first_curr.val)
        while curr.next != right_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # print(curr.val)
        left_prev.next = curr
        curr.next = prev
        first_curr.next = right_next

        if left == 1:
            return curr
        return dummy.next

            
        