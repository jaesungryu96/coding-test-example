"""
여행가 A는 N X N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 X 1  크기의 정사각형으로 나누어져 있다.
가장 왼쪽 위 좌표는 (1, 1) 가장 오른쪽 아래 좌표는 (N, N)에 해당한다. 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며,
시작 좌표는 항상 (1, 1)이다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다.
이 계획서를 바탕으로 움직인다고 할때, 여행가 A의 최종 좌표를 출력하는 프로그램을 작성하시오.

입력 예시        출력 예시
5               3 4
R R R U D D

"""

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
