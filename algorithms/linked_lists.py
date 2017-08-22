class Node:
    def __init__(self, node_data=None, link=None):
        self.data = node_data
        self.next = link


class LinkedList:
    def __init__(self, head_node=None):
        self.head = head_node
        self.current_node = self.head
        self.previous_node = None

    def remove_node(self, node):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.data == node.data:
                if self.previous_node:
                    self.previous_node.next = self.current_node.next
                    self.current_node = self.current_node.next
                else:
                    self.head = self.current_node.next
                    self.current_node = self.current_node.next
            else:
                self.previous_node = self.current_node
                self.current_node = self.current_node.next

    def add_node(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def print_links(self):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.next is None:
                print('{} -->'.format(self.current_node.data))
            else:
                print('{} --> {}'.format(self.current_node.data, self.current_node.next.data))
            self.current_node = self.current_node.next


if __name__ == '__main__':

    linked_list = LinkedList()
    node_list = [Node(c) for c in ['A', 'B', 'C']]

    for node in node_list:
        linked_list.add_node(node)

    linked_list.print_links()
    print('Removing')
    linked_list.remove_node(linked_list.head.next.next)
    linked_list.print_links()




