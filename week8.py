############ function 함수 강의 내용

## 3page
score = [71, 55, 24, 73, 68, 90]
# coding here 
cnt = 1
for i in score:
   if i > 70:
      print('%d번 학생 합격'%(cnt))
   cnt +=1
      

## 4page
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school' 'hotel', 'india']

## coding here ##

b=[]
for i in a:
   if len(i) ==5:
      b.append(i)
print(b)



## 5page
capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이","덴마크":"코펜하겐"}
for i in capital:
   if len(capital[i==2]):
      print('%s의 수도는 %s입니다.'%(i, capital[i]))


## 6page
sum = 0
num = 3**79
for i in str(num):
   sum += int(i)
print(sum)



## 7page
string = "apple"
alphabet = []
for i in string:
   if  i not in alphabet:
      alphabet.append(i)

print(alphabet)



## 22page

def how_many(a,b):
   cnt = 0
   for in in a:
      if i ==b:
         cnt += 1
   return cnt

x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]
print(how_many(x,3))
print(how_many(x,5))


## 23page

def bigger_than(a,b):
   count = 0
   for i in a:
      if i>b:
         count +=1
   return count

x = [1,3,2,5,9,0,2,3,5,6,2,3,1,8,9,3,4,1,7,6,3]
print(bigger_than(x,4))
print(bigger_than(x,5))


## 별 그리는 문제 함수로 푸는 법
def draw_star(x):
   for i in range(x):
      print('*'*x)

draw_star(15)


## 24page
student = [12,18,3,20,14,5,1,9,10,11,6,2,17,16,4,15,8]

res = Check(student)

def Check(list):
   for i in range(1,21):
      if i not in list:
         res.append(i)
      return res

print(res)


## 25page

def find_capitalcity(capital, country):
   return capital[country]

capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이","덴마크":"코펜하겐"}

print(find_capitalcity(capital, "대한민국"))
print(find_capitalcity(capital, "덴마크"))
print(find_capitalcity(capital, "미국")) 


## 26page
def pickup_even(items):
   x=[]
   for i in items:
      if i % 2 ==0:
         x.apprend(i)
   print(x)
   return

pickup_even([3, 4, 5, 6, 7, 8])


## 27page
def find_character(string,k):
   print(string[k-1])
   return

find_character("computer",2) # o 출력
find_character("happy",1) # h 출력
find_character("data",3) # t 출력
