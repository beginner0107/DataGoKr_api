#딕셔너리 자료구조와 반복문2-중첩 딕셔너리와 for반복문

#[1]딕셔너리 선언-->2가지 방법-->(1)빈 중괄호({})를 사용. (2)dict생성자를 사용.
print('-'*120,'[1]')

#(1)빈 중괄호 사용
testDict1={} #set중괄호를 이용하는 것이지만 타입 체크를 해보면 dict로 나옴.
print(type(testDict1)) #dict

#(2)생성자사용
testDict1_2=dict(tiger=2,lion=4,aligator=7,hippo=9)
print(testDict1_2)
print(type(testDict1_2))

#[2]딕셔너리 변환-->"키(key):값(value)"쌍을 맞춰만 준다면 리스트, 튜플을 딕셔너리로 변환할 수 있음
print('-'*120,'[2]')

#(1)리스트를 딕셔너리로.
animals=[['Tiger',3],['Lion',4],['Aligator',10]]
animals_dict=dict(animals)
print(animals_dict)
print(type(animals_dict))

#(2)튜플을 딕셔너리로.
goods=(('book',10000),('bag',20000),('purse',30000))
goods_dict=dict(goods)
print(goods_dict)
print(type(goods_dict))

#(3)리스트 안에 튜플을 딕셔너리로-->반대도 가능-->튜플안에 리스트를 딕셔너리로.
worms=[('cockroach',10),('cricket',20),('centipede',30)]
worms_dict=dict(worms)
print(worms_dict)
print(type(worms_dict))

#[3] %s,%d,%f-->출력 서식 기호
print('-'*140,'[3]')

fruits={'apple':10,'pear':5,'peach':20}

for key,value in fruits.items():
    print("%s:%d"%(key,value),end=' ')
print()

for key in fruits.keys():
    print("%s:%03d"%(key,fruits[key]),end=' ')
print()

#[4] 키(key)와 값(value)직접 추가
print('-'*140,'[4]')

goods={
    'price':50000,
    'computer':['print','monitor','ram','hdd'],
    'vegetable':['cabbage','cucumber','carrot','lettuce']
}

# goods.setdefault('office')
goods['fruit']=['pear','orage','peach','apple']
print(goods)

#[5] 키(key)와 값(value)직접 추가
print('-'*140,'[5]')
print(goods) 
goods['fruit'].remove('apple')
print(goods)

goods['fruit'].append('new-apple')
print(goods)

#항목을 완전 삭제-->del
del goods['fruit']
print(goods)

#[6]연산
print('-'*140,'[6]')
print(goods)
print(goods['price']+10000)

#[7]정렬-->sort()메서드 사용.
print('-'*140,'[7]')
testDict7={
    'a':[4,1,3,7,9,5,6],
    'b':['f','t','g','c','a','w','p']
}

print(testDict7)
# testDict7['a'].sort() #오름차순 정렬이 되어 있었기 때문에 reverse했을 때 내림차순 정렬
# testDict7['b'].sort()
# testDict7['a'].reverse()
# testDict7['b'].reverse()
testDict7['a'].sort(reverse=True) #바로 역순으로 정렬해줌.
testDict7['b'].sort(reverse=True)
print(testDict7)

#[8]2개의 딕셔너리 반복
print('-'*140,'[8]')

testDic8_1={'name':'로켓펀치','member':6}
testDic8_2={'name':'잇지','member':4}

groups=[testDic8_1,testDic8_2]

for idol in groups:
    print(idol['name'],idol['member'])

#[9]카운트 세기-->요소별로 카운트를 딕셔너리로 만들기
print('-'*140,'[9]')

numbers=[3,4,1,5,8,4,2,6,7,9,8,2,3,2,5,7,8,9,4,3,6,5,8,1,6,9,2]
cnt={}

for num in numbers:
    if num in cnt:
        cnt[num]+=1
    else:
        cnt[num]=1
print(cnt)

#[10]중첨 딕셔너리 반복
print('-'*140,'[10]')

idol_group={
    "name":"스테이씨",
    "member_num":6,
    "members":{
        "member1":"수민",
        "member2":"시은",
        "member3":"아이사",
        "member4":"세은",
        "member5":"윤",
        "member6":"재이"
    },
    "features":["노래","연기","춤"]
}

# for key in idol_group:
    # print(key)
    # print(type(idol_group[key]))

for key in idol_group:
    if(type(idol_group[key])==dict):
        for key1 in idol_group[key]:
            print(key1,"의 이름은:",idol_group[key][key1])
    elif(type(idol_group[key])==list):
        for item in idol_group[key]:
            print(key,":",item)
    else:
        print(key,":",idol_group[key])

























