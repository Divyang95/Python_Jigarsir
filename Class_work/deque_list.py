from _collections import deque

l = deque([])

l.append(10)
print(type(l))
print(l)
print(list(l))

l.append(20)
print(list(l))

l.append(30)
print(list(l))

l.append(40)
print(list(l))

l.popleft()
print(list(l))

l.popleft()
print(list(l))

l.popleft()
print(list(l))
