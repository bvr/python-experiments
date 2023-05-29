
# experiments with examples from https://death.andgravity.com/namedtuples

from collections import namedtuple
Point = namedtuple('Point', 'x y')

# construct
p = Point(10, 20)

# print and access to properties
print(p)
print(f'{p[0]} {p[1]}')
print(f'{p.x} {p.y}')

# build a dictionary from namedtuple
print(p._asdict())

# build namedtuple from iterable
print(Point._make([30, 40]))
