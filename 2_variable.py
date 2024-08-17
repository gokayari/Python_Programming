"""
In Java: static Typing
    DataType var = Data

In Python: Dynamic Typing
    var = Data
"""
print('----------Data types---------')


name = None

print(name)


name = 'Jones'

print(name)
print(type(name))  # >>> <class 'str'>


age = 25

print(age)
print(type(age))    # >>> <class 'int'>

gpa = 3.5

print(gpa)
print(type(gpa))    # >>> <class 'float'>


is_employed = True
print(is_employed)
print(type(is_employed))    # >>> <class 'bool'>

print("--------Constructor function-------------")

s = '25'

s = int(s)
print(s * 5)