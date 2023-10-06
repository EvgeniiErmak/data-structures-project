import unittest
from src.stack import Node, Stack

class TestNode(unittest.TestCase):

    def test_node_creation(self):
        data = 42
        node = Node(data)
        self.assertEqual(node.data, data)
        self.assertIsNone(node.next_node)

    def test_node_with_next_node(self):
        data1 = 42
        data2 = 23
        node1 = Node(data1)
        node2 = Node(data2, node1)
        self.assertEqual(node2.data, data2)
        self.assertEqual(node2.next_node, node1)

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_stack_push_pop(self):
        self.stack.push(42)
        self.stack.push(23)
        self.assertEqual(self.stack.pop(), 23)
        self.assertEqual(self.stack.pop(), 42)

    def test_stack_pop_empty(self):
        self.assertIsNone(self.stack.pop())

    def test_stack_push_pop_multiple(self):
        data = [1, 2, 3, 4, 5]
        for item in data:
            self.stack.push(item)
        for item in reversed(data):
            self.assertEqual(self.stack.pop(), item)

if __name__ == '__main__':
    unittest.main()
