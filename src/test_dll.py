"""Test double linked list class."""
import pytest


@pytest.fixture
def dll():
    """Instantiate a dll for testing."""
    from dll import DoubleLinkedList
    double_link = DoubleLinkedList()
    return double_link


def test_dll_initialization(dll):
    """Test that there's nothing initialized."""
    assert dll.tail == None
    assert dll.head == None


def test_dll_push_raises_type_error(dll):
    """Test that the value error  is raised."""
    with pytest.raises(TypeError):
        dll.push()


def test_dll_push_pushes_value(dll):
    """Test that the push pushes a value to head of list."""
    dll.push(1)
    assert dll.tail.data == 1
    assert dll.head.data == 1

def test_dll_push_head_and_tail_change(dll):
    """Test that if second item is pushed in head and tail are seperate values."""
    dll.push(1)
    dll.push(2)
    assert dll.tail.data == 1
    assert dll.head.data == 2

def test_dll_push_3(dll):
    """Test that if 3 vals are pushed there is a head, prior node and tail."""
    dll.push(1)
    dll.push(2)
    dll.push(3)
    assert dll.tail.data == 1
    assert dll.head.prior_node.prior_node.data == 1
    assert dll.head != dll.head.prior_node
    assert dll.head.data == 3
    assert dll.head.prior_node.next_node.data == 3
    assert dll.tail.next_node.data == 2 

def test_dll_pop_Index_Error(dll):
    """Testing that the Index Error is raised if no val is popped."""
    with pytest.raises(IndexError):
        dll.pop()


def test_dll_pop_only_has_one_item(dll):
    """Testing that pop only has one item and both are head and tail none vals."""
    dll.push(1)
    dll.push(2)
    assert dll.pop() == 2 
    assert dll.head.data == 1 
    assert dll.tail.data == 1 
    assert dll.head.next_node == None 
    assert dll.pop() == 1
    assert dll.head == None
    assert dll.tail == None


def test_dll_append_raises_type_error(dll):
    with pytest.raises(TypeError):
        dll.append()


def test_dll_appends_a_value(dll):
    dll.append(1)
    assert dll.tail.data == 1 
    assert dll.head.data == 1 

def test_dll_appends_3_values(dll):
    dll.append(1)
    dll.append(2)
    dll.append(3)
    assert dll.tail.data == 3
    assert dll.head.data == 1
    assert dll.head.next_node == None
    assert dll.tail.prior_node == None
    assert dll.tail.next_node.data == 2 
    assert dll.head.prior_node.data == 2
    assert dll.head.prior_node.next_node.data == 1
    assert dll.tail.next_node.prior_node.data == 3 

