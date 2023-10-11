from src.linked_list import LinkedList, Node

def test_node_creation():
    """
    Тестирование создания узла (Node).

    Убеждаемся, что узел создается правильно и его атрибуты задаются корректно.
    """
    data = {'key': 'value'}
    node = Node(data)
    assert node.data == data
    assert node.next_node is None

def test_linked_list_insert_beginning():
    """
    Тестирование вставки узла в начало связанного списка.

    Проверяем, что узел успешно вставляется в начало списка и порядок узлов сохраняется.
    """
    ll = LinkedList()
    data1 = {'id': 0}
    data2 = {'id': 1}
    data3 = {'id': 2}
    data4 = {'id': 3}
    ll.insert_beginning(data1)
    ll.insert_beginning(data2)
    assert str(ll) == "{'id': 1} -> {'id': 0} -> None"

def test_linked_list_insert_at_end():
    """
    Тестирование вставки узла в конец связанного списка.

    Проверяем, что узел успешно вставляется в конец списка и порядок узлов сохраняется.
    """
    ll = LinkedList()
    data1 = {'id': 0}
    data2 = {'id': 1}
    data3 = {'id': 2}
    data4 = {'id': 3}
    ll.insert_at_end(data1)
    ll.insert_at_end(data2)
    assert str(ll) == "{'id': 0} -> {'id': 1} -> None"

def test_linked_list_empty():
    """
    Тестирование пустого связанного списка.

    Убеждаемся, что связанный список без элементов возвращает корректное строковое представление.
    """
    ll = LinkedList()
    assert str(ll) == "None"

def test_linked_list_str_representation():
    """
    Тестирование строкового представления связанного списка.

    Проверяем, что строковое представление связанного списка корректно отображает его содержимое.
    """
    ll = LinkedList()
    data1 = {'id': 0}
    data2 = {'id': 1}
    data3 = {'id': 2}
    data4 = {'id': 3}
    ll.insert_beginning(data1)
    ll.insert_at_end(data2)
    ll.insert_at_end(data3)
    ll.insert_at_end(data4)
    assert str(ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
