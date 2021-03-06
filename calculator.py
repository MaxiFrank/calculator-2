"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
def main_calculator():
    while True:
        input_ = input()
        tokenized_input = input_.split(' ')
        if tokenized_input[0] == 'q':
            break
        else:
            if tokenized_input[0] == '+':
                print(add(int(tokenized_input[1]), int(tokenized_input[2])))
            if tokenized_input[0] == '-':
                print(subtract(int(tokenized_input[1]), int(tokenized_input[2])))
            if tokenized_input[0] == '*':
                print(multiply(int(tokenized_input[2]), int(tokenized_input[1])))
            if tokenized_input[0] == '/':
                print(divide(int(tokenized_input[1]), int(tokenized_input[2])))
            if tokenized_input[0] == 'square':
                print(square(int(tokenized_input[1])))
            if tokenized_input[0] == 'cube':
                print(cube(int(tokenized_input[1])))
            if tokenized_input[0] == 'pow':
                print(power(int(tokenized_input[1]), int(tokenized_input[2])))
            if tokenized_input[0] == 'mod':
                print(mod(int(tokenized_input[1]), int(tokenized_input[2])))

main_calculator()