"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def myreduce(op, ls):
    value = ls[0]
    if op.__name__ == 'square' or op.__name__ == 'cube':
        value = op(value)
    else:
        for num in ls[1:]:
            value = op(value, num)
    return value

def main_calculator():
    while True:
        input_ = input()
        tokenized_input = input_.split(' ')
        tokenized_input = [tokenized_input[0]] + [int(string) for string in tokenized_input[1:]]
        if tokenized_input[0] == 'q':
            break
        else:
            if tokenized_input[0] == '+':
                print(myreduce(add, tokenized_input[1:]))
            if tokenized_input[0] == '-':
                print(myreduce(subtract, tokenized_input[1:]))
            if tokenized_input[0] == '*':
                print(myreduce(multiply, tokenized_input[1:]))
            if tokenized_input[0] == '/':
                print(myreduce(divide, tokenized_input[1:]))
            if tokenized_input[0] == 'square':
                print(myreduce(square, tokenized_input[1:]))
            if tokenized_input[0] == 'cube':
                print(myreduce(cube, tokenized_input[1:]))
            if tokenized_input[0] == 'pow':
                print(myreduce(power, tokenized_input[1:]))
            if tokenized_input[0] == 'mod':
                print(myreduce(mod, tokenized_input[1:]))
                
main_calculator()
