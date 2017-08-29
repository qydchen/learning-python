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

    def reverse_print_ll(self):
        self._reverse_print_ll(self.head)

    def _reverse_print_ll(self, node):
        if node is None:
            return
        else:
            self._reverse_print_ll(node.next)
            print(node.val)

    def iterative_print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.val)
            current_node = current_node.next

    def pop(self):
        if self.head.next is None:
            self.head = None
            return
        else:
            self.head = self.head.next
            return self.head.val

    def push(self, val):
        if self.head is None:
            self.head = Node(val)
            return self.head.val

        current_node = self.head

        while current_node is not None:
            if current_node.next is None:
                current_node.next = Node(val)
                return current_node.next.val
            else:
                current_node = current_node.next

ll = LinkedList()
ll.push("a")
ll.print_ll()
ll.push("b")
ll.print_ll()
