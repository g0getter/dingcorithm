def solution(genres, plays):
    # 1. 장르로 줄 세움 -> dictionary 필요: genre_total_play_dict와(genre: total play)
    # 2. 장르 내부에서 play수로 줄 세움(같으면 index 작은 순) -> 별개의 dictionary: genre_plays_array_dict (genre: [plays] array)

    dict_genre_total = {}  # 장르별 전체 재생 횟수
    dict_genre_plays = {}  # index를 모아놓음

    # 장르 array 내용(key) 넣어 놓고
    for i in range(len(genres)):
        dict_genre_total[genres[i]] = 0
        dict_genre_plays[genres[i]] = []

    # value 채움
    for i in range(len(plays)):
        dict_genre_total[genres[i]] += plays[i]
        dict_genre_plays[genres[i]].append((i, plays[i]))

    # 1. dict_genre_total 정렬
    sorted_total = sorted(dict_genre_total.items(), key=lambda item: item[1], reverse=True)
    # .items(): key-value를 배열 형태로 추출(정렬하기 위해서는 배열로 추출 필수!)

    # 2. dict_genre_plays 정렬 후 순서대로 2개씩 뽑음
    answer_tuple = []
    answer = []
    for genre, _ in sorted_total:
        sorted_plays = sorted(dict_genre_plays[genre], key=lambda item: item[1], reverse=True)
        answer_tuple += sorted_plays[0:2]  # (map 사용하면 참 좋을텐데)

    for index, _ in answer_tuple:
        answer.append(index)

    return answer