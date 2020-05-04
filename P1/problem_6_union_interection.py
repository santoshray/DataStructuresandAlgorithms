class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def linked_list_to_dict(self):
        d = {}
        node  = self.head
        while node:
            val = node.value
            if val in d:
                d[val] +=1
            else:
                d[val] = 1

            node = node.next

        return d


def union(llist_1, llist_2):
    # Your Solution Here
    l1_dict = llist_1.linked_list_to_dict()
    l2_dict = llist_2.linked_list_to_dict()
    l3 = LinkedList()
    
    for k2 in l2_dict.keys():
        if k2 in l1_dict:
            l1_dict[k2] += l2_dict[k2]
        else:
            l1_dict[k2] = l2_dict[k2]

    for k1 in l1_dict.keys():
        i = 0 
        while i < l1_dict[k1]:
            l3.append(k1)
            i+=1

    return l3

def intersection(llist_1, llist_2):
    # Your Solution Here
    l1_dict = llist_1.linked_list_to_dict()
    l2_dict = llist_2.linked_list_to_dict()
    l3_dict = {}
    l3 = LinkedList()

    
    for k2 in l2_dict.keys():
        if k2 in l1_dict:
            l3_dict[k2] = min(l1_dict[k2],l2_dict[k2] )

    for k1 in l3_dict.keys():
        i = 0 
        while i < l3_dict[k1]:
            l3.append(k1)
            i+=1

    return l3


if __name__ == '__main__':

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    linked_list_1.linked_list_to_dict()
    linked_list_2.linked_list_to_dict()

    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

    # Test case 2

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)


    print (union(linked_list_3,linked_list_4))
    print (intersection(linked_list_3,linked_list_4))

    # Test case 3

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = [1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)


    print (union(linked_list_3,linked_list_4))
    print (intersection(linked_list_3,linked_list_4))

    # Test case 4

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)


    print (union(linked_list_3,linked_list_4))
    print (intersection(linked_list_3,linked_list_4))

    # Test case 5  ( disjoint sets)

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [1,1,4,5,6]
    element_2 = [2,3,7,8,7]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4))
    print (intersection(linked_list_3,linked_list_4))


    # Test case 6  ( equal sets)

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [1,1,4,5,6]
    element_2 = [1,1,4,5,6]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)


    print (union(linked_list_3,linked_list_4))
    print (intersection(linked_list_3,linked_list_4))

