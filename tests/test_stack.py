import unittest
from src.stack import Node, Stack

class TestStack(unittest.TestCase):


    def test_node_creation(self):
        n1 = Node(5, None)
        self.assertEqual(n1.data, 5)
        self.assertIsNone(n1.next_node)

        n2 = Node('a', n1)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n2.next_node, n1)


    def test_stack_push(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.top.data, 'data1')

        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')

        stack.push('data3')
        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')


    def test_stack_pop(self):
        stack = Stack()
        with self.assertRaises(ValueError):
            stack.pop()

        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        data = stack.pop()
        self.assertEqual(data, 'data3')
        self.assertEqual(stack.top.data, 'data2')

        data = stack.pop()
        self.assertEqual(data, 'data2')
        self.assertEqual(stack.top.data, 'data1')

        data = stack.pop()
        self.assertEqual(data, 'data1')
        self.assertIsNone(stack.top)

if __name__ == '__main__':
    unittest.main()
