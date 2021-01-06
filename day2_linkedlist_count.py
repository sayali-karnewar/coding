class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def countNodes(head):
    count = 1
    while head.next != None:
        count = count+1
        head = head.next
    
    return (count)


A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)

A.next = B
B.next = C
C.next = D

print(countNodes(A))