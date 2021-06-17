from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge_truck = deque([])
    bridge_time = deque([])
    complete = deque([])
    count = 0

    while truck_weights or bridge_truck:
        count += 1

        if truck_weights:
            truck = truck_weights.popleft()
        else:
            truck = None

        if bridge_truck:
            for i in range(len(bridge_time)):
                bridge_time[i] += 1

            x = bridge_time.popleft()

            if x >= bridge_length:
                y = bridge_truck.popleft()
                complete.append(y)
            else:
                bridge_time.appendleft(x)

        if truck is not None:
            # 무게가 넘지 않고 들어갈 자리가 있을 때
            if truck + sum(bridge_truck) <= weight and len(bridge_truck) <= bridge_length:
                bridge_truck.append(truck)
                bridge_time.append(0)
                continue
            else:
                truck_weights.appendleft(truck)
                continue
        else:
            continue

    answer = count
    return answer


# print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))