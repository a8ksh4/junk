'''
Use sorted and key functions!

>>> numbers = [0, 2, 3, 5, -1, -4]
>>> sort_abs(numbers)
[0, -1, 2, 3, -4, 5]
>>> words = "Beautiful is better than ugly".split(" ")
>>> sort_last_letter(words)
['Beautiful', 'than', 'better', 'is', 'ugly']

Two other common builtin "functional" functions are map and filter.

Use the builtin "map" function to complete the following:

>>> double_numbers(numbers)
[0, 4, 6, 10, -2, -8]
>>> lower_case(words)
['beautiful', 'is', 'better', 'than', 'ugly']

Use the builtin filter function to complete the following:

>>> positive(numbers)
[2, 3, 5]
>>> non_zero(numbers) # use filter, but don't write any other functions
[2, 3, 5, -1, -4]


And of course mix and match both map and sorted!

>>> lower_last_longwords(words) # longwords == len(word) > 3
['beautiful', 'than', 'better', 'ugly']
>>> double_positive(numbers)
[4, 6, 10]

Use reduce (try the operator module too) to find the multiplication
of a list of numbers

>>> multiply_list(numbers[1:4]) # 2 * 3 * 5
30


'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
