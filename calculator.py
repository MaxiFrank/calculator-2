"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    input_ = input()
    tokenized_input = input_.split(' ')
    if tokenized_input[0] == 'q':
        break
    else:
        if tokenized_input[0] == '+':
            return add(tokenized_input[1], tokenized_input[2])
        if tokenized_input[0] == '-':
            return subtract(tokenized_input[2], tokenized_input[1])
        if tokenized_input[0] == '*':
            return multiply(tokenized_input[2], tokenized_input[1])
        
