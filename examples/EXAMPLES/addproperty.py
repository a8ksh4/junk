#!/usr/bin/env python

class AddProperty(object):
    
    def __init__(self, property_name, **kw):
        '''Add one property to a class.
        
        fixed parameter:
        property_name->str or unicode  Name of the property
        
        keyword parameters:
        readwrite->Boolean   Whether the property is writable
        value->object        Initial value of property
        self._property_name = property_name
        self._is_readwrite = kw.get('readwrite', False)
        self._value = kw.get('value', None)
        '''
        self._property_name = property_name
        self._is_readwrite = kw.get('readwrite', False)
        self._value = kw.get('value')

    def __call__(self, old_class):
        private_name = '_' + self._property_name.lower() 
        get_function = lambda self_: getattr(self_, private_name)
        get_method = property(get_function)
        setattr(old_class, self._property_name, get_method )
        setattr(old_class, private_name, self._value)
        if self._is_readwrite:
            def set_function(self, new_value):
                setattr(self, private_name, new_value)
            set_method = get_method.setter(set_function)
            setattr(old_class, self._property_name, set_method)
        return old_class   # return the original class

if __name__ == '__main__':
    
    @AddProperty('Spam', value='Fried')
    @AddProperty('Eggs', value='Poached', readwrite=True)
    class Breakfast(object):
        '''"empty" class'''
        pass

    b = Breakfast()

    print 'b.Spam:', b.Spam
    print 'b.Eggs:', b.Eggs
    b.Eggs = 'Scrambled'
    print 'b.Eggs:', b.Eggs
    print type(b.Spam)
    print type(b.Eggs)
    print type(Breakfast.Spam)
    print
    print dir(b)