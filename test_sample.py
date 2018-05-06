import pytest

@pytest.fixture(scope='module')
def a():
    a=30
    yield a


@pytest.fixture(scope='module')
def b():
    b=10
    yield b

def test_add(a,b):
    print('addition is :'+str(a+b))

def test_sub(a, b):
    print('Subtraction is :'+str(a-b))

def test_mul(a, b):
    print('mul is :'+str(a*b))

def test_div(a, b):
    print('Division is :'+str(a/b))


