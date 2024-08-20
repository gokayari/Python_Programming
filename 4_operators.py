print("------    arithmetic operators: +, -, /, %    -------")

print(100 - 3)
print(100 + 3)
print(100 * 3)
print(100 / 3)

print(100/2)    # always float
print(int(100/2))

print(100 % 3)

print("------    shorthand assignment operators: =, +=, -=, /=, %=    -------")

a = 100

a += 50
print(a)    # 150

a /= 2
print(a)    # 'a' is now float
print(int(a))   # >>> to convert to int (but only for this printing)

a %= 20
print(a)


print("------    logical operators: and, or, not    -------")
s = 'Hello World'

print('H' and 'W' in s)     # it is not in Java

print(True and True)
print(True or False)    # These both are like in Java

s = 'Java Python C# C++'
print('Java' or 'Ruby' in s)    # it is different, >>> returns "Java"

print('---i')
age = 29
citizen_ship = 'GER'
is_eligible = age >= 18 and citizen_ship == 'GER'

print(is_eligible)

print('---ii')

has_java = 'Java' in s
print(has_java)

# !contains()   (in Java):
print('Python' not in s)

print('---iii')
print(not False)
print(not True)  # !


print('---------iv-----------')

s = 'Java'
s2 = 'Java'

print(s in s2)  # to check if two variables are referencing to the same objects ( == operator of Java)




