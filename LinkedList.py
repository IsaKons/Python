# No code for that here, just to remember idea of loop inside linkedlist.
# 1-2-3-4-5-6-7-8-9->4. - it is our linked list with loop on 4.
# 1--x--4----y-7--z-->

# So x its the path till loop start.
# y - its the path, where cur_node will make, before meet node2.
# z - it is path from meet point till end of loop.

# cur_node will make x+y path and then meet node2
# node2 will make x+y+z+y path, before meet cur_node
# In reason that for node2 we have next.next - double speed.

# All educated people also know, that time = distance / speed
# if time is the same, and we know distance, and we know speed, then -
# x+y / 1 = x+y+z+y / 2, so we have x = z

# Then, we need to create node3, in moment of meet node2 and cur_node. And in the moment when cur_node finishes full
# loop, node3 will be on the same place. cur_node will complete Z path, and node3 will complete X path. ##### No code
# here for that!!

# Create a dict of Nodex: CopyNodeX, and then copy all parameters
if head is None: return None
mapping = {}
cur = head
while cur:
    mapping[cur] = Node(cur.val, None, None)
    cur = cur.next
cur = head
while cur:
    if cur.next:
        mapping[cur].next = mapping[cur.next]
    if cur.random:
        mapping[cur].random = mapping[cur.random]
    cur = cur.next
return mapping[head]

# If need to find connection of two different lists
headB = "head of list1"
headA = "head of list2"
while one != two:
    one = headB if one is None else one.next
    two = headA if two is None else two.next
    print(one)

# Check if it is palindrome, 2 pointers and reverse second part.
head = "YUE LINKED LIST"
if not head:
    print(True)

cur_node = sec_node = head
while sec_node and sec_node.next:
    cur_node = cur_node.next
    sec_node = sec_node.next.next

past = None
while cur_node:
    current = cur_node
    cur_node = cur_node.next
    current.next = past
    past = current

while past:
    if past.val != head.val:
        print(False)
    past = past.next
    head = head.next
print(True)


# Main part of created
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # get methods
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    # set methods
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
        while cur_node is not None:
            output += str(cur_node.get_data()) + " -> "
            cur_node = cur_node.get_next()
        print(output)

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.get_next()
        return count

    def get(self, index: int) -> int:
        cur_node = self.head
        if cur_node is None or index < 0: return -1
        count = 0
        while cur_node is not None:
            if count == index:
                return cur_node.get_data()
            cur_node = cur_node.get_next()
            count += 1
        return -1

    def add_at_head(self, val: int) -> None:
        new_node = Node(val)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head = new_node

    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.get_next()

    def add_at_tail(self, val: int) -> None:
        new_node = Node(val)
        cur_node = self.head
        if cur_node is None:
            self.head = new_node
            return
        while cur_node.get_next() is not None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def remove_back(self):
        cur_node = self.head
        while cur_node.get_next().get_next() is not None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)

    def addAtIndex(self, index: int, val: int) -> int | None:
        new_node = Node(val)
        cur_node = self.head
        count = 0

        if index < 0:
            index = 0
        if index == 0:
            self.add_at_head(val)
            return

        if self.length() == index:
            self.add_at_tail(val)
            return

        if cur_node is None:
            return -1

        while cur_node.get_next() is not None:
            if count + 1 == index:
                the_node_after_cur = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(the_node_after_cur)
                return
            count += 1
            cur_node = cur_node.get_next()
        return print("Index is not in range")

    def delete_at_index(self, index: int) -> None:
        cur_node = self.head
        count = 0

        if cur_node is None:
            return print("Index is not in range")

        if index == 0:
            self.remove_front()
            return

        while cur_node.get_next() is not None:
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
        next_node = None
        while cur_node is not None:
            next_node = cur_node.get_next()
            cur_node.set_next(prev)
            prev = cur_node
            cur_node = next_node
        self.head = prev


# To merge 2 sorted lists
list1 = MyLinkedList()
list2 = MyLinkedList()

list1.add_at_head(2)
list1.add_at_tail(2)
list1.add_at_tail(4)

list2.add_at_head(1)
list2.add_at_tail(3)
list2.add_at_tail(4)

l1_node = list1.head
l2_node = list2.head
list3 = MyLinkedList()
l3_node = Node(-1)
list3.head = l3_node

while l1_node and l2_node:
    if l1_node.val < l2_node.val:
        l3_node.next = l1_node
        l1_node = l1_node.next
    else:
        l3_node.next = l2_node
        l2_node = l2_node.next
    l3_node = l3_node.next

if not l1_node:
    l3_node.next = l2_node
elif not l2_node:
    l3_node.next = l1_node

print(list1.show())
print(list2.show())
print(list3.show())
