#SQLite3 데이터베이스 사용하기

#[!]SQLite3
#자체 내장되어 있는 데이터베이스
#즉,파이썬이 설치될 때 기본으로 인스톨되는 모듈로써 편리하게 DB를 이용할 수 있음.
#보통 3.x대 파이썬 버전을 설치하면 SQLite3모듈 버전은-->2.6.0

#[1]버전확인
import sqlite3

print(sqlite3.version) #모듈 자체의 버전-->2.6.0
print(sqlite3.sqlite_version) #SQLite버전.

#[2]DB생성
#확장자가-->데이터베이스명.db-->로컬 디스크내 생성-->Connection객체의-->connect()함수를 사용해서 생성
#주의사항-->생성 시 순서 및 권한이 중요.
#!가급적 c드라이브 루트 밑에다가는 생성을 안 하는게 좋다.-->보안 등의 권한 문제로 에러날 확률이 높음.
#!따라서 c드라이브 밑에다가 sqlite3폴더를 하나 생성해놓고-->그 디렉토리 안에다가 DB파일을 생성시키는 것을 권장
dbConn=sqlite3.connect("C:\sqlite3/publicapi.db")
print(type(dbConn)) #sqlite3.Connection 객체.

#[3]DB입력

#[3-1]Cursor객체 생성
#SQL구문을 호출하고 실행하고 사용하기 위해서 필요-->Connection객체인 dbConn을 사용해 Cursor객체를 생성.
#SQL구문을 실행할 때-->cs.execute()메서드가 필요.
cs=dbConn.cursor() 
print(type(cs)) #slite3.Cursor객체.

#[3-2]Table생성
#생성된 이후에 다시 같은 이름의 테이블을 또 생성하려고 하면 에러 발생.
# cs.execute("CREATE TABLE testapi(Column1 text,Column2 int,Column3 int,Column4 int)")

#[3-3]데이터 Insert
# cs.execute("INSERT INTO testapi (Column1,Column2,Column3,Column4)values('공공API공부중이네요...5',5,55,555)")

#[3-3]데이터 Select
print('-'*100,'[3-3]데이터 Select')
rst=cs.execute("select*from testapi")
# print(rst)
# print(cs.fetchall()) #fetchall의 타입-->list

#[3-3-1]반복문을 이용한 DB데이터 출력
print('-'*100,'[3-3-1]반복문을 이용한 DB데이터 출력')

for row in cs.fetchall():
    print(row)
    
#[3-4]최종 반영
dbConn.commit()

#[3-5]DB닫기
dbConn.close()