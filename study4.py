#4주차 스터디 waum-up (백준 10817)

#.sort()를 사용하여 리스트의 항목을 작은 것부터 큰 순으로 정렬하였다. 
# 세 정수 A, B, C가 공백으로 구분되어 주어지므로 정수형 int를 사용하였고 띄어쓰기를 기준으로 입력받은 값을 나누었다.

# num = list(map(int,input().split()))
# num.sort()
# print(num[1])




#4주차 스터디 문제 풀이

#1 파이썬에서 연산자는 값이 같고 자료형(타입)도 같아야 같은 것이다.
# false

#2 
# s= 'abc'
# print(s+'123')


# #3
# print('ha'*3)

# #4
# s = input()
# print(len(s))

# #5
# print('hello'.upper())

# #6
# print('Python Is Fun'.swapcase())

# #7
# print('welcome to my place'.title())

# #8
# s= input()

# if s.isupper():
#     print('대문자입니다.')
# elif s.islower():
#     print('소문자입니다.')
# elif s.isdigit():
#     print('숫자입니다.')

# #9
# print('banana'.count('a'))


# # #10 모르겠. 틀림. 어려움. 아직 안 고침...
# print('o의 첫 번째 인덱스는', 'hello world'.find('o'),'이고, 마지막 인덱스는' , 'hello world'.rfind('o')'입니다'', sep = '' )

#10번 정답: print("o의 첫 번째 인덱스는 ", "hello world".find('o'), "이고, 마지막 인덱스는 ", "hello world".rfind('o'), "입니다.", sep='')


# #11
# print('a,b,c'.split(','))

# #12
# print(" ".join(['hi', 'i\'m', 'genie']))


# #13
# s = 'hello  world'
# print(s.strip())


# #14 모르겠

# s = input()
# s1 = s.find('@')
# s2 = s.find('@', s1 +1)
# if s1 == -1:
#     print('없음')
# else:
#     print(s2)


# #15
# print('###data#science###'.strip('#'))

# #16 공백수 출력하는 것 모르겠. 아예 못 품.

#  replace()는 문자열 변경에 쓰임.
#ex. print(word.replace('공부', '놀기')) -----공부라는 문자열을 운동으로 변경.

##정답 
# s = input().replace(" ", "")
# index = s.find('a')

# while index != -1:
#     print(index, end=' ')
#     index = s.find('a', index + 1)

# #17 공백수 출력하는 것 모르겠.아예 못 품. 공백수제거: strip() lstrip() rstirp()
#자우림노래 매직카펫라이드 스트립쇼..공백을 없앤다.
#맨 앞의 공백수를 변수 left라 하고, 맨 뒤의 공백수를 변수 right라 
#정답
# s = input()

# left = len(s) - len(s.lstrip())
# right = len(s) - len(s.rstrip())
# print(left, right)

# #18
# email = input()

# #19
# s = input().strip()
# print(s[0] == s[-1])

# #20
# words = input().split()
# res =[]
# for word in words:
#     if word[0].lower() == word[-1].lower():
#         result.append(word.title())

# print(', '.join(res))

# join 앞에 들어가는 문자를 리스트 요소 사이사이에 넣어서 리스트를 만드는 것.
#split과 join의 역할은 반대이다. split은 문자열 분리. join은 문자열 결합.





