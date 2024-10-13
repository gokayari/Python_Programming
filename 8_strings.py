name = 'Python'

print(len(name))

print(name[0])
print(name[len(name)-1])

print(name[-1])
print(name[-2])

print('----------')

s = 'Java Programming Language'
s2 = s[5:16]

print(s2)

s3 = s[:4]
print(s3)

print('----/reverse/----')

s4 = s[::-1]    # reverses the string after slicing, first method!
print(s4)

s = 'Python Programming'
s5 = reversed(s)
print(type(s5))
print(s5)
# s5 = str(reversed(s)) # it does not work! to reverse

s6 = ''.join(reversed(s))   # with reversed() function, second method!
print(type(s6))
print(str(s6))

word = 'C++ Programming Language'  # with for loop, third method!
r = ""
for char in word:
    r = char + r
print(r)

print("------//------")

s = 'python programming language'

s = s.capitalize()  # Python programming language
s = s.title()       # Python Programming Language

s = '        programming        '
s = s.strip()       # 'programming'

print(s.index('g'))     # =3    (first index)
print(s.rindex('g'))    # =10   (last index)

print('-----replace-----')

s = 'JAVA programming language'
s = s.replace('JAVA', 'PYTHON', 1)
print(s)

print('-----///-----')

s = 'Java jAVA java JAVA Python Python'

count_java = s.count('java')    # s.lower.count('java') =4
count_python = s.count('Python')

print(count_java)       # =1
print(count_python)     # =2


s1 = 'java'
s2 = 'jAvA'

print(s1 == s2)       # =False
print(s1.lower() == s2.lower())    # =True

print(s[0].islower())   # =False
print(s[0].isupper())   # =True


s = 'a'

print(s.isalpha())      # =True

s = '1'

print(s.isdigit())      # =True
print(s.isnumeric())    # =True