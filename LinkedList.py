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
        count = 0
        while cur_node != None:
            if count == index:
                return cur_node.get_data()
            cur_node = cur_node.get_next()
            count += 1
        return -1

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

        if index < 0: index = 0
        if index == 0:
            self.addAtHead(val)
            return

        if self.lenght() == index:
            self.addAtTail(val)
            return
        
        if cur_node == None:
            return -1

        while cur_node.get_next() != None:
            if count + 1 == index:
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

        if cur_node == None:
            return print("Index is not in range")

        if index == 0:
            self.remove_front()
            return
        
        while cur_node.get_next() != None:
            if count + 1 == index:
                the_node_to_remove = cur_node.get_next()
                the_node_after_removed = the_node_to_remove.get_next()
                cur_node.set_next(the_node_after_removed)
                return
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


my_list = MyLinkedList()

my_list.addAtHead(1)
my_list.addAtTail(2)
my_list.addAtTail(3)
my_list.addAtIndex(1,5)
my_list.lenght()
my_list.show()
my_list.get(3)
my_list.remove_back()
my_list.show()
my_list.remove_front()
my_list.show()
my_list.deleteAtIndex(1)
my_list.reverse()