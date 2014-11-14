def factorial(n):
    f = lambda n: [1 if n <= 2 else f(n-1), n]
    r = lambda m: (m[0]*m[1] if type(m[0]) != type(list()) else r(m[0])*m[1])
    return r(f(n))
