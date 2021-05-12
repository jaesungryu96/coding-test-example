'''
큰 수의 법칙
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙. 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서
K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

입력 조건
- 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <== 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
- 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000 이하의 수로 주어진다.
- 입력으로 주어지는 K는 항상 M보다 작거나 같다.

출력 조건
- 첫째 줄에 입력된 큰 수의 법칙에 따라 더해진 답을 출력한다.

입력 예시
5 8 3
2 4 5 4 6

출력 예시
46
'''
import sys


N, M, K = map(int, input().split(" "))
data = list(map(int, input().split(" ")))

if N != len(data):
    print("데이터 개수가 맞지 않습니다.")
    sys.exit()

data.sort()
first = data[N-1]
second = data[N-2]

count = 0

count = int(M / (K + 1)) * K
count += M % (K + 1)

result = 0

result += count * first
result += (M - count) * second

print(result)

#
# result = 0
#
# while True:
#     for i in range(K):
#         if M == 0:
#             break
#         result += first
#         M -= 1
#
#     if M == 0:
#         break
#     result += second
#     M -= 1
#
# print(result)