from functools import reduce
"""CLI application for a prefix-notation calculator with reduce"""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
def main_calculator():
    while True:
        input_ = input()
        tokenized_input = input_.split(' ')
        tokenized_input = [tokenized_input[0]] + [int(string) for string in tokenized_input[1:]]
        if tokenized_input[0] == 'q':
            break
        else:
            if tokenized_input[0] == '+':
                print(reduce(add, tokenized_input[1:]))
            if tokenized_input[0] == '+':
                print(reduce(add, tokenized_input[1:]))
            if tokenized_input[0] == '-':
                print(reduce(subtract, tokenized_input[1:]))
            if tokenized_input[0] == '*':
                print(reduce(multiply, tokenized_input[1:]))
            if tokenized_input[0] == '/':
                print(reduce(divide, tokenized_input[1:]))
            if tokenized_input[0] == 'square':
                print(square(int(tokenized_input[1])))
            if tokenized_input[0] == 'cube':
                print(cube(int(tokenized_input[1])))
            if tokenized_input[0] == 'pow':
                print(reduce(power, tokenized_input[1:]))
            if tokenized_input[0] == 'mod':
                print(reduce(mod, tokenized_input[1:]))

main_calculator()
