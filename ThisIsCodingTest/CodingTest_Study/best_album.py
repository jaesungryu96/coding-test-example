"""

문제 설명

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항

genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.

입출력 예

genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

"""


def solution(genres, plays):
    answer = []

    genres_plays_with_id = sorted(list(zip([i for i in range(len(genres))], genres, plays)), key = lambda x : x[2], reverse=True)

    genres_set = set(genres)

    idx_of_genres = dict()
    total_plays_by_genre = dict()

    for genre in genres_set:
        idx_of_genres[genre] = [idx for idx in range(len(genres)) if genres[idx] == genre]

    for genre in genres_set:
        total_plays_by_genre[genre] = sum([plays[i] for i in idx_of_genres[genre]])

    total_plays_by_genre = dict(sorted(total_plays_by_genre.items(), key=lambda x : x[1], reverse=True))  # 내림차순

    genres_sorted_by_total_plays = total_plays_by_genre.keys()

    idx_dict = dict()

    for i in genres_sorted_by_total_plays:
        idx_dict[i] = [idx for idx, genre, plays in genres_plays_with_id if genre == i]

    for j in idx_dict:
        if len(idx_dict[j]) < 2:
            answer.extend(idx_dict[j])
        else:
            answer.extend(idx_dict[j][:2])

    return answer

# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "electronic", "pop"], [500, 600, 150, 3000, 250]))
