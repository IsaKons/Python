class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    #get methods
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    #set methods
    def set_data(self, data):
        self.data = data
    
    def set_next(self, next):
        self.next = next

    
class MyLinkedList:

    def __init__(self):
        self.head = None

    def show(self):
        cur_node = self.head
        output = ""
        while cur_node != None:
            output += str(cur_node.get_data()) + " -> "
            cur_node = cur_node.get_next()
        print(output)
    
    def lenght(self):
        cur_node = self.head
        count = 0
        while cur_node != None:
            count += 1
            cur_node = cur_node.get_next()
        return count

    def get(self, index: int) -> int:
        cur_node = self.head
        if cur_node == None or index < 0: return -1
        for x in range(index):
            if cur_node.get_next() == None: return -1
            else: cur_node = cur_node.get_next()
        return cur_node.get_data()

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head = new_node
    
    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.get_next()


    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)
    
    def remove_back(self):
        cur_node = self.head
        while cur_node.get_next().get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        cur_node = self.head
        count = 0
        while cur_node.get_next() != None:
            if index == 0: 
                self.addAtHead()
                return
            elif count + 1 == index:
                the_node_after_cur = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(the_node_after_cur)
                return
            count += 1
            cur_node = cur_node.get_next()
        return print("Index is not in range")

    def deleteAtIndex(self, index: int) -> None:
        cur_node = self.head
        count = 0
        while cur_node.get_next() != None:
            if index == 0:
                self.remove_front()
                return
            elif count + 1 == index:
                the_node_to_remove = cur_node.get_next()
                the_node_after_removed = the_node_to_remove.get_next()
                cur_node.set_next(the_node_after_removed)
            count += 1
            cur_node = cur_node.get_next()
        return print("Index is not in range")
    
    def reverse(self):
        prev = None
        cur_node = self.head
        next = None
        while cur_node != None:
            next = cur_node.get_next()
            cur_node.set_next(prev)
            prev = cur_node
            cur_node = next
        self.head = prev
