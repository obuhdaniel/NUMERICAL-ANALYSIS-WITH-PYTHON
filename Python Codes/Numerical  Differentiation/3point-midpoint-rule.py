def myFunction(x):
    """
    This function calculates the square of a given number.

    Parameters:
    x (int or float): The number to be squared.

    Returns:
    int or float: The square of the input number.
    """
    return x ** 2


def numerical_differentiation(x, h):
    """
    This function calculates the numerical derivative of a given function at a specific point using the 3-point midpoint rule.

    Parameters:
    x (int or float): The point at which the derivative is to be calculated.
    h (int or float): The step size for the numerical differentiation.

    Returns:
    int or float: The numerical derivative of the function at the given point.
    """
    return (1/(2 * h)) * ((myFunction( x - (2 *h))) - (myFunction( x- h)))


if __name__ == "__main__":
    x = 2
    h = 1
    derivative = numerical_differentiation(x, h)
    print(derivative)