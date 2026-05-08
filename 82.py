# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        current = head
        
        while current:
            # Check if current node is duplicate
            if current.next and current.val == current.next.val:
                
                # Skip all nodes with same value
                while current.next and current.val == current.next.val:
                    current = current.next
                
                # Remove duplicates completely
                prev.next = current.next
            
            else:
                prev = prev.next
            
            current = current.next
        
        return dummy.next