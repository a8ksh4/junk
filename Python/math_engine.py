#!/usr/bin/env python3
'''tokenizer and a few math operations;
exploring how this stuff might work.'''

import argparse
import math
import re
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

def parse_args():
    '''Parses the args!'''
    parser = argparse.ArgumentParser(
        description='A simple math expression tokenizer and evaluator.'
    )
    parser.add_argument('-e', '--expression', type=str,
                        help='Mathematical expression to evaluate.')
    parser.add_argument('-s', '--solve_for', type=str,
                        help='Variable to solve for.')
    parser.add_argument('-g', '--givens', type=str, default='',
                        help='Comma-separated list of variable=value pairs for givens.')
    parser.add_argument('-t', '--test', action='store_true',
                        help='Run test cases.')
    args = parser.parse_args()
    return args


def cleanup(expression):
    '''This will eventually handle anything needed to 
    sanitize the expression for the tokenizer.  E.g. it will convert:
    * "sin ( " into "sin("
    * "3pi" into "3 * pi"
    * "1+2" into "1 + 2"
    '''
    # number times variable/constant -> number * variable/constant
    # pattern = r'(\d*(\.\d+)?)([a-zA-Z_(]+)'
    pattern = r'((\d+\.)?\d+)([a-zA-Z_(]+)'
    replacement = r'\1 * \3'
    expression = re.sub(pattern, replacement, expression)
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
    if '=' in tokens:
        eq_index = tokens.index('=')
        left = tokens[:eq_index]
        right = tokens[eq_index + 1:]
        left_structured = structure(left, foo=foo+1)
        right_structured = structure(right, foo=foo+1)
        return ['=', left_structured, right_structured]

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


def simple_reduce_node(node):
    '''Paired with the commutative node function, we can
    combine like terms in a simple way here.'''
    numeric_values = []
    other_values = []
    oper = node[0]
    assert oper in ('+', '*'), "simple_reduce_node only works for + and *"
    for item in node[1:]:
        if isinstance(item, (int, float)):
            numeric_values.append(item)
        else:
            other_values.append(item)
    oper_func = OPPS[oper]
    print(numeric_values, other_values, oper_func, oper)
    if numeric_values:
        total = oper_func(*numeric_values)
        other_values.insert(0, total)

    node = [oper] + other_values
    return node


def collapse_commutative_nodes(node):
    '''Check nested nodes for common operators to simplify if possible.
    E.g. ['+', 1, ['+', 2, y]] can become ['+', 3, y].
    Starting with + and *, tbd how this will work for - and /, etc.'''
    if not isinstance(node, list):
        return node
    oper = node[0]
    if oper not in ('+', '*'):
        return node
    values = []
    for item in node[1:]:
        if isinstance(item, list) and item[0] == oper:
            for subitem in item[1:]:
                values.append(subitem)
        else:
            values.append(item)
    node = [oper] + values
    node = simple_reduce_node(node)
    return node


def update_constants(givens):
    '''Update CONSTANTS dict with any provided givens...'''
    givens = givens.split(',')
    for given in givens:
        var, val = given.strip().split('=')
        var = var.strip()
        val = val.strip()
        try:
            val = float(val)
        except ValueError:
            print(f'Given value for {var} is not numeric: {val}')
            continue
        CONSTANTS[var] = val


def main(args):
    '''Main func!'''
    input_expr = args.expression
    update_constants(args.givens)

    input_expr = cleanup(input_expr)
    tokens = tokenize(input_expr)
    structured = structure(tokens)
    print(f'Initial structured: {structured}')
    structured = recurse_apply(structured, collapse_commutative_nodes)
    print(f'After collapse_commutative_nodes: {structured}')
    structured = recurse_apply(structured, solve_or_reduce)
    print(f'Final structured: {structured}')


if __name__ == '__main__':
    ARGS = parse_args()
    if not ARGS.test:
        main(ARGS)
        exit(0)

    # Test cases
    EXAMPLES = [
        '1 + 2',
        '3 * 2 + 5 / 7',
        'exp( 2, exp( 3, exp( 4, 5 ) ) )',
        '2 ** ( 3 ** ( 4 ** 5 ) )',
        '2 ** 3 ** 4 ** 5',
        '3 + 4 * 2 / ( 1 - 5 ) ^ 3',
        'sin( 0 ) + cos( ( 3 * pi ) / 2 )',
        'exp( 2 , 3 ) + log( 10 )',
        '2x + 3 ** 2',
        '5 * n ** 2 + 2 * n ** 3 - 7',
        'y = 2x + 5',
        'm = 3.3n - 4.4',
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
        print(f'Cleaned: "{EX}"')
        TOKENS = tokenize(EX)
        print(f'Tokens: {TOKENS}')

        STRUCTURED = structure(TOKENS)
        print(f'Structured: {STRUCTURED}')

        STRUCTURED = recurse_apply(STRUCTURED, collapse_commutative_nodes)
        print(f'After collapse_commutative_nodes: {STRUCTURED}')

        STRUCTURED = recurse_apply(STRUCTURED, solve_or_reduce)
        print(f'After solve_or_reduce: {STRUCTURED}')

        # result = evaluate(STRUCTURED)
        # print(f'Result: {result}')
