def solution(name, yearning, photo):
    answer = []
    dict_yearning = {}
    for i,j in zip(name,yearning):
        dict_yearning[i] = j
    for i in photo:
        for j in i:
            score = 0
            if j in name:
                score += dict_yearning[j]
        answer.append(score)
    return answer

solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])