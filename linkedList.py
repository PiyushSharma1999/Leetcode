# Singely linked list

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head =ListNode(-1)
        self.tail = self.head

    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def printLL(self):
        curr = self.head.next
        while curr:
            print(curr.val, " -> ", end="")
            curr = curr.next
        print()


ll = LinkedList()
ll.insertEnd(4)
ll.insertEnd(99)
ll.insertEnd(999)
ll.printLL() 
ll.remove(1)
ll.printLL()
    