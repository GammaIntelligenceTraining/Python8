from collections import deque

d = deque([1, 2, 3, 4, 5])
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
a = d.popleft()
print(a)
d.extendleft([4, 5, 6])
print(d)
d.rotate(-2)
print(d)