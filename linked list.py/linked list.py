class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


arr = [10, 20, 30, 40]
head = Node(arr[0])
current = head
for i in arr[1:]:
    current.next = Node(i)
    current = current.next
current = head
while current:
    print(current.data)
    current = current.next
