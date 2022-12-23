def String_(num):
    half = len(num) // 2
    lt = 0
    rt = len(num) - 1
    for _ in range(half):
        if num[lt] != num[rt]:
            return "no"
        lt += 1
        rt -= 1
    return "yes"


while True:
    num = input()
    if num == '0':
        break
    print(String_(num))