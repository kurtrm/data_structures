"""
The priority queue is going to look almost exactly like the binary heap.
We can use the same logic, but we'll have to put each piece
of data into a node object so it can have two attributes, data
and priority. Priority will be set to zero by default, and the
normal way of organizing the heap will prevail. In this case,
it will not take an heap for initialization; it will be
initialized as an empty priority queue.
"""
import pytest


@pytest.fixture
def priority_queue():
    """Priority queue for use in test."""
    from priorityq import PriorityQueue
    priority_queue = PriorityQueue()
    return priority_queue


@pytest.fixture
def priority_queue_full():
    """Priority queue for use in test."""
    from priorityq import PriorityQueue
    priority_queue = PriorityQueue()
    priority_queue.insert(15, 5)
    priority_queue.insert(12, 3)
    priority_queue.insert(11, 1)
    priority_queue.insert(6, 2)
    priority_queue.insert(17)
    priority_queue.insert(3)
    return priority_queue


def test_priority_que_init():
    """Make sure they don't provide any arguments."""
    from priorityq import PriorityQueue
    with pytest.raises(TypeError):
        new_pqueue = PriorityQueue(1)


def test_priority_que_type_arguments_negative(priority_queue):
    """Make sure they cannot give priority <= 1."""
    with pytest.raises(ValueError):
        priority_queue.insert(3, -99)


def test_priority_que_type_arguments_a(priority_queue):
    """Make sure they only give priority >= 1."""
    with pytest.raises(TypeError):
        priority_queue.insert(3, 'a')


# def test_priority_que_type_arguments_negative(priority_queue):
#     """Make sure they only give priority >= 1."""
#     with pytest.raises(ValueError):
#         priority_queue.insert(3, -2)



def test_priority_que_type_arguments_none(priority_queue):
    """Make sure an argument is give."""
    with pytest.raises(TypeError):
        priority_queue.insert()


# def test_priority_que_type_arguments(priority_queue):
#     """For now, ensure data type is integer."""
#     with pytest.raises(TypeError):
#         priority_queue.insert('a', 1)


# def test_priority_que_type_arguments_list(priority_queue):
#     """For now, ensure data type is integer."""
#     with pytest.raises(TypeError):
#         priority_queue.insert([1], 1)


def test_priority_que_type_arguments_float(priority_queue):
    """For now, ensure data type is integer."""
    with pytest.raises(TypeError):
        priority_queue.insert(1.5, 3)


def test_priority_que_success(priority_queue):
    """Ensure it takes the correct arguments."""
    priority_queue.insert(15)
    assert list(priority_queue._heap[0].keys())[0] == 15
    assert list(priority_queue._heap[0].values())[0] == 0


def test_priority_que_success_multiple(priority_queue_full):
    """Ensure it takes the correct arguments."""
    assert list(priority_queue_full._heap[0].keys())[0] == 11
    assert list(priority_queue_full._heap[-1].keys())[0] == 3


def test_priority_que_success_multiple_empty(priority_queue):
    """Ensure it takes the correct arguments."""
    priority_queue.insert(15)
    priority_queue.insert(13, 1)
    assert list(priority_queue._heap[0].keys())[0] == 13
    assert list(priority_queue._heap[0].values())[0] == 1
    assert list(priority_queue._heap[1].keys())[0] == 15


def test_priority_que_success_min_no_priority(priority_queue):
    """Ensure it orders by min if no priority provided."""
    priority_queue.insert(10)
    priority_queue.insert(5)
    priority_queue.insert(100)
    assert list(priority_queue._heap[0].keys())[0] == 5


def test_priority_que_success_priority(priority_queue):
    """Ensure it orders by precedence if same."""
    priority_queue.insert(10)
    priority_queue.insert(5)
    priority_queue.insert(100, 1)
    priority_queue.insert(10, 1)
    assert list(priority_queue._heap[0].keys())[0] == 100


def test_priority_que_success_priority_multiple(priority_queue):
    """Ensure it orders by priority with different priorities."""
    priority_queue.insert(10)
    priority_queue.insert(5)
    priority_queue.insert(100, 5)
    priority_queue.insert(10, 2)
    priority_queue.insert(50, 1)
    assert list(priority_queue._heap[0].keys())[0] == 50
    assert list(priority_queue._heap[1].keys())[0] == 10
    assert list(priority_queue._heap[2].keys())[0] == 5


# def test_priority_que_failure_pop(priority_queue):
#     """Ensure it does not allow popping from empty priority queue."""
#     with pytest.raises(IndexError):
#         priority_queue.pop()



def test_priority_que_pop(priority_queue_full):
    """Ensure pop is working as expected."""
    assert priority_queue_full.pop() == 11
    assert priority_queue_full.pop() == 6
    assert priority_queue_full.pop() == 12
    assert priority_queue_full.pop() == 15
    assert priority_queue_full.pop() == 3
    assert priority_queue_full.pop() == 17


# def test_priority_que_peek(priority_queue_full):
#     """Ensure we can peek at the correct value."""
#     assert priority_queue_full.peek() == 11



def test_priority_que_pop_and_push(priority_queue_full):
    """Ensure successful interaction between pop and push."""
    priority_queue_full.pop()
    priority_queue_full.insert(11, 1)
    assert list(priority_queue_full._heap[0].values())[0] == 1
    priority_queue_full.pop()
    priority_queue_full.pop()
    priority_queue_full.insert(10, 1)
    assert priority_queue_full.peek() == 10
