'''
Each of the functions below takes the statically defined dictionary 'MENU'
as input and should return (not print) a value that looks like what's shown
in the test.  The dictionary contains mappings of sandwiches and their
ingredients.  See the skeleton implementations for details on what each
function should determine.

>>> option_count(MENU)
26
>>> most_ingredients(MENU)
'California Burger: 9'
>>> most_common(MENU)
'mayonnaise: 22'
>>> unique_ingredients(MENU)
35
'''

def option_count(menu):
    '''How many options can I choose from for lunch?'''
    pass

def most_ingredients(menu):
    '''Which item on the menu has the most ingredients?
       How many does it have?'''
    pass

def most_common(menu):
    '''Which ingredient is the most common?  How many menu items does it
       appear on?'''
    pass

def unique_ingredients(menu):
    '''How many different ingredients are there?'''
    pass

MENU = { 'BBQ Beef': ['chopped beef steak', 'bbq sauce', 'mayonnaise'],
  'Bacon Burger': [ 'bacon',
                    'mustard',
                    'mayonnaise',
                    'onions',
                    'pickles',
                    'tomato',
                    'lettuce'],
  'California Burger': [ 'bacon',
                         'pepper jack',
                         'jalapenos',
                         'mustard',
                         'mayonnaise',
                         'onions',
                         'pickles',
                         'tomato',
                         'lettuce'],
  'California Chicken': [ 'chicken breast',
                          'mayonnaise',
                          'pepper jack',
                          'bacon',
                          'jalapenos',
                          'tomato',
                          'lettuce'],
  'Charbroiled Beef Hot Dog': [ 'mustard',
                                'mayonnaise',
                                'onions',
                                'pickles',
                                'tomato',
                                'lettuce'],
  'Charbroiled Chicken Breast': [ 'marinated filet chicken',
                                  'mayonnaise',
                                  'tomato',
                                  'lettuce'],
  'Club Sandwich': [ 'ham',
                     'turkey',
                     'bacon',
                     'cheese',
                     'mayonnaise',
                     'tomato',
                     'lettuce'],
  'Double Burger': [ 'mustard',
                     'mayonnaise',
                     'onions',
                     'pickles',
                     'tomato',
                     'lettuce'],
  'Garden Burger': ['veggie burger', 'onions', 'pickles', 'tomato', 'lettuce'],
  'Grilled Corned Beef': [ 'mustard',
                           'mayonnaise',
                           'onions',
                           'pickles',
                           'tomato',
                           'lettuce'],
  'Grilled Ham & Cheese': [ 'mustard',
                            'mayonnaise',
                            'onions',
                            'pickles',
                            'tomato',
                            'lettuce'],
  'Grilled Pastrami': [ 'mustard',
                        'mayonnaise',
                        'onions',
                        'pickles',
                        'tomato',
                        'lettuce'],
  'Guacamole Burger': [ 'avocado',
                        'mustard',
                        'mayonnaise',
                        'onions',
                        'pickles',
                        'tomato',
                        'lettuce'],
  'Guacamole Chicken': [ 'chicken breast',
                         'avocado',
                         'mayonnaise',
                         'onions',
                         'tomato'],
  'Hamburger Steak Sandwich': [ 'two beef patties',
                                'grilled onions',
                                'mushrooms',
                                'pepper',
                                'jack cheese on a roll'],
  'Hot Link': [ 'beef link',
                'mustard',
                'mayonnaise',
                'onions',
                'pickles',
                'tomato',
                'lettuce'],
  'Mushroom Burger': [ 'mushrooms',
                       'mustard',
                       'mayonnaise',
                       'onions',
                       'pickles',
                       'tomato',
                       'lettuce'],
  'Old Fashioned B.L.T': ['bacon', 'mayonnaise', 'tomato', 'lettuce'],
  'Pepper Steak': [ 'marinated beef',
                    'red pepper',
                    'onions',
                    'mushroom',
                    'tomato',
                    'lettuce'],
  'Philly Cheese Steak': [ 'chopped tender lean steak',
                           'mayonnaise',
                           'provolone cheese'],
  'Polish Sausage': ['mustard', 'mayonnaise', 'onions', 'tomato', 'lettuce'],
  'Roast Beef Melt': [ 'roast beef',
                       'choice of cheese',
                       'lettuce'],
  'Single Burger': [ 'mustard',
                     'mayonnaise',
                     'onions',
                     'pickles',
                     'tomato',
                     'lettuce'],
  'Steak Sandwich': [ 'sliced tender beef',
                      'mushrooms',
                      'grilled onions',
                      'mayonnaise',
                      'tomato',
                      'lettuce'],
  'Tuna Melt': [ 'fresh tuna',
                 'melted cheese',
                 'mayonnaise',
                 'onions',
                 'tomato',
                 'lettuce'],
  'Turkey Melt with Bacon': [ 'fresh cut turkey',
                              'bacon',
                              'melted cheese',
                              'mayonnaise']}

if __name__ == '__main__':
    import doctest
    doctest.testmod()
