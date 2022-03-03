#sqlite DB에서 데이터 삭제하기

import sqlite3

#[1]DB연결-->connect()
dbConn=sqlite3.connect('c:\sqlite3\mydata.db')

#[2]DB커서 객체 생성-->Connection객체인 dbConn을 사용해 Cursor객체를 생성.
cs=dbConn.cursor()

#[3]DB데이터 출력
print('-'*100,'[출력]')
cs.execute('select*from tbl_PublicAPI')
rst=cs.fetchall()

for row in rst:
    print(row)
    
#[4]DB데이터 삭제
print(type((555)))  #int
print(type((555,))) #tuple

# cs.execute("delete from tbl_PublicAPI where Column2=?",(444,))#한 개만 삭제

# cs.execute("delete from tbl_PublicAPI") #전체 삭제
print(cs.execute("delete from tbl_PublicAPI").rowcount)
# dbConn.commit()

print('-'*100,'[삭제 후 출력]')
for row in rst:
    print(row)

#[5]DB닫기
cs.close()
dbConn.close()



