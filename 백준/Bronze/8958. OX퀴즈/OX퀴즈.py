num = int(input())
score = 0
total = 0

for _ in range(num):
    test = input()
    for i in range(len(test)):
        if test[i] == 'O':
            score += 1
            total += score
            if i != len(test) -1 and test[i+1]== 'X':
                score = 0
    print(total)
    total = 0
    score = 0