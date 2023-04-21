def time_change(l): # 시간 표현 바꾸는 함수
    for idx,(sub,start,time) in enumerate(l):
        a,b = list(map(int,start.split(':')))
        l[idx][1] = 60*a + b
    return sorted(l, key=lambda x: x[1]) # 시작 순서대로 배열
def solution(plans):
    ing = [] # 진행 중인 과제
    fin = [] # 마무리한 과제 
    plans = time_change(plans)
    now = plans[0][1] # 현재 시간은 맨 첫번째 과제 시작시간
    for idx,plan in enumerate(plans[:-1]): # idxError피하려고 마지막 항은 포함 x
        sub = plan[0]
        start = plan[1]
        time = plan[2]
        if now + int(time) <= plans[idx+1][1]: # 다음 과목 시작 시간과 비교해서 더 작으면
            fin.append(sub) # 과제 끝내서 fin에 append
            now = now + int(time) # 지금 시간 update
            last = plans[idx+1][1]-now # 다음과제 시작 시간까지 남은시간
            while last != 0 and ing: # 남은 시간동안 ing의 과제 진행
                ing_sub, last_time = ing.pop()
                if last_time <= last: # 남은 시간 동안 과제 마무리할 수 있으면
                    last = last - last_time # 남은시간에서 과제 진행한 시간 빼주고
                    fin.append(ing_sub) # 마무리한 과제 fin에 append
                else: # 남은 시간동안 과제 못 끝내면
                    ing.append([ing_sub,last_time-last]) # ing의 과제 남은 시간 update
                    last = 0
            now = plans[idx+1][1] # 다음 과제 시작
        else: # 다음 과제 시작시간인데 지금 과제 못 끝냈으면
            ing.append([sub, start+int(time) - plans[idx+1][1]]) # ing에 [과목명,남은시간] append
            now = plans[idx+1][1] # 다음 과제 시작
            
    sub = plans[-1][0] 
    fin.append(sub) # 마지막 과제 일단 끝내고
    for i in ing[::-1]: # ing의 과제 차례로 끝냄
        fin.append(i[0])
        
    return fin

solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]])