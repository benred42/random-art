import random
from math import *
# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


class ExpressionGenerator:
    def __init__(self):
        self.one_arg_functions = ["sin(", "cos(", "sin(pi * ",
                                  "cos(pi * ", "(x * ", "(y * ", "extreme(",
                                  "invert_sign(", "e_pow_log(",
                                  "divide_by_five(", "reciprocal(", "exp("]
# The reciprocal() and exp() functions in the list above sometimes result in
# math range errors since they can cause a result outside the range of -1 to 1
# They can also produce some very striking results, however.
        self.two_arg_functions = ["avg(", "power(", "subtraction(",
                                  "addition(", "multiply("]
        self.starter = ["(x)", "(y)", "(x * y)", "(x * x)", "(y * y)",
                        "(x/2)", "(y/2)", "(sin(x))", "(sin(y))", "(cos(x))",
                        "(cos(y))", "((x + y)/2)", "((x - y)/2)"]

    def generate(self):
        temp_string = random.choice(self.starter)
        length = random.randint(5, 20)
        while length > 0:
            number_args = random.choice([1, 1, 2])
            if number_args == 1:
                random_function = random.choice(self.one_arg_functions)
                temp_string = random_function + temp_string + ")"
                length -= 1
            else:
                random_function = random.choice(self.two_arg_functions)
                temp_string = random_function + random.choice(self.starter) + \
                    ", " + temp_string + ")"
                length -= 1

        self.expression = temp_string

    def evaluate(self, x, y):
        return eval(self.expression)

    def __str__(self):
        return self.expression


def avg(x, y):
    return (x + y)/2


def extreme(x):
    if x < 0:
        x = -1
    else:
        x = 1
    return x


def invert_sign(x):
    return -x


def power(x, y):
    return pow(abs(x), abs(y))


def minimize(x):
    if x > 0.25:
        x = .1
    else:
        x = -.1
    return x


def e_pow_log(x):
    if x != 0:
        return exp(log(abs(x)))
    else:
        return x


def subtraction(x, y):
    return (x - y)/2


def addition(x, y):
    return (x + y)/2


def divide_by_five(x):
    return x/5


def reciprocal(x):
    if x != 0:
        return 1/x
    else:
        return x


def multiply(x, y):
    return x * y


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    gen = ExpressionGenerator()
    gen.generate()
    return gen


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr.evaluate(x, y)
