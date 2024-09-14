import sys
from pprint import pprint

def introspection_info(obj):
    attributes = []
    methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)
    return {
        'type': type(obj).__name__,
        'attributes': attributes,
        'methods': methods,
        'module': __name__,
        'id': id(obj),
        'size': sys.getsizeof(obj)
    }


number_info = introspection_info('42')
#str_info = introspection_info('stroka')
pprint(number_info)
