# 해쉬 알고리즘 방식
from sys import stdin

_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())

# 해쉬 자료구조는 주로 Dictionary로 구현
hashmap = {}

for n in N:
    # hashmap에 key가 있을 경우, +1
    if n in hashmap:
        hashmap[n] += 1
    # hashmap에 key가 없을 경우, 값 1 추가    
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))