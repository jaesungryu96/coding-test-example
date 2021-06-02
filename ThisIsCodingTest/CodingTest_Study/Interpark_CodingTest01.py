"""
https://programmers.co.kr/learn/courses/30/lessons/42891

"""

input_data = list(map(int, input().split()))
count_list = [0] * 100000

for i in input_data:
    count_list[int(i)] += 1

count_list_len = len(count_list)
rank_list = count_list.copy()
count = 1

while count_list_len != 0:
    if rank_list[count_list_len - 1] != 0:
        rank_list[count_list_len - 1] = count
        count += count_list[count_list_len - 1]

    count_list_len -= 1

output_list = []

for i in input_data:
    output_list.append(rank_list[i])

print(output_list)