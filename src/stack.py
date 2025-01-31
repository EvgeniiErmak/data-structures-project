class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :param next_node: ссылка на следующий узел, по умолчанию None
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента или None, если стек пуст
        """
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next_node
        return data

    def __str__(self):
        """
        Метод для представления стека в виде строки

        :return: строковое представление стека
        """
        current = self.top
        stack_str = ""
        while current:
            stack_str += str(current.data) + " "
            current = current.next_node
        return stack_str.rstrip()  # Удаляем лишний пробел в конце строки
