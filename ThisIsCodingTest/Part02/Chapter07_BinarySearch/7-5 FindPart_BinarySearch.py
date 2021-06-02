"""
부품 찾기

동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 보품을 대량으로 구매하겠다며
당일 날 견적서를 요청했다. 동ㅁ빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에 부품이
모두 있는지 확인하는 프로그램을 작성해보자.

입력 조건
- 첫째 줄에 정수 N이 주어진다.
- 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1000000 이하이다.
- 셋째 줄에는 정수 M이 주어진다.
- 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1000000 이하이다.

출력 조건
- 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.

입력 예시       출력 예시
5              no yes yes
8 3 7 9 2
3
5 7 9
"""


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result:
        print('yes', end=' ')
    else:
        print('no', end=' ')