class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        """Принимает данные и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        """Принимает данные и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def __str__(self):
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return "None"

        ll_string = ''
        while node:
            ll_string += f"{str(node.data)} -> "
            node = node.next_node

        ll_string += "None"
        return ll_string
