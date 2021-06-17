"""
보드 크기 N
사과 개수 K



6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

"""
import heapq

n = int(input())
k = int(input())

whole_map = [[0] * (n + 2) for _ in range(n + 2)]

for _ in range(k):
    row, column = map(int, input().split())
    whole_map[row][column] = 1

turning_count = int(input())
turning_points = {}

for _ in range(turning_count):
    s, d = input().split()
    turning_points[int(s)] = d

print(turning_points)

# snake
snake_head_x = 1
snake_head_y = 1
snake_body = []
snake_length = 1
snake_state = 1
move_types = ['U', 'R', 'D', 'L']
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

second_count = 0

while True:
    second_count += 1

    # 방향 전환
    if second_count in turning_points:
        if turning_points[second_count] == 'D':
            snake_state += 1

            if snake_state > 3:
                snake_state = 0
        else:
            snake_state -= 1

            if snake_state < 0:
                snake_state = 3

    snake_head_x += dx[snake_state]
    snake_head_y += dy[snake_state]

    # 사과가 있을 때
    if whole_map[snake_head_x][snake_head_y] == 1:
        snake_length += 1

    break