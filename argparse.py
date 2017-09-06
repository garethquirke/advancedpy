
#Argparse is a parser for command-line options, arguments, and sub-commands.
import argparse
import sys


def calc(x,y,operation):
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    elif operation == 'mul':
        return x * y
    elif operation == 'div':
        return x / y

print(calc(8,5,'mul'))
print(calc(6,3,'div'))


