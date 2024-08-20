name = 'James'
age = 26

print('My name is ' + name)
# print('My age is ' + age) >>> TypeError: can only concatenate str (not "int") to str

print('My age is ' + str(age))  # the first method

print('My age is {}'.format(age))   # the second method
print('My age is {} and I am {} years old.'.format(name, age))

print(f'My name is {name} and I am {age} years old')   # the third one, it is recommended
# "f" is format function

print('Python', 3, 'is awesome:', True)    # the fourth