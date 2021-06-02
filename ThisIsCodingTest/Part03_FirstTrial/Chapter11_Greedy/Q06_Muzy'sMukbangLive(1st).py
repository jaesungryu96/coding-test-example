"""
First Trial
acc = 32
efficiency = 0
"""
def solution(food_times, k):
    second = 0
    index = 0

    while second < k:
        if food_times[index % len(food_times)] == 0:
            index += 1
            continue

        food_times[index % len(food_times)] -= 1
        second += 1
        index += 1

    x = 0

    while x == 0:
        x = food_times[index % len(food_times)]

        if x == 0:
            index += 1

    if max(food_times) != 0:
        answer = (index % len(food_times)) + 1
    else:
        answer = -1

    return answer

# TODO : try binary search