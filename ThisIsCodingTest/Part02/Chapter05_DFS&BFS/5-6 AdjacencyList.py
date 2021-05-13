"""
인접 리스트(Adjacency List) 방식

'연결 리스트'라는 자료구조를 이용해 구현한다.
파이썬은 기본 자료형인 리스트 자료형이 append()와 메소드를 제공하므로, 배열과 연결 리스트의 기능을 모두 기본으로 제공한다.
단순히 2차원 리스트를 사용하면 된다.
"""

graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)