"""
큐 예제

파이썬에서 큐를 구현하기 위해 collections 패키지에 deque 라이브러리 사용
"""

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)