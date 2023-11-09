#/usr/bin/python3

# a function that says hello
def say_hello():
    print("Hello, World!")

# a unit test function for say_hello
def test_say_hello():
    assert say_hello() == "Hello, World!"

# a function that returns the max of 2 numbers
def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

# a unit test function for max_of_two
def test_max_of_two():
    assert max_of_two(3, 4) == 4
    assert max_of_two(0, 0) == 0
    assert max_of_two(-5, 2) == 2

# a function that returns the max of 3 numbers

def max_of_three(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z
