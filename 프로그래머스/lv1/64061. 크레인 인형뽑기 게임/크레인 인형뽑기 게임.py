def solution(board, moves):
    answer = 0
    
    moves = [i - 1 for i in moves]
    bucket = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i] != 0:
                if len(bucket) != 0 and board[j][i] == bucket[-1]:
                    answer += 2
                    bucket.pop()
                else:
                    bucket.append(board[j][i])
                    
                board[j][i] = 0
                break
    
    return answer