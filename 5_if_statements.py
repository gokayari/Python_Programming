if True:
    print('Python Programming')  # belongs to if block

print('Java Programming')  # does not belong to if block


print('---------1-----------')

score = 70
if score >= 60:
    print('Congrats! You passed the exam!')


print('---------2-----------')

s = 'Hello World'
if 'H' and 'W' in s:
    print(s, 'has', 'H and W')


print('---------3-----------')

age = 20
result = None

if age >= 21:
    result = 'Eligible'
else:
    result = 'Not Eligible'
print(result)


print('---------4-----------')
# Ternary:

age = 26
result = 'Eligible' if age >= 21 else 'Not Eligible'

print(result)


print('----------5----------')

num = 100
result = None

if num > 0:
    result = 'Positive'
elif num < 0:
    result = 'Negative'
else:
    result = 'Zero'

print(result)


print('----------6----------')

num = -200

result2 = 'Positive' if num > 0 else 'Zero or negative'
print(result2)


print('----------7----------')
# first way, not so correct
score = -59

if 0 <= score <= 100:
    pass
else:
    print('Invalid Score')

if score >= 60:
    print('Passed')
else:
    print('Failed')

print('----------8----------')
# second way, better

if 0 <= score <= 100:
    if score >= 60:
        print('Passed')
    else:
        print('Failed')
else:
    print('Invalid Score')
