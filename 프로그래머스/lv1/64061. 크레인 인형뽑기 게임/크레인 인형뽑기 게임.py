def solution(board, moves):
    basket = []
    answer = 0
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                basket.append(board[j][i - 1])    # 0이 아닌 경우에만 인형 뽑기
                board[j][i - 1] = 0    # 뽑은 후, 해당 자리는 0으로 변경
                break
                
        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                basket.pop()
                basket.pop()
                answer += 2
    return answer