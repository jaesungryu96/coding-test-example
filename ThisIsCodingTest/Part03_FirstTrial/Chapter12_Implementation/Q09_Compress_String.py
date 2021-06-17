"""
문자열 압축

https://programmers.co.kr/learn/courses/30/lessons/60057

정답 코드 보고 했음.

코드의 흐름

1. 문자열 앞에서부터 잘릴 길이 (step)을 점차 늘려나간다.
2. 늘려나가는 step에 맞춰서 문자열을 압축한다.

압축 과정

1. step 만큼 잘라낸 문자열(패턴)을 제외하고
2. 그 뒤의 문자열부터 잘라낸 문자열과 중복여부를 검사한다.
3. 같으면 count +=1, 다르면 결과 문자열에 추가하고 다른 문자열을 패턴으로 설정한다.
4. 반복
"""

def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[0: step]
        count = 1

        for j in range(step, len(s), step):
            if prev == s[j: j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j: j + step]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev

        answer = min(answer, len(compressed))

    return answer