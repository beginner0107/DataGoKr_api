#csv파일에 들어있는 데이터를 sqlite DB에 저장하기2

import csv

#[1]파일 읽기-->open()사용-->csv.reader()메서드 사용하여 한 줄씩 읽기.
fileName="apijson.csv"
file=open(fileName,'r')
reader=csv.reader(file)

#[2]파일 출력
# for row in reader:
    # print(row,type(row)) #list

print('-'*120)

arr=[]

for row in reader:
    arr.append(row)

# print(arr)
for row in arr:
    print(row[0], row[1])
    

