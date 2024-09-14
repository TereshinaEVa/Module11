import sys
from pprint import pprint

class Pupil:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


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

pup1 = Pupil('Vasiliy', 15, 8)
#number_info = introspection_info('42')
#str_info = introspection_info('stroka')
class_info = introspection_info(pup1)
#pprint(number_info)
pprint(class_info)
