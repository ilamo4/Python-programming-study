### 예시1 ###
# for i in range(5):
#     print('**********')
# #또는
# for i in range(5):
#     print('*'*10)

# for i in range(5):
#     print(i)
    # print('hi')

#range 안의 숫자만큼 i라는 것을 5번 반복하자. i=0 , print 안에 i를 넣으면 i에 0,1,2,3,4가 한 줄씩 차례대로 출력됨.
#range()안의 숫자가 1개만 있으면 0부터 그 횟수만큼 반복. range(3,5)는 3,4만 나옴. range(5,101)이면 5부터 100까지 출력.
#range(1,10,2)는 2씩 건너뛰고 1부터 9까지 출력하라는 뜻.
#range 안에는 원래 숫자 3개 씌여있지만 원래 1칸씩 건너뛰니까 맨 뒤에것 생략. 그리고 ㅐ부터 시작하면 맨 앞에것 생략.

# for i in range(5):
#     print(i)
    # print('hi')

# cnt = 0
# for i in range(3,10):
#     print(i)
#     cnt +=1 ### cnt = cnt+1 (복합대입연산자)
#     print(cnt)

## 위의 코드에서 print(cnt)를  for문 속 어디에 넣느냐에 따라 실행결과가 달라질 수 있다.


### 예시2 ###
# for i in range(1, 6) :
#     print('*'*i)
##또는는
# for i in range(6):
#     print ('*'*(i+1))


### 예시3 ###

# for i in range(6) :
#     print('*'*(5-i))


### 예시4 ###

# for i in range (1,31) :
#     if i % 3 == 0 :
#         print(i)

# for문을 활용한 반복적인 덧셈에서 변수의 초깃값 선언해주자.
#누적 덧셈
#1부터 10까지 더하는 예시
# res = 0
# for i in range(1, 11, 1) :
#     res = res + i
# print("1에서 10까지의 합 = \n", res)

#res는 result라는 변수이다.
# res = 0
# for i in range(1,11):
#     res = res + i

#누적곱셈
# res = 0
# for i in range(1,11):
#     res = res * i
# print(res)

# res = 0 
# for i in range(1,11):
#     if i % 2 == 0:
#         res += i
# print(res)

# # for i in range(1,11,2): 홀수 구할 때
# # for i in range(0,11,2): 짝수 구할 때
# # 그래도 반복문 안에 if 절 넣어서 코드 짜자.


### 예시5  팩토리얼 값 구하기 ###

# num = int(input('2 이상의 숫자를 입력해 주세요 : '))
# fact=1
# for i in range(1,num+1):
#     fact = fact * i
# print(fact)
    
### 예시6 ### 구구단 구하기 빈출!

# i = 0
# dan = 0
# dan = int(input('구구단 몇 단을 계산할까요? : '))
# for i in range(1,10)   :
#     print("%d x %d = %d"%(dan,i,dan*i))

### 예시7 ### 이중for문으로 구구단 쓰기
#이중 for문의 실행 횟수: 바깥 for문 반복 횟수 ×안쪽 for문 반복 횟수

# for i in range(2,10):
#     for j in range(1,10):
#         print('%d x %d = %d'%(i,j,i*j))

########################################################################################################################
#while문은 초깃값 i를 while문 앞에 선언해줘야한다.

#while문 예시 1
# i=0
# while i<5:
#     print(i)
#     i += 1

#while문 예시 2
# i=0
# while i<5:
#     print('*'*10)
#     i = i+ 1
#for문을 while문으로 바꿀 수 있다.
#모든 for문은 while문으로 바꿀 수 있고 모든 while문은 for문으로 바꿀 수 있다.
# res = 0
# for i in range(1,11):
#     res = res + i

##위의 for문을 while문으로 바꿔주면..

# res =0
# i =0
# while i<11:
#     res +=i
#     i += 1
# print(res)

#while문 예시 3
# password = 'data'
# answer = input('비번 :')
# if answer == password:
#     print("정답")
#이 코드를 while문을 통해 정답을 맞힐 때까지 코드를 동작시킬 수 있다.


# password = 'data'
# answer =''
# while answer != password:
#     answer = input('비번 :')
# print("정답")


### 예시8 ###

# i =0
# while i<5:
#     print('*'*10)
#     i +=1

### 예시9 ###
##for문으로 코드 짜면
# res=0
# for i in range(1,101):
#     res += i
# print(res)

##while문으로 코드 짜면
# res=0 
# i=1
# while i<101:
#     res +=1
#     i +=1
# print(res)



### 예시10 ### (30과 75의 최대 공약수를 출력해라.) while문 hard

# res =3
# if 30 % res ==0 and 75 % res ==0:
#     print('30과 75의 공약수')


##for문으로 코드 짜면
# res =1
# for i in range(1,31):
#     if 30 % i ==0 and 75 % i ==0:
#         res = i
# print(res)


##while문으로 코드 짜면
# res =1
# i =1
# while i<31:
#      if 30 % i ==0 and 75 % i ==0:
#          res = i
#     i += 1
# print(res)