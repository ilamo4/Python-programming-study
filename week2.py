#print('hi')

##출력함수 배운거 
#세모 플레이 표시 눌러야 실행됨
#주석처리, 주석풀기 하는 법 배움.

#주석처리 전체적으로 할 때

## 주석처리 ctrl+kc
## 주석풀기 ctrl+ku

#은 하나만 써도 실행안됨 (수업내용 적을 때 유용. 왜냐면 코드 안 돌아감.)

#터미널 칸 삭제하면 실행된 목록 삭제됨
#print(2+5)
#print('2+5')
#따옴표의 역할: 글자. 계산 안 됨
#따옴표 작은 따옴표, 큰 따옴표 상관없음음
#print('%d점 입니다.' %100)
#print('당신의 학점은 %c입니다 %A+')
#d는 숫자를 의미. 문자열은 c는 한글자일때. 여러글자는 s 이용
#따옴표 안의 %
#입니다 등 띄어쓰기 정확하게 하기

# print ('수학점수 %d,영어점수 %d' %(90,80))

# print('%d+%d = %d' %(200,100,200+100))

# print('%d+%d = %d' %(200,100,200+100))
# %d는 정수만 가능 %f는 소수점 표현 가능

# a=3
# b=1
# c=a+b
# print(c)
# print(a+b)
# print('%d'%c)
#순차적으로 써야 함. b=1을 나중에 쓰면 a+b 실행 안됨
#이제 이스케이프 문자에 대해 알아보자
#print('hi\n')
#backspace 밑의 원화모양 버튼이 역슬래시 버튼
#따옴표가 적혀있는 문장을 출력하고  싶을 때 기본세팅+ "" 앞에 역슬래시 붙이기

# price=100
# # score_math=100
# #변수 명확하게 정해라
# #변수명 같으면 덮어쓰기 됨. 위 경우에 4 10 차례로 출력됨.
# #변수 썼으면 변수 이용해서 출력함수 써라.
# print(price,'원')

# a=1
# b=2
# c=3
# print(a,b,c)
# print(a,b,c,sep='+')
# #print 함수는 원래 한칸씩 띄어쓰기 되서 출력됨. sep=의 역할: 사이 사이에 넣어줌. 

#4가지의 기본 데이터형 (정수와 실수의 계산 중 나누기 특히 신경 쓰기)
#true와 false가 코딩의 기본

# a=1
# b=2,5
# c='hi'
# d=False
# print(type(a))

# # *가 곱하기 표시임. shift 8

# print('name')
# print(type(Name))

#띄어쓰기 중요 출력될 때 그대로 나옴.
#문자열
# print('동덕'*3)
# print('동덕'+'여대')

# x= 100>10
# print(x)
#위의 경우 x의 참, 거짓이 나옴. true와 false로

#변수의 역할:그릇. 변수명 쓸 때 왼쪽에 붙여서 해야함. 오른쪽에 할당값 적기.
#대문자, 소문자가 다르게 출력됨.love와 Love는 다름. 
#변수앞에 숫자 붙이는 것도 금지.변수명은 영어로.한글사용X

# score_math=88
# score_science=90
# print(score_math+score_science)

# love=100
# Love=99
# print(love, Love)

# age=input('당신은 몇 살 입니까?')
# print(age)
# print(type(age))

# #print(age+10) 이런 식으로 문자와 숫자 더하기 불가능 
# #input 함수에서는 모든 데이터를 문자열 (str)로 인식

# #int로 감싸면 숫자로 출력됨. 코드는 겉에서부터 보자.
# #float로 감싸면..?

# x=90
# y=float(x)

# print('## 택배를 보내기 위한 정보를 입력하세요. ##')
# name = input('받는 사람:')
# addr = input('주소:')
# weight = input('무게(g):')
# price = weight *5

# print(' ** 받는 사람 ==> %s' %name)
# print(' ** 주소 ==> %s' %addr)
# print(' ** 배송비 ==> %d원' %price)
