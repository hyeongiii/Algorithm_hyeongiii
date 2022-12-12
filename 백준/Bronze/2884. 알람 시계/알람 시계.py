hour, min = map(int, input().split())

if min < 45 and hour != 0:
    print(hour-1, min + 15)
elif min < 45 and hour == 0:
    print(23, min + 15)
else:
    print(hour, min - 45)