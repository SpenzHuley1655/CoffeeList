def myfunc(x):
    return 2*x

def test_func():
    assert myfunc(2) == 4
    assert myfunc(3) == 6
    
test_func()