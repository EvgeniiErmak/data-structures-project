import unittest
from src.stack import Node, Stack

class TestNode(unittest.TestCase):
    def test_node_creation(self):
        node = Node(5)
        self.assertEqual(node.data, 5)
        self.assertIsNone(node.next_node)

    def test_node_with_next_node(self):
        next_node = Node(10)
        node = Node(5, next_node)
        self.assertEqual(node.data, 5)
        self.assertEqual(node.next_node, next_node)

class TestStack(unittest.TestCase):
    def test_stack_creation(self):
        stack = Stack()
        self.assertIsNone(stack.top)

    def test_push_and_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertIsNone(stack.pop())

    def test_str_method(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(str(stack), "3 2 1")

if __name__ == '__main__':
    unittest.main()
