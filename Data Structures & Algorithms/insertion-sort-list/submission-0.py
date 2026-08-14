class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node helps us handle insertion at head
        dummy = ListNode(0)
        dummy.next = None
        
        current = head
        
        while current:
            # Save next node before we modify current.next
            next_node = current.next
            
            # Find correct position to insert current node
            pos = dummy
            while pos.next and pos.next.val < current.val:
                pos = pos.next
            
            # Insert current node at correct position
            current.next = pos.next
            pos.next = current
            
            # Move to next unsorted node
            current = next_node
        
        return dummy.next