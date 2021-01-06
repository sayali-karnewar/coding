class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node


A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)

A.next = B
B.next = C
C.next = D

print(A.data,"->", B.data,"->",C.data,"->",D.data)