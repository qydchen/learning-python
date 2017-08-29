class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, *args):
        self.head = self.create_list(*args)

    def create_list(self, *args):
        last_node = None
        for nval in reversed(args):
            current_node = Node(nval)
            current_node.next = last_node
            last_node = current_node
        return last_node

    def print_ll(self):
        self._print_ll(self.head)

    def _print_ll(self, node):
        if node is None:
            return
        else:
            print(node.val)
            self._print_ll(node.next)

    def iterative_print(self):
        current_node = self.head
        while current_node is not None:
print(current_node.val)                                                                                             ``````````````````````````
current_node = current_node.next             AQAQAAAÃA

ll = LinkedList("a","b","c",'d','e')
# ll.print_ll()
ll.iterative_print()
