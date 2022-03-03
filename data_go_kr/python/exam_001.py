#파이썬에서의 JSON데이터 처리

# [1]
# JSON데이터 처리란?
# 클라이언트와 서버 사이에서 데이터를 교환시 파이썬의 객체 타입을 문자열 데이터로 또는 문자열 데이터를 파이썬의 객체 타입으로 변환
# 파이썬의 대표적인 자료구조 4개 --> List, Tuple, Dictionary, Set

# [2] 
# 파이썬 딕셔너리 타입이란?
# 파이썬 자료구조의 한 형태. "키(key):값(value)" 쌍을 요소로 갖는 컬렉션 객체
# 키(key)를 통하여 빠르게 값(value)을 찾아내는 해시테이블(Hash Table)구조를 가지는 객체
# 파이썬에서 딕셔너리 객체는 "dict" 클래스 구현되어 있음.
# 딕셔너리의 키(key)는 값을 변경할 수 없다. --> 즉, Immutable 속성.(변경이 불가능한)(ex)int, str, tuple)
#                                                                              (    ) 
# 딕셔너리의 값(value)은 둘 다 가능 --> 즉, Immutable, Mutable(key로 오면 error) 모두 가능.
                                # (set, list, Dict) 이런 속성들이 key로 오면 안 된다는 뜻
#                                 {  },[   ],{'key' 'value'}    
a={'name':'홍길동'} #dict
print(a) # 가장 전형적인 딕셔너리 타입
print(type(a)) # class<dict>

a={100:'홍길동'} #dict
print(a)
print(type(a)) 

a={(1,2):'홍길동'} #tuple
print(a)
print(type(a)) 

a={'name':{1,2}}
print(a)
print(type(a)) #dict

a={'name':(1,2)}
print(a)
print(type(a)) #dict
print(type(a['name'])) #tuple

b = list(a)
print(type(b)) 
print(b[0]) #name
print(type(b[0])) #str

a={1000:(1,2)}
print(a)
print(type(a)) #dict

b = list(a)
print(type(b)) 
print(b[0]) #name
print(type(b[0])) #int

# 딕셔너리 빈 요소는 --> {}
# 딕셔너리 키 인덱스 --> 딕셔너리명['키'] --> 키를 인덱스처럼 사용. (주의:f 문자열 사용시는 따옴표 주의!)

# [3]
# 파이썬에서 제공하는 JSON 기본 모듈이란?
# 파이썬은 기본적으로 JSON데이터를 효율적으로 다루는 JSON모듈을 제공한다. (그냥 import json해서 사용)
# 가급적 3.x 대 이상의 버전을 사용할 것. 2.x 낮은 일부 버전에서는 기본 모듈이 없을 수 있음.
# 결론 --> json모듈을 사용하면 JSON 데이터를 아주 편리하게 객체에서 문자열로, 문자열을 객체로 변환시킬 수 있다.

# [4] 실습
import json

# 파이썬 딕셔너리 타입
members={
    'id':1004,
    'name':'Json Kim',
    'age':22,
    'email':'jsonkim@test.com',
    'logdata':[
        {'date':'2010-01-13', 'device':'pc(windows os)'},
        {'date':'2010-10-24', 'device':'mobile'},
        {'date':'2010-12-31', 'device':'pc(mac os)'}
    ]
}
print('-'*120)
print(type(members)) #dict

# JSON문자열로 변환
jsonStr = json.dumps(members,indent=4);

# 문자열 출력
print(jsonStr)
print(type(jsonStr)) # str
