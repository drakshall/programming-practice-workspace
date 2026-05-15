class Node:
    next = None
    data = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)
    
class LinkedList:
    head = None

    def add(self, data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def __repr__(self):
        s = []
        n = self.head
        while n:
            s.append(str(n))
            n = n.next
        return " -> ".join(s)

days = LinkedList()
days.add("Monday")
days.add("Tuesday")
days.add("Wednesday")
days.add("Thursday")
days.add("Friday")
days.add("Saturday")
days.add("Sunday")
print(days)