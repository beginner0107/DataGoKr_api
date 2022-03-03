#csv파일에 들어있는 데이터를 sqlite DB에 저장하기1

import sqlite3

#[1]DB생성-->Conncetion객체의-->connect()함수를 사용하여 생성
dbConn=sqlite3.connect('c:\sqlite3\mydata.db')
print(type(dbConn)) #sqlite3.Conncetion 객체.

#[2]DB커서 객체 생성-->Conncetion객체인 dbConn을 사용해 Cursor객체를 생성.
cs=dbConn.cursor()
print(type(cs)) #sqlite3.Cursor객체.

#[3]DB테이블 생성
# cs.execute("Create table if not exists tbl_PublicAPI)_")
cs.execute('Create table if not exists tbl_PublicAPI(Column1 text, Column2 text)')


#[4]DB데이터 입력
# cs.execute("insert into tbl_PublicAPI values('두 번째 데이터 입력','222')")
# cs.execute("insert into tbl_PublicAPI values('세 번째 데이터 입력','333')")
# cs.execute("insert into tbl_PublicAPI values('네 번째 데이터 입력','444')")
# cs.execute("insert into tbl_PublicAPI values('다섯 번째 데이터 입력','555')")
dbConn.commit()

#[5]DB데이터 출력
print('-'*100,'SELECT')
cs.execute("select * from tbl_PublicAPI")
rst=cs.fetchall()
print(rst)

#[6]DB데이터 출력 -for
print('-'*100,'DB데이터 출력 -for')
for row in rst:
    print(row)

dbConn.close()