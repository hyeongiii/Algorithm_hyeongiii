import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
cnt = []

for _ in range(n):
    board.append(input())

for a in range(n - 7):  # 8*8 로 자르기 위해 -7을 해준다.
    for b in range(m - 7):
        white_cnt = 0  # white로 시작한 경우, 바뀐 체스판의 개수
        black_cnt = 0  # black으로 시작한 경우, 바뀐 체스판의 개수
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        white_cnt += 1
                    elif board[i][j] != 'B':
                        black_cnt += 1
                elif (i + j) % 2 != 0:
                    if board[i][j] != 'B':
                        white_cnt += 1
                    elif board[i][j] != 'W':
                        black_cnt += 1
        cnt.append(white_cnt)
        cnt.append(black_cnt)

print(min(cnt))