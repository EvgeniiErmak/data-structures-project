import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        # Инициализация очереди перед каждым тестом
        self.queue = Queue()

    def test_init(self):
        # Тестирование метода __init__
        self.assertIsNone(self.queue.head)
        self.assertIsNone(self.queue.tail)

    def test_enqueue(self):
        # Тестирование метода enqueue
        self.queue.enqueue(1)
        self.assertEqual(str(self.queue), "1")

        self.queue.enqueue(2)
        self.assertEqual(str(self.queue), "1\n2")

        self.queue.enqueue(3)
        self.assertEqual(str(self.queue), "1\n2\n3")

    def test_dequeue(self):
        # Тестирование метода dequeue
        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(str(self.queue), "2")

        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(str(self.queue), "")

        # Попытка извлечения из пустой очереди должна вызвать IndexError
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_str(self):
        # Тестирование метода __str__
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(str(self.queue), "1\n2")

        self.queue.dequeue()
        self.assertEqual(str(self.queue), "2")

        self.queue.enqueue(3)
        self.assertEqual(str(self.queue), "2\n3")

if __name__ == '__main__':
    unittest.main()
