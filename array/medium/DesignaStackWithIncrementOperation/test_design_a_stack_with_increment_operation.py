from design_a_stack_with_increment_operation import CustomStack

def test_custom_stack():

    # 檢驗maxSize是否在滿的狀況下，不會在push新的資料

    maxSize = 2
    obj = CustomStack(maxSize)
    obj.push(1)
    obj.push(2)
    obj.push(3)
    param_2 = obj.pop()

    assert param_2 == 2

    # 檢驗push和pop是否正常發揮
    maxSize = 2
    obj = CustomStack(maxSize)
    obj.push(1)
    obj.push(3)
    param_2 = obj.pop()

    assert param_2 == 3

    # 檢驗空stack時，要pop -1
    maxSize = 2
    obj = CustomStack(maxSize)
    param_2 = obj.pop()

    assert param_2 == -1

    # 檢測increment
    maxSize = 3
    obj = CustomStack(maxSize)
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.increment(1,100)
    param_2 = obj.pop()
    assert param_2 == 3
    param_2 = obj.pop()
    assert param_2 == 2
    param_2 = obj.pop()
    assert param_2 == 101

def test_custom_stack_by_offical_data():
    # 使用官方測資
    # ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
    # [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]

    obj = CustomStack(3)
    obj.push(1)
    obj.push(2)

    assert obj.pop() == 2

    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.increment(5,100)
    obj.increment(2,100)

    assert obj.pop() == 103
    assert obj.pop() == 202
    assert obj.pop() == 201
    assert obj.pop() == -1







