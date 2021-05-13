"""
Q 04. 만들 수 없는 금액

동네 편의점의 주인인 동빈이는 N개의 동전을 가지고 있습니다. 이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는
프로그램을 작성하세요.
예를 들어, N = 5이고, 각 동전이 각각 3원, 2원, 1원, 1원, 9원짜리 (화폐 단위) 동전이라고 가정합시다. 이때 동빈이가 만들 수 없는 양의
정수 금액 중 최솟값은 8원 입니다.
또 다른 예시로, N = 3이고, 각 동전이 각각 3원, 5원, 7원짜리 (화폐 단위) 동전이라고 가정합시다. 이때 동빈이가 만들 수 없는 양의 정수 금액 중
최솟값은 1원 입니다.

입력 조건
- 첫째 줄에는 동전의 개수를 나타내는 양의 정수 N이 주어집니다. (1 <= N <= 1000)
- 둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며, 각 자연수는 공백으로 구분합니다. 이때, 각 화폐 단위는 1000000 이하의
  자연수입니다.

출력 조건
- 첫째 줄에 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력합니다.

입력 예시       출력 예시
5              8
3 2 1 1 9
"""

n = int(input())

data = list(map(int, input().split()))

data.sort()
data.reverse()

price_list = []

sum = 0

for i in data:
    sum += i

total_list = [i for i in range(1, sum + 2)]

for i in range(1, sum + 1):
    i_flag = i
    for j in data:
        if i - j < 0:
            continue
        elif i - j == 0:
            price_list.append(i_flag)
            break
        else:
            i -= j

sub_list = [x for x in total_list if x not in price_list]

print(min(sub_list))