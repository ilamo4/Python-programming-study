# a=10

# if a>1:
#     print(a)
#     print('1보다크다')
# print('끝')

# x='hello'
# y='hello'

# if x==y :
#     print('정답')



# num = int(input('숫자 하나 입력해주세요: '))
# if num % 2 == 0 :
#     print('짝수')

# math = 83
# science =90
# if math >= 80 and science >= 80:
#     print('합격')


# math = 83
# science = 90
# if math < 85 or science < 85:
#     print('탈락')

# num = int(input('숫자 입력: '))
# if num % 5 == 0 and num % 7 == 0:
#     print('35의 배수')


# #10과 15의 공약수
# num=5
# if 10 % num == 0 and 15 % num == 0:
#     print('정답')

# a=1

# if a > 5:
#     print('5보다크다')
# else:
#     print('5보다작다')

# print('끝')



# if a % 2 ==0:
#     print('짝수')

# if a % 2 ==1:
#     print('홀수')
# 바로 위의 질문을 안 하기 위해서 else를 사용한다.

# math = 83
# science = 90
# if math > science:
#     print ('math')
# else:
#     print('science')

# num = int(input('숫자 입력: '))
# if num % 2 ==0 and num >10 :
#     print('x')
# else:
#     print ('o')



# year = int(input('연도를 입력하세요: '))
# if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0) :
#     print('%d년은 윤년입니다.'%year)
# else:
#     print('%d년은 윤년이 아닙니다'%year)


# if a > 3: 
#     print ('3보다작다')
# elif a < 0:
# #     print('0보다작다')
# else:
#     print('0보다 크고 3보다 작다')


# price = int(input('주문 금액: '))
# delivery_fee = -1

# if price >= 50000:
#     print('배달비 무료료')
# elif price >= 30000:
#     delivery_fee = price * 0.05
# elif price >= 10000:
#     delivery_fee = price * 0.1
# else:
#     print('배달 불가')

# print('배달비는 %d원입니다.'%delivery_fee)



speed = 100
if speed > 100:
    print('면허정지')
elif speed >= 81:
    print('과속')
elif speed >= 51:
    print('과속')
else:
    print('정상')


x=42
user_number = int(input('1부터 100 사이의 숫자를 입력하세요: '))
if user_number < x:
    print('더 큰 숫자를 입력하세요!')
elif user_number > x:
    print('더 작은 숫자를 입력하세요!')
else:
    print('정답입니다! 축하합니다!')
