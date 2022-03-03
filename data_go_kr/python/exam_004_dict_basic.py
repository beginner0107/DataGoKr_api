#딕셔너리 자료구조와 반복문
#파이썬 딕셔너리 타입에 대해서는 여러 사용 문법과 반복문 등과 함께 사용하는 방법을 잘 익혀두는게 중요하다.

#[1]키(key)출력
testDict1={'Tiger':100,'Lion':200,'Alligator':300,'Hippo':400}
for i in testDict1:
    # print(i) #Tiger, Lion, Alligator, Hippo 키만 출력되고, 값을 출력X
    print(i, end=' ') # 가로 출력
print()

#[2]키(key)와 값(value)출력
print('-'*50)
testDict2={'Tiger':100,'Lion':200,'Alligator':300,'Hippo':400}
for key, value in testDict2.items(): # items 메소드 사용
    print(key,value)

#[3]딕셔너리를 직접 반복문내에 써서 사용하기
print('-'*50)
for key, value in {'Tiger':100,'Lion':200,'Alligator':300,'Hippo':400}.items():
    print(key,value)

#[4]키(key)와 값(value)만 출력하는 방법-->keys(),values()
print('-'*50)
for key in {'Tiger':100,'Lion':200,'Alligator':300,'Hippo':400}.keys():
    print(key)
    
for value in {'Tiger':100,'Lion':200,'Alligator':300,'Hippo':400}.values():
    print(value)
 
#[5]키(key)추가하기-->기존 딕셔너리에 키(key)추가-->setdefault()메서드 사용.
print('-'*120,'[5]')
testDict5={'홍길동':20,'이순신':30,'강감찬':40,'을지문덕':50}
testDict5.setdefault('김유신') # value 값은 없다. 키(key)만 추가 --> none으로 값이 입력 처리됨.
print('testDict5:',testDict5)

testDict5.setdefault('광개토대왕',100) # 키(key)와 값(value)이 모두 입력
print('testDict5:',testDict5)

#[6]키(key)를 통한 값 수정하기-->update()메서드 사용-->주의사항 있음!
print('-'*120,'[6]')
testDict6={'홍길동':20,'이순신':30,'강감찬':40,'을지문덕':50}
#testDict6.update('을지문덕'=80) # 따옴표를 때야 함 Error-->쌍따옴표든 홑따옴표든 모두 생략하고 사용.
testDict6.update(을지문덕=80) # 따옴표를 때야 함 
testDict6.update(강감찬=44)
print('testDict6:', testDict6)

#[7]수정시 만약 없는 쌍을 수정하려고 하면-->그건 입력으로 처리 됨.
print('-'*120,'[7]')
testDict7={'홍길동':20,'이순신':30,'강감찬':40,'을지문덕':50}
testDict7.update(장수왕=80) #'장수왕'이라는 키(key)는 없으므로 이 쌍은 그냥 새로운 입력으로 처리.
print('testDict7:',testDict7)

#[8]여러 개의 항목을 수정하려면?-->콤마(,)로 구분.
print('-'*120,'[8]')
testDict8={'홍길동':20,'이순신':30,'강감찬':40,'을지문덕':50,'장수왕':70, '광개토대왕':40}
print('testDict8:',testDict8)
testDict8.update(광개토대왕=100,장수왕=200)
print('testDict8:',testDict8)

#[9]키(key)가 문자열이 아닌 숫자인 경우-->수정시 주의사항!
print('-'*120,'[9]')
testDict9={1:'잇지',2:'오마이걸',3:'스테이씨',4:'로켓펀치'}
# testDict9.update(4=에이티즈) #Error

#udpate()메서드 안에서 딕셔너리({})로 감싸준 다음-->해당 요소의 값을 수정.
testDict9.update({4:'에이티즈'})
print('testDict9',testDict9)

#여러 개인 경우도 딕셔너리로 감싸주고 콤마(,)로 구분하여 수정.
testDict9.update({3:'원어스',4:'트와이스'})
print('testDict9',testDict9)

#[10]키(key)가 숫자인 경우 딕셔너리로 감싸주는 것 대신-->리스트(List),튜플(Tuple)로 감싸주는 방법도 가능.
print('-'*120,'[10]')
testDict10={1:'잇지',2:'오마이걸',3:'스테이씨',4:'로켓펀치'}
# testDict10.update([1:'프로미스9']) #Error-->콜론(:)을 콤마(,)로 바꿔줘야 함.
# testDict10.update([1,'프로미스9']) #Error-->리스트를 다시 리스트로 감싸줘야 함.
testDict10.update([[1,'프로미스9'],[2,'레드벨벳']])
print('testDict10',testDict10)

#[11]딕셔너리는 순서가 없다-->따라서,인덱스가 아닌 키(key)로 엑세스 한다
print('-'*120,'[11]')
testDict11={'aaa':100,'bbb':200}

#print(testDict11[0]) #Error-->인덱스로 접근하려 했긴 때문
print(testDict11['aaa']) #100
print(testDict11['bbb']) #200

#값(value)을 수정하는 것도-->키(key)로 접근하여 수정.(만약, 없는 키를 입력해서 수정하려고 하면-->입력으로 처리!)
testDict11['aaa']=1000
testDict11['bbb']=2000
testDict11['ccc']=3000
print('testDict11',testDict11)

















