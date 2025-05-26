# 2차 시험

##### 1번 문제 #####

# num = 3/813
# res = 0


# print(res)


##### 2번 문제 #####

# name = ['hello','trip','pho','airplane','zebra']

# for i in name:



##### 3번 문제 #####

# def draw_star(n):
#     i=1
#     while i <= n:


# draw_star(3) ## 결과 확인용
# draw_star(4) ## 결과 확인용


##### 4번 문제 #####

# student = {"Alice": 88, "Julia":68, "Bob": 95, "Tony": 97,  "David": 90}

# max_score=0
# max_name=''

# for k,v in student.items():


# print(max_name, max_score)
         


##### 5번 문제 #####
# def count_space(a):




# sentence = 'Python is powerful and interesting for me.'
# num = count_space(sentence)
# print(sentence)
# print('빈칸의 개수 : ', num)



##### 6번 문제 #####

# scores = [91,74,82,98,56,49,26,87,93,55]
# high =[]
# for i in scores:
#     if i>=80:



# print(high)




##### 7번 문제 #####

# def extract_even_index_letters(x):
#     res =[]
#     for i in x:
#         res.append(i[0])
#     return res

# input_data = ["apple", "blue", "captain", "dry"]
# result = extract_even_index_letters(input_data)
# print(result)

##### 8번 문제 #####

# sentence = "Python is fun but sometimes annoying and slow"
# banned_words = ["annoying", "slow"]

### coding here ###


# x=sentence.split()
# new=[]
# for i in x:
#     if i in banned_words:
#         i ='***'
#     new.append(i)
# result=' '.join(new)

# print(result)

##### 9번 문제 #####

# answer = 25

# ## coding here ###

# while True:
#     if num == answer:
#         print('correct')
#         break
#     elif num < answer:
#         print('up')
#     elif num > answer:
#         print('down')
    
# num = int(input('0부터 50사이 숫자 입력:'))


### 객체지향프로그래밍 수업 내용 

# 객체(instance)란?  어떤 속성과 행동을 가지고 있는 데이터.
# 클래스란? 객체를 만드는 틀.

# class Car:
#     color = ''
#     speed = 0
# car1 = Car()
# car1.color = 'red'
# car1.speed = 0

# car2=Car()
# car2.color = 'yellow'
# car2.speed = 10


# # 생성자

# car1=Car()


# def __init__(self,a,b,c) :
#      self.color = a
#      self.speed = b
#      self.model = c



# 자기소개 객체 만들기

# class Student:
#      age=0
#      mbti=''
#      name=''

#      def __init__(self,x,y,z):
#           self.name = x
#           self.mbti = y
#           self. age = z 

#      def hello(self):
#           print('안녕하세요 제 이름은 %s입니다.'%(self.name))

# person1 = Student('김태완','ISTJ',20)



# # 2차 시험에 출제된 함수를 읽을 수 있어야 한다. 함수가 무엇을 리턴하는지.


# # 상속 
# class Truck(Car):
#      price=0



#1

class Human:
     name =''
     age = 0
     gender = ''
     def __init__(self,a,b,c):
          self.name = a
          self .age = b
          self .gender = c
     def who(self):
          print('이름:%s,나이:%d,성별:%s' %(self.name, self.))
areum = Human("아름", 25, "여자")

print(areum.name)
print(areum.age)
print(areum.gender)


#2

areum = Human("아름", 25, "여자")


areum.who()
del(areum)



#3
class 차:
     바퀴 = 0
     가격 =0

     def __init__(self,a,b):
          self.바퀴 =a
          self.가격 = b


car = 차(2, 1000)
print(car.바퀴)
print(car.가격)


#4


#5
class Animal:
    name =''
    def __init__(self, name):
         self.name = name


class Dog(Animal):
     def speak(self):
          message = '%s 멍멍'


class Cat(Animal):

class Cow(Animal):



animals = [Dog("바둑이"),Cat("나비"),Cow("순이")]

for animal in animals:
     print(animal.speak())

#6
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = {} # 과목명: 점수
    def add_score(self, subject, score):
        self.scores[subject] = score

    def get_average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)
    def print_scores(self):
        print(f"[{self.name}]의 성적표:")
        for subject, score in self.scores.items():
            print(f" -{subject}: {score}점")
            print(f"> 평균 점수: {self.get_average():.2f}점\n")


student1 = Student("김민지")
student1.add_score("수학", 95)
student1.add_score("영어", 88)
student1.add_score("과학", 92)
student1.print_scores()

student2 = Student("이준호")
student2.add_score("국어", 80)
student2.add_score("영어", 85)
student2.print_scores()
