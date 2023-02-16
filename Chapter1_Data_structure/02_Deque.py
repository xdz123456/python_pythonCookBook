from collections import deque


# Keeping the last N Items
# deque, a kind of stack
test_deque = deque(maxlen=3)
test_deque.append(8)
print(test_deque)
test_deque.append(9)
print(test_deque)
test_deque.append(11)
print(test_deque)
test_deque.append(19)
print(test_deque)
test_deque.append(121)
print(test_deque)
test_deque.appendleft(4)
print(test_deque)
# O(1)
test_deque.pop()
print(test_deque)