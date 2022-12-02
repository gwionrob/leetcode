"""https://leetcode.com/problems/add-two-numbers/"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_val = l1.val
        l2_val = l2.val
