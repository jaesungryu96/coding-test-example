import heapq


def solution(numbers):
    numbers_str = "".join(sorted([str(number) for number in numbers], key= lambda x : str(x) * 5, reverse=True))
    return str(int(numbers_str))

print(solution([3, 30, 34, 5, 9]))

"""
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9] "9534330"
"""