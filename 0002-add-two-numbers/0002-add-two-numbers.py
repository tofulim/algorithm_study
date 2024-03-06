# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_listnode = self.node2int(l1) + self.node2int(l2)
        
        return self.int2node(sum_listnode)
    
    def node2int(self, listnode: ListNode):
        arr = []
        while listnode is not None:
            arr.append(str(listnode.val))    
            listnode = listnode.next

        return int(''.join(arr[::-1]))

    def int2node(self, number: int) -> Optional[ListNode]:
        # reverse
        reversed_num = str(number)[::-1]

        start_node = ListNode(reversed_num[0]) 
        curr_node = start_node

        for idx, num in enumerate(reversed_num):
            if idx == 0:
                continue
            new_node = ListNode(num)
            curr_node.next = new_node
            curr_node = new_node
        
        return start_node
            