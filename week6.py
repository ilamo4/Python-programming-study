## 1번 문제 ##
greetings = ['안녕','니하오','하이','곤니찌와','올라','싸와디캅','봉쥬르']

#range 쓰지 말고 리스트 이름을 for문에 작성해라.

# for i in greetings:
#     print (i)

#한 줄씩 띄어쓰기 안하려면 print(i, end='')로 코드 작성하기.

# print(len(greetings))

##############
# tttt=[]

# for i in greetings:
#     if len(i) == 2:
#         tttt.append(i)

    
#         # print(i)

# print(tttt)

#########
# x='동덕여대데사'
# for i in x:
#     print(i)

###########
# x=[]
# y=[]
# for i in range(1,101):
#     x.append(i)

# for i in range(1,101):
#     y.append(x[100-i])

# print(y)

#######################


## 2번 문제 ##
# a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school' 'hotel', 'india']

# ## coding here ##
# b=[]
# for i in a:
#     if len(i) == 5:
#         b.append(i)

# print(b)



## 3번 문제 ##
# a = [1, 11, 40, 24, 67, 22, 19, 24, 88]
# res=0
# for i in a:
#     if i<30 and i>10:
#         res += 1

# print("원소의 개수는 %d 입니다"%res)



## 4번 문제 ## 4번 다시 풀기기
#way1

# name = ['hello','trip','pho','airplane','zebra']
# cnt=1
# for i in name:
#     cnt += i
#     print(cnt,i)

# #way2

# for i,j in enumerate(name):
#     print(i+1,j)





## 5번 문제 ##
# a = [1, 11, 80, 24, 67, 32, 19, 24, 88]
# res = 0

# for i in a:
#     if i % 2 == 0:
#         res +=1
# print(res)


###################################################################################

# x={'kim':100, 'lee':90, 'park':77}
# print(x['kim'])

#출력값에 중괄호가 있으면 딕셔너리다..



## 6번 문제 ##

# score = {'국어': 90, '영어':95,'수학':77, '미술':68, '과학': 82}
# sum = 0
# average = 0.0
# for i in score:
#     sum += score[i]
#     print("%s 과목의 점수는 %d 입니다."%(i,score[i]))
# average = sum/len(score)
# print("전체 평균은 %f 입니다."%average)






## 7번 문제 ## (작년 시험문제)

# visit = ['영국','일본','미국','프랑스','폴란드','칠레','캐나다','이탈리아']
# wish = ['브라질', '독일', '캐나다', '호주', '영국']
# result = []

# for i in wish:
#     if i in visit:
#         result.append(i)

# print(result)




## 8번 문제 ##
scores = {'math': 82, 'english': 91, 'science': 78}

#way1
max_key=''
max_value=0

for i in scores:
    if scores[i] > max_value:
        max_value = scores[i]
        max_key = i
print(max_key)

#way2
max_key=''
max_value=0
for k,v in scores.items():
    if v > max_value:
        max_value = v
        max_key = k
print(max_key)

