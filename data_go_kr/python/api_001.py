#공공 데이터 API사용을 위한 파이썬 라이브러리

#[1]Url Encode
#공공 데이터 이용을 위해 HTTP요청을 할 때(예를들면 GET방식)URL에는 쿼리 파라미터 값들이 붙게 된다.
#이 파라미터에 한글이 포함된다면?-->애석하게도 URL아스키(ASCII)코드 값만 사용이 가능하기 때문에 URL인코딩을 해줘야 한다.
#물론, API호출시 파라미터에 한글 값 그대로를 사용해도 되는 경우도 있지만, 가급적 URL인코딩을 통해 전송하는 것을 권장.
#이때, 사용되는 유용한 파이썬 라이브러리가 urllib라는 패키지가 있다.-->파이썬 자체에 이미 내장되어 있음.
#결론적으로,urllib를 사용해서 URL인코딩 및 URL 관련 처리 작업들을 유연하게 처리할 수 있다.

#[2]urllib
from urllib.parse import urlparse, urlunparse, parse_qs, parse_qsl, urlencode

url=urlparse('https://google.com:80/subpage/search.google?name=홍길동&password=1234')
#urlparse메서드-->URL을 6개의 요소로 분석하여 반환-->명명된 튜플(namedtuple)-->ParseResult의 객체라고 생각
#urllib.parse.ParseResult 객체를 통해서 URL의 여러 값을 분석-->URL의 일반적인 구조라고 생각하면 됨.
#namedtuple이므로 인덱스로 접근하거나 또는 속성명으로 요소에 접근하는 것이 가능
#namedtuple특성상-->immutable속성.

#6개의 반환 값
print(url.scheme)  #https(통신방식)
print(url.netloc)  #google.com:80(서버주소)
print(url.port)    #80(포트번호-서버 프로세스를 구분,80번 포트는 생략이 가능하여 생략시 80포트로 전송)
print(url.path)    #/subpage/search.google (서버상의 도큐먼트 위치)
print(url.params)  #
print(url.query)   #name=홍길동&password=1234(추가정보)
print(url.fragment)#id001(식별자)

#url-->위 요소를 모두 출력
print(url) #ParseResult객체

#ParseResult 객체를 다시 URL로 만들고자 한다면?-->geturl()또는 urlunparse()메서드를 사용.
#urlunparse() 사용법 주의-->url객체를 괄호안에 넣어줌.
print('-'*120,'geturl()')
print(url.geturl())

print('-'*120,'urlunparse()') 
print(urlunparse(url)) #import urlunparse시켜줘야 함.

#namedtuple이므로 인덱스 접근이 가능.for문 사용도 가능
print('-'*120,'인덱스 접근 및 반복문')
print('url[0]:',url[0]) #https
print('url[0]:',url[1])

for value in url:
    print(value)
    
#[3]parse_qs
#qs-->query string
#쿼리 스트링이 문자열 형태로 이뤄져 있는데 값의 변경이나 분리를 용이하게 해주는 함들들이 있는데-->parse_qs(),parse_qsl()
#parse_qs() -> dict | parse_qsl() -> list
#사용을 위해서는 상단에서 import를 먼저 해준다.
#둘의 차이점은 반환 타입이 다르다는 것-->딕셔너리(Dictionary),리스트(List)
#parse_qs는 key에 대해 value들을 리스트(List)로 묶어준 후-->딕셔너리(Dictionary)로 반환
print('-'*120,'parse_qs,parse_qsl')
print(url.query)
qs=parse_qs(url.query)
print(qs,type(qs))                          #타입-->딕셔너리(Dict)

qsl=parse_qsl(url.query)
print(qsl,type(qsl),type(qsl[0]))           #타입-->리스트(List)-->안쪽 요소의 타입은 튜플(tuple)

#[4]urllib.parse를 이용하여 password 변경해보기
#print(parse_qsl(url.query))
print('-'*120,'파라미터 값 변경하기')

test_qs=dict(parse_qsl(url.query))
print(test_qs)

test_qs['password']='5678'
print(test_qs)

test_url=url._replace(query=urlencode(test_qs))
print(test_url)

new_url=urlunparse(test_url)
print(new_url)
