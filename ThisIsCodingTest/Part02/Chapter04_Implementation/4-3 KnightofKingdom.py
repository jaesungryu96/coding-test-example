"""
행복 왕국의 왕실 정원은 체스판과 같은 8 X 8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.

1. 수평으로 두칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두칸 이동한 뒤에 수평으로 한 칸 이동하기

나이트의 위치가 주어졌을 때, 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
행 위치는 1 ~ 8, 열 위치는 a ~ h로 표현한다.

입력 예시    출력 예시
a1          2

ord
ord(c)는 문자의 유니코드 값을 돌려주는 함수이다.

※ ord 함수는 chr 함수와 반대이다.

>>> ord('a')
97
>>> ord('가')
44032
"""

input_data = input()
row = int(input_data[1])
# steps를 int로 처리하기 위한 전처리
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >=1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
