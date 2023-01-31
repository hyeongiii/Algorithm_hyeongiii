def solution(new_id):
    answer = ''
    Ok = ["-", "_", "."]
    
    # 1. 모든 대문자를 대응되는 소문자로 치환 (문자열 내에 숫자나 기호가 들어있어도 대소문자 변환 가능)
    new_id = new_id.lower()
    
    # 2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(-), 마침표(.) 를 제외한 모든 문자 제거
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in Ok:
            answer += i   
    
    # 3. 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환
    while '..' in answer:
        answer = answer.replace("..", ".")
    
    # 4. 마침표가 처음이나 끝에 위치한다면 제거
    if answer == '.':
        answer = ''        
    else:
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 5. new_id가 빈 문자열일 경우, "a" 대입
    if answer == '':
        answer = "a"
    
    #6. 만약 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자 모두 제거
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    #7. 만약 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될때까지 반복
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer