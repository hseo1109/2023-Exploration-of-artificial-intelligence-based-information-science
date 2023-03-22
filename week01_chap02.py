import sys
a=777
print(f'{sys.getrefcount(a)}')
b=3.7
c=a
print(f'{sys.getrefcount(a)}')
c="school"
print(f'{sys.getrefcount(a)}')
# print(type(a),type(b))
# print(id(a),id(b),id(c))