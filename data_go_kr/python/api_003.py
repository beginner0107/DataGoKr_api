#URL문자열 반환-한글 인코딩 디코딩 quote, unquote

#url에 한글이 포함될 경우 가끔씩 오류가 나는 경우가 있는데 이때 한글을 URL인코더로 인코딩해서 입력해줘야 한다.
#이때, 간편하게 처리하고자 한다면-->urllib-->quote,unquote메서드 사용도 좋다.
#quote():한글-->url
#unquote():url-->한글

from urllib.parse import quote,unquote

qt=quote("대한민국")
print(qt)

unqt=unquote("%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD")
print(unqt)