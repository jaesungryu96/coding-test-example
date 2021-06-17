"""

문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

입출력 예

numbers	return

"17"	3
"011"	2

public static boolean isPrime(int num){
        for(int i=2; i*i<=num; i++){
            if(num % i == 0) return false;
        }
        return true;
    }

"""

import itertools
import math


def solution(numbers):
    result = []

    for i in range(1, len(numbers) + 1):
        tmp = list(itertools.permutations(list(numbers), i))

        for j in range(len(tmp)):
            result.append(int("".join(tmp[j])))

    result = [x for x in list(set(result)) if x > 1]

    answer = 0

    for num in result:
        limit = math.sqrt(num)
        x = 2

        while x <= limit:
            if num % x == 0:
                break
            x += 1

        if x > math.sqrt(num):
            answer += 1

    return answer


print(solution("011")) # 2
print(solution("17")) # 3