# first we need a node class

class Node:
    def __init__(self, data=None, next =None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("LinkedList is empty!")
            return

        llstr =''
        itr = self.head
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)



cl = LinkedList()
cl.insert_at_begining(8)
cl.insert_at_begining(9)
cl.insert_at_begining(10)
cl.insert_at_begining(11)
cl.print()