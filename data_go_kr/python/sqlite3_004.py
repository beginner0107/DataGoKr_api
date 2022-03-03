#csv파일에 들어있는 데이터를 sqlite DB에 저장하기2

import csv
import sqlite3

#[1]csv파일 읽기-->open()사용-->csv.reader()메서드 사용하여 한 줄씩 읽기.
fileName="apijson.csv"
file=open(fileName,"r")
reader=csv.reader(file)

#[2]DB연결 및 커서 객체 생성
dbConn=sqlite3.connect("C:\sqlite3\mydata.db")
cs=dbConn.cursor()

#[3]순회하면서 할 일 처리.
arr=[]

for row in reader:
    # print(row)
    arr.append(row)
    
for row in arr:
    print(row[0],row[1])
    strSQL="INSERT INTO tbl_PublicAPI(Column1,Column2)values(?,?)"
    cs.execute(strSQL,(row[0],row[1]))

dbConn.commit()

print('-'*100)
print('CSV파일의 데이터가 DB에 입력되었습니다.')

#[4]DB데이터 출력
print('-'*100,'SELECT')
cs.execute("select * from tbl_PublicAPI")
rst=cs.fetchall()
print(rst)

#[5]DB데이터 출력 -for
print('-'*100,'DB데이터 출력 -for')
for row in rst:
    print(row)

cs.close()
dbConn.close()
