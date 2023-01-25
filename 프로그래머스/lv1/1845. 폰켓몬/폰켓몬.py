'''
내가 푼 풀이
def solution(nums):
    num = len(nums) // 2    # 가져갈 폰켓몬의 수
    box = []    # 서로 다른 종류의 폰켓몬이 들어갈 수 있는 박스

    for i in nums:
        if not i in box:    # 만약 박스 내에 해당 종류의 폰켓몬이 없다면, 박스내로 주입
            box.append(i)

    if len(box) < num:    # 박스 내 폰켓몬 수 > 가져가야할 수, 폰켓몬 종류의 최댓값 = 박스 내의 폰켓몬 수
        return len(box)
    else:    # 박스 내 폰켓몬 수 <= 가져가야할 수, 폰켓몬 종류의 최댓값 = 가져갈 폰켓몬의 수
        return num
'''

def solution(nums):
    return min(len(set(nums)), len(nums) // 2)