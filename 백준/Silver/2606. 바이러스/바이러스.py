import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 그래프 생성
n = int(input())
m = int(input())
graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = graph[b][a] = True

visited = [False] * (n + 1)    # 방문기록 확인하는 리스트 생성
com = []    # 1번 컴퓨터와 연결된 컴퓨터를 저장할 리스트


def dfs(node):
    visited[node] = True
    com.append(node)
    for i in range(1, n + 1):
        if not visited[i] and graph[node][i]:
            dfs(i)


dfs(1)
print(len(com) - 1)    # 1번 컴퓨터를 제외한 수를 구해야하기 때문에 -1