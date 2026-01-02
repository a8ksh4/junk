#!/usr/bin/env python3
'''tokenizer and a few math operations;
exploring how this stuff might work.'''

import math
from types import NotImplementedType

OPPS = {  # Follow order of operations
    '^': float.__pow__,
    '*': float.__mul__,
    '/': float.__truediv__,
    '+': float.__add__,
    '-': float.__sub__,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    # 'exp': math.exp,
    '**': float.__pow__,
    'exp': float.__pow__,
    'log': math.log,
}

CONSTANTS = {
    'pi': math.pi,
    'e': math.e,
}

def cleanup(expression):
    '''This will eventually handle anything needed to 
    sanitize the expression for the tokenizer.  E.g. it will convert:
    * "sin ( " into "sin("
    * "3pi" into "3 * pi"
    * "1+2" into "1 + 2"
    '''
    return expression


def tokenize(expression):
    '''Convert a mathematical string into tokens representing
    numbers, operators, and parentheses.  Operaotrs can 
    be such as +, -, *, /, ^, as well as stuff like exp(), sin(), 
    and so on.
    We'll have expectains of clean inupt for now, increase
    flixibility later.'''
    tokens = expression.split()
    tokens = [t for t in tokens if t and t != ',']
    for n, token in enumerate(tokens):
        if token.endswith(','):
            # tokens[n] = token[:-1]
            token = token[:-1]
        try:
            tokens[n] = float(token)
        except ValueError:
            # print(f'Non-numeric token: {token}')
            pass
        if token in CONSTANTS:
            tokens[n] = CONSTANTS[token]
    return tokens


def structure(tokens, foo=0):
    '''This is a recursive function that will step through tokens and
    generate a hierarchal structure representing the order of operations.
    '''
    # Collapse parens first
    while True:
        open_paren = None
        depth = 0
        for n, token in enumerate(tokens):
            if isinstance(token, (list, tuple)):
                continue
            if not open_paren and isinstance(token, str) and token.endswith('('):
                open_paren = n
                continue
            if isinstance(token, str) and token.endswith('('):
                depth += 1
                continue
            if token == ')' and depth > 0:
                depth -= 1
                continue
            if token == ')':
                # Found a matching paren
                inner = structure(tokens[open_paren:n], foo=foo+1)
                if inner[0] == '(':
                    assert len(inner) == 2
                    assert isinstance(inner[1], list)
                    inner = inner[1]
                # print(inner)
                inner = [i.replace('(', '') if isinstance(i, str) else i for i in inner]
                tokens = tokens[:open_paren] + [inner] + tokens[n + 1:]
                open_paren = None
                break
        else:
            break # No more parens to process
        assert depth == 0, "Mismatched parentheses"
        assert open_paren is None, "Mismatched parentheses"

    # print(foo, 'After parens:', tokens)
    # Collapse operators by precedence
    precedence = ['**', '^', '*', '/', '+', '-']
    for operator in precedence:
        while True:
            for n, token in enumerate(tokens):
                if token == operator:
                    left = tokens[n - 1]
                    right = tokens[n + 1]
                    new_token = [operator, left, right]
                    tokens = tokens[:n - 1] + [new_token] + tokens[n + 2:]
                    break
            else:
                break # No more of this operator

    structured = tokens
    if len(structured) == 1 and isinstance(structured[0], list):
        structured = structured[0]

    return structured


def recurse_apply(node, func):
    '''Not sure yet how this shuold work. I'm pretty
    sure lots of stuff will need to be tested across and 
    possibly applied to every node/level of the structure.'''
    if not isinstance(node, list):
        return node

    for n, item in enumerate(node):
        if isinstance(item, list):
            node[n] = recurse_apply(item, func)
    # print('node before func:', node)
    node = func(node)
    # print('node after func:', node)
    return node


def solve_or_reduce(node):
    '''Evaluate a node if possible, otherwise return it unchanged.'''
    oper = node[0]
    # print('oper is:', oper)

    func = lambda x: x  # Default no-op
    try:
        func = OPPS[oper]
    except TypeError:
        print('TypeError for oper (probably not an oper:', oper)
    except KeyError:
        print('KeyError for oper (unknown oper):', oper)

    try:
        new_node = func(*node[1:])
        if isinstance(new_node, type(NotImplemented)):
            raise NotImplementedError("Can't eval this node using given operator.")
        node = new_node
    except NotImplementedError as e:
        print(f'NotImplemented evaluating {node}: {e}')
    except OverflowError as e:
        print(f'Overflow evaluating {node}: {e}')
    except Exception as e:
        print(f'Error evaluating {node}: {e}')

    return node


if __name__ == '__main__':
    EXAMPLES = [
        '1 + 2',
        '3 * 2 + 5 / 7',
        'exp( 2, exp( 3, exp( 4, 5 ) ) )',
        '2 ** ( 3 ** ( 4 ** 5 ) )',
        '2 ** 3 ** 4 ** 5',
        '3 + 4 * 2 / ( 1 - 5 ) ^ 3',
        'sin( 0 ) + cos( ( 3 * pi ) / 2 )',
        'exp( 2 , 3 ) + log( 10 )',
    ]
    EX_STRUCTURED = [
        ('+', 1, 2),
        None,
        None,
        None,
        None
    ]
    for EX in EXAMPLES:
        print(f'\nInput: "{EX}"')

        EX = cleanup(EX)
        TOKENS = tokenize(EX)
        print(f'Tokens: {TOKENS}')

        STRUCTURED = structure(TOKENS)
        print(f'Structured: {STRUCTURED}')

        STRUCTURED = recurse_apply(STRUCTURED, solve_or_reduce)
        print(f'After solve_or_reduce: {STRUCTURED}')

        # result = evaluate(STRUCTURED)
        # print(f'Result: {result}')
