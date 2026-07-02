class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:

            if current.val == current.next.val:
                current.next = current.next.next #GUys, This part removes the duplicate [for info.]
            else:
                current = current.next

        return head