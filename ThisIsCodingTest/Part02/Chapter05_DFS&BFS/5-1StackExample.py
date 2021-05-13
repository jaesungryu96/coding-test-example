"""
스택 예제

파이썬은 별도의 라이브러리를 사용할 필요가 없다. 기본 리스트에서 append(), pop()이 동일한 동작을 한다.
"""

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])