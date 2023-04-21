#무슨 경우가 빠진거지...
def winner(a,board):
    x = 1
    points = []
    for i in board:
        y = 1
        for j in i:
            if j == a:
                points.append(str(x)+str(y))
            y += 1
        x += 1
    winning_case = [['11','12','13'],
                    ['21','22','23'],
                    ['31','32','33'],
                    ['11','22','33'],
                    ['11','21','31'],
                    ['12','22','32'],
                    ['13','23','33']]
    for i in winning_case:
        if len(set(i)-set(points)) == 0:
            return 'win'          
            
def solution(board):
    a = b = 0
    for i in board:
        for j in i:
            if j == 'O':
                a += 1
            if j == 'X':
                b += 1
    if a < b or a > b+1:
        return 0
    if winner('O',board)== 'win' and winner('X',board)== 'win':
        return 0
    if winner('O',board)== 'win':
        if a == b+1:
            return 1
        else:
            return 0
    if winner('X',board)== 'win':
        if a == b:
            return 1
        else:
            return 0
    else:
        return 1