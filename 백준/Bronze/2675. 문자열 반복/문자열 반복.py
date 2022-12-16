num = int(input())

for i in range(num):
    a, b = map(str, input().split())
    result = ''

    for i in range(len(b)):
        result += int(a) * b[i]
    print(result) 
