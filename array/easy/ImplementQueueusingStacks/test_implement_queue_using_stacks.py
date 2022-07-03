
from implement_queue_using_stacks import MyQueue

def test_solution():

    obj = MyQueue()
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()

    assert param_2 == 2
    assert param_3 == None
    assert param_4 == True

    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_2 = obj.peek()
    param_3 = obj.pop()
    param_4 = obj.empty()

    assert param_2 == 1
    assert param_3 == 1
    assert param_4 == False