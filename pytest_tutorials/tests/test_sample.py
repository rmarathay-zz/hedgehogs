#test_1
"""
function func returns x + 1
parameters: x is an int 
requires x to be an int
"""
def func(x):
    return x + 1

"""
function test_answer tests func

"""
def test_answer():
    # this assert should pass.
    assert func(3) == 4
    
    # this assert should fail.
    # x is not an int
    assert func("hi") == 4

def test_answer_again():
    # this assert should fail. 
    assert func(3) == 5