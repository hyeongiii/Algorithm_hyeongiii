import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def dfs(node):
    visited[node] = True
    i = graph[node]
    if not visited[i]:
        dfs(i)


t = int(input())

# 테스트 케이스만큼 반복
for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().rstrip().split()))
    visited = [False] * (n + 1)

    # 사이클의 개수 세기
    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            count += 1

    print(count)