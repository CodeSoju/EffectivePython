# Python code for type() with a name, bases and dict param

o1 = type('X', (object,), dict(a = 'Foo', b = 12))

print(type(o1)) 
print(vars(o1))
print('\n')

class test:
	a = 'Foo'
	b = 12

o2 = type('Y', (test,), dict(a = 'Foo', b = 12))
print(type(o2)) 
print(vars(o2))

# isinstace() function checks if the obj (first arg) is an instance or
# subclass of classinfo class (second arg)
"""
Syntax:
isinstance(object, classinfo)
object: object to be checked
classinfo: class, type, or tuple of classes and types

Return value: 
true: if the object is an instance or subclass of a class , or any element of the tuple
false: otherwise. if class info is not a type or tuple of types, a TypeError exception is raised

"""

class exam:
	a = 5

ExamInstance = exam()

print(isinstance(ExamInstance, exam))
print(isinstance(ExamInstance, (list, tuple)))
print(isinstance(ExamInstance, (list, tuple, exam)))

# If you're checking to see if an objet has a certain type, you want 
# isinstance()
#
#