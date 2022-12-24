def solution(before, after):
    be = list(before)
    af = list(after)

    be.sort()
    af.sort()

    for i in range(len(before)):
        if be[i] != af[i]:
            return 0

    return 1