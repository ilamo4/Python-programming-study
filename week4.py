### 학번:              이름: 박소은은


### 예시1 ###
### coding here ###


# for i in range(5):
#     print('***********')  or
#     print('*'*10)

# for i in range(5):
#     print(i)
    # print('hi')

#range 안의 숫자만큼 i라는 것을 5번 반복하자. i=0 , print 안에 i를 넣으면 i에 0,1,2,3,4가 한 줄씩 차례대로 출력됨.
#range()안의 숫자가 1개만 있으면 0부터 그 횟수만큼 반복. range(3,5)는 3,4만 나옴. range(5,101)이면 5부터 100까지 출력.
#range(1,10,2)는 2씩 건너뛰고 1부터 9까지 출력하라는 뜻.
#range 안에는 원래 숫자 3개 씌여있지만 원래 1칸씩 건너뛰니까 맨 뒤에것 생략. 그리고 ㅐ부터 시작하면 맨 앞에것 생략.


# cnt = 0
# for i in range(3,10):
#     print(i)
#     cnt += 1 ### cnt = cnt+1 (복합대입연산자)

# print(cnt)


### 예시2 ###
# for i in range(1, 6) :
#     print('*'*i)

# for i in range(6):
#     print ('*'*(i+1))



# for i in range(10):
#     if i % 2 == 0:
#         print (i)


### 예시3 ###

# for i in range(6) :
#     print('*'*(5-i))



### 예시4 ###

# for i in range (1,31) :
#     if i % 3 == 0 :
#         print(i)

# p11
# cnt =0
# for i in range(1,11):
#     cnt += 1
# print(cnt)

# res = 0

# for i in range(1,11):
#     res = res * i
# print(res)

# res = 0

# for i in range(1,11):
#     res = res + i

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

### coding here ###

    
### 예시6 ###

# i = 0
# dan = 0

# dan = int(input('구구단 몇 단을 계산할까요? : '))

# for i in range(1,10)   :
#     print("%d x %d = %d"%(dan,i,dan*i))


# for i in range(5):
#     for j in range(3):
#         print(i,j)



### 예시7 ###

# for i in range(2,10):
#     for j in range(1,10):
#         print('%d x %d = %d'%(i,j,i*j))

##############################################################################################

# for i in range(5):
#     print(i)

# i=0
# while i<5:
#     print(i)
#     i += 1

# i=0
# while i<5:
#     print('*'*10)
#     i = i+ 1

# res = 0

# for i in range(1,11):
#     res = res + i


# res =0
# i =0
# while i<11:
#     res +=i
#     i += 1
# print(res)

# res =0
# i =0
# while i<11:
#     i += 1
#     res +=i
# print(res)


# password = 'data'
# answer = input('비번 :')
# if answer == password:
#     print("정답")


# password = 'data'
# answer =''
# while answer != password:
#     answer = input('비번 :')
# print("정답")


### 예시8 ###
### coding here ###

# i =0
# while i<5:
#     print('*'*10)
#     i +=1

# i =0
# while i<10:
#     print(i)
#     i += 1
#     if i>5 : break


# for i in range(3,10):
#     print(i)
#     if i>8: break


# for i in range(1,31):
#     if i % 3 !=0:
#         continue
#     print(i)

# i=1
# while i <31:
#     if i % 3 !=0:
#         i += 1
#         continue
#     print(i)
#     i += 1


### 예시9 ###
### coding here ###

# for i in range(1,100):

# res=0 
# i=1
# while i<101:
#     res +=1
#     i+= 1
# print(res)



### 예시10 ###
### coding here ###

############ my way

# for i in range(1,75):
#     if 30 % i ==0  and 75 % i ==0:
#         print(i)
# 이건 30, 75의 공약수를 구하는 과정.

# res=1
# i=1
# while i<30:
#     30 % i ==0  and 75 % i ==0
# print(i)


##################################################################################

# res =3
# if 30 % res ==0 and 75 % res ==0:
#     print('30과 75의 공약수')



# res =1
# for i in range(1,31):
#     if 30 % i ==0 and 75 % i ==0:
#         res = i
# print(res)

res =1
i =1
while i<31:
     if 30 % i ==0 and 75 % i ==0:
         res = i
    i += 1
print(res)