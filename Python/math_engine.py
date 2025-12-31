#!/usr/bin/env python3
'''tokenizer and a few math operations;
exploring how this stuff might work.'''

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
            if not open_paren and token.endswith('('):
                open_paren = n
                continue
            if token.endswith('('):
                depth += 1
                continue
            if token == ')' and depth > 0:
                depth -= 1
                continue
            if token == ')':
                # Found a matching paren
                inner = structure(tokens[open_paren:n], foo=foo+1)
                tokens = tokens[:open_paren] + [inner] + tokens[n + 1:]
                open_paren = None
                break
        else:
            break # No more parens to process
        assert depth == 0, "Mismatched parentheses"
        assert open_paren is None, "Mismatched parentheses"

    # print(foo, 'After parens:', tokens)
    # Collapse operators by precedence
    precedence = ['^', '*', '/', '+', '-']
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
    return structured


if __name__ == '__main__':
    EXAMPLES = [
        '1 + 2',
        '3 * 2 + 5 / 7',
        'exp( 2, exp( 3, exp( 4, 5 ) ) )',
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
        # result = evaluate(STRUCTURED)
        # print(f'Result: {result}')
