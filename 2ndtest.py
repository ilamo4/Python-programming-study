##### 2025-1학기 파이썬프로그래밍 (A0019 2차시험) #####
# ----------------------------------------------------------------------------------------------------------
# 다음과 같은 행위를 부정행위로 간주하며, 온라인 시험 부정행위에 대해서는 관련자 모두를 0점(F)처리하고 학칙에 따라 징계처분 될 수 있으니 유념하시기 바랍니다.
# (1) 시험 중 문제나 답안을 전화, SNS, 단톡방, 문제풀이 사이트 등을 통해 공유하는 행위
# (2) 시험도중 시험화면을 이탈하거나 특수키(Ctrl, Alt, Window key 등) 사용, 다른 프로그램을 사용하는 행위
# (3) 오픈북 시험이 아닌데 교재나 시험관련 자료를 펴놓고 시험을 보는 행위
# ----------------------------------------------------------------------------------------------------------

# 본인은 온라인 시험 관련 모든 유의사항을 확인하였고 부정행위를 하지 않을 것이며, 부정행위를 하였을 경우에는 0점(F학점)을 감수하며 학칙에 따른 징계절차에 따르겠습니다.
# 위의 사항에 동의할 경우 아래 대답에 "동의합니다" 라고 작성해 주십시오.

##### 대답 : 동의합니다
##### 학번 : 20250987
##### 이름 : 박소은


##### 1번 문제 #####

# num = 3/813
# res = 0

# num_str = str(num).split('.')[1]

# for digit in num_str:
#         res += int(digit)

# print(res)


##### 2번 문제 #####

# name = ['hello','trip','pho','airplane','zebra']

# for i in name:
#     print(i,len(i))

## 각 단어 출력하려면 print문 안에 i, 단어의 길이 출력하려면 len(i), 첫 글자를 출력하려면 i[0] .

##### 3번 문제 #####

# def draw_star(n):
#     i=1
#     while i <= n:
#             spaces = ' ' * (n-i)
#             stars = '*' * (2*i-1)
#             print(spaces+stars)
#             i +=1


# draw_star(3) ## 결과 확인용
# draw_star(4) ## 결과 확인용


##### 4번 문제 #####

# student = {"Alice": 88, "Julia":68, "Bob": 95, "Tony": 97,  "David": 90}

# max_score=0
# max_name=''

# for k,v in student.items():
#     if v > max_score:
#         max_score = v
#         max_name = k

# print(max_name, max_score)
         

##### 5번 문제 #####

# def count_space(a):
#     count = 0
#     for ch in a:
#         if ch == ' ':
#             count += 1
#     return count

# sentence = 'Python is powerful and interesting for me.'
# num = count_space(sentence)
# print(sentence)
# print('빈칸의 개수 : ', num)


##### 6번 문제 #####

# scores = [91,74,82,98,56,49,26,87,93,55]

# high=[]

# for x in scores:
#     if x >= 80:
#         high.append(x)

# print(high)


##### 7번 문제 #####

# def extract_even_index_letters(x):
#     result = []
#     for word in x:
#         result.append(word[0])  # 각 단어의 첫 글자(인덱스 0)만 추가
#     return result

# input_data = ["apple", "blue", "captain", "dry"]
# result = extract_even_index_letters(input_data)
# print(result)


##### 8번 문제 #####

# sentence = "Python is fun but sometimes annoying and slow"
# banned_words = ["annoying", "slow"]

# for word in banned_words:
#     sentence = sentence.replace(word, "***")

# print(sentence)



##### 9번 문제 ##### (아예 모르겠음.)

# answer = 25

# num = int(input('0부터 50사이 숫자 입력:'))
### coding here ###
