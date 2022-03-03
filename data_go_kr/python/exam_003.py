#JSON 문자열을 객체로 변환 및 출력

import json

#JSON 문자열
#종료를 의미하는 세미콜론(;)의 경우 붙여도 에러가 나는 것은 아니나 보통 파이썬에서는 안 붙인다.
jsonStr='{"id": 1004,"name": "Json Kim","age": 22,"email": "jsonkim@test.com","logdata": [{"date": "2010-01-13","device": "pc(windows os)"},{"date": "2010-10-24","device": "mobile"},{"date": "2010-12-31","device": "pc(mac os)"}]}'
print(type(jsonStr)) # str

#JSON문자열 데이터-->파이썬 딕셔너리 타입
jsonObj=json.loads(jsonStr)
print(type(jsonObj)); # dict

#하나만 출력 --> Json Kim
print(jsonObj['name']) # Json kim

#중첩된 구조의 반복
print('-'*120)
for v in jsonObj['logdata']:
    #print(v['date'], v['device'])
    # print(f'접속날짜는 {v["date"]}이고, 접속 장치는 {v["device"]}입니다.') #주의:홑따옴표로 감쌌다면 안쪽은 쌍따옴표로 처리
    print(f"접속날짜는 {v['date']}이고, 접속 장치는 {v['device']}입니다.") #주의:홑따옴표로 감쌌다면 안쪽은 쌍따옴표로 처리













