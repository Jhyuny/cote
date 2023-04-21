from collections import deque

def solution(numbers):
    answer = []
    numbers = deque(numbers)
    a = numbers.popleft()
    while numbers:
        for i in range(len(numbers)):
            if numbers[i]>a:
                answer.append(i)
                a = numbers.popleft()
                continue
            if i == len(numbers)-1:
                answer.append(-1)
    return answer

solution([2,3,3,5])