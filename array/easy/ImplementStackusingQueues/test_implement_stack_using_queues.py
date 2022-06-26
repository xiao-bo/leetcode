
from implement_stack_using_queues import MyStack


def test_mystack():


    obj = MyStack()
    obj.push(1)
    obj.push(2)

    assert obj.pop() == 2
    assert obj.top() == 1
    assert obj.empty() == False

