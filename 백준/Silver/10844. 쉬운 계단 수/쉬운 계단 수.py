import sys
input = sys.stdin.readline

# 정수 입력 받기
n = int(input())

# dp를 위한 리스트 초기화
dp = [[0] * 10 for _ in range(n + 1)]

# 첫 번째 자리에는 0을 제외한 1부터 9까지 한번씩 들어갈 수 있으므로 1로 초기화
for i in range(1, 10):
    dp[1][i] = 1

# dp[n번째 자리수][해당 index보다 앞(n-1번째 자리)에 올 수 있는 숫자]
# 2 자리수부터 시작
for i in range(2, n + 1):    # n : 자리수
    for j in range(10):    # n번째 자리수에 들어간 숫자 (0~9)
        if j == 0:    # i번째 자리의 값이 0이면, i-1번째 자리에는 1만 올 수 있음
            dp[i][j] = dp[i - 1][1]
        elif j == 9:    # i번째 자리의 값이 9이면, i-1번째 자리에는 8만 올 수 있음
            dp[i][j] = dp[i - 1][8]
        else:    # i번째 자리의 값이 2~8이면 i-1번째 자리에는 숫자가 2개씩 올 수 있음
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)