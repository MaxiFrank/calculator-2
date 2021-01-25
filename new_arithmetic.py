"""Functions for common math operations."""

def add(ls):
    sum = 0
    for num in ls:
        sum = sum + num
    return sum


def subtract(ls):
    diff = 0
    for num in ls:
        diff = num - diff
    return diff

# def multiply(num1, num2):
def multiply(ls):
    """Multiply the two inputs together."""
    result = 1
    for num in ls:
        result = result * num 
    return result



def divide(ls):
    """Divide the first input by the second and return the result."""
    result = 1
    for num in ls:
        result = num / result
    return result

def square(num1):
    # doesn't make sense to have a list
    """Return the square of the input."""

    return num1 * num1


def cube(num1):
    # doesn't make sense to have a list
    """Return the cube of the input."""

    return num1 * num1 * num1


def power(ls):
    """Raise num1 to the power of num2 and return the value."""
    result = ls[0]
    for num in ls[1:]:
        result = result ** num
    return result  # ** = exponent operator

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    result = None
    for num in ls:
        result = result %num
    return result


def add_mult(num1, num2, num3):
    """Add num1 and num2 and multiply sum by num3."""
    # uncertain about how this one works. for for example ([1, 2, 3, 4])
    return multiply(add(num1, num2), num3)


def add_cubes(ls):
    """Cube num1 and num2 and return the sum of these cubes."""
    sum = 0
    for num in ls:
        sum = sum + cube(num)
    return sum

print(divide([2,4,2]))