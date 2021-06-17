from collections import deque


def solution(progresses, speeds):
    progresses_que = deque(progresses)
    speeds_que = deque(speeds)

    complete_progress = []

    while progresses_que:
        progresses_que = deque([progress + speed for progress, speed in zip(progresses_que, speeds_que)])

        count = 0

        if progresses_que[0] >= 100:
            while True:
                if len(progresses_que) == 0:
                    if count > 0:
                        complete_progress.append(count)
                    break

                x = progresses_que.popleft()

                if x >= 100:
                    speeds_que.popleft()
                    count += 1
                    continue
                else:
                    progresses_que.appendleft(x)
                    if count > 0:
                        complete_progress.append(count)
                    break

    return complete_progress


print(solution([93, 50, 55], [1, 30, 5]))