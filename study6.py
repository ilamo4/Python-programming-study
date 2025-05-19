# 6주차 스터디 warm-up (백준 2480)

a,b,c = map(int, input().split())

if a==b==c:
    print(10000+a*1000)
elif a==b:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
elif c==a:
    print(1000+c*100)
else:
    print(max(a,b,c)*100)


#6주차 스터디 문풀 (2차 시험 대비)

#1 hard...
n = int(input())

if n == 0:
    pos_str = "zero이고"
    is_prime = False
else: 
    if n % 2 == 1:
        pos_str = " 홀수이고"
    elif n % 2 == 0:
        pos_str = " 짝수이고"

    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break

if is_prime == True:
    prime_str = "prime입니다."
else: prime_str = "prime이 아닙니다."

print("%d은 %s %s" % (n, pos_str, prime_str))


#2
evens_sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i

print('1부터 100까지의 짝수 합은 ', even_sum, '입니다.', sep='')


#3
students = input('몇 명에 대한 입력을 받겠습니까?')
names =[]
scores =[]

for i in range(students):
    name = input("학생 %d 이름: " % (i+1))
    score = int(input("학생 %d 성적: " % (i+1)))
    names.append(name)
    scores.append(score)


max_score = max(scores)
max_index = scores.index(max_score)
top_score_student = names[max_index]
average_score = sum(scores) / len(scores)
print('최고 점수 학생은' , top_score_student '이며,평균 점수는', round(average_score,1), '입니다.', sep ='')


#4 hard...





#5
data = input().split()  # 입력 받아 공백 기준으로 나눔

scores = {}

# 과목과 점수 딕셔너리에 저장
for i in range(0, len(data), 2):
    subject = data[i]
    score = int(data[i + 1])
    scores[subject] = score

# 전체 평균 계산
total_avg = sum(scores.values()) // len(scores)

# 평균 이상 과목 찾기
above_avg_subjects = []
above_avg_scores = []

for subject, score in scores.items():
    if score >= total_avg:
        above_avg_subjects.append(subject)
        above_avg_scores.append(score)

# 평균 이상 과목의 평균
above_avg = sum(above_avg_scores) // len(above_avg_scores)

print("입력된 과목의 수는 %d이고, 평균은 %d입니다." % (len(scores), total_avg))
print("평균 이상의 과목은 %s입니다." % ', '.join(above_avg_subjects))
print("평균 이상의 과목의 평균은 %d입니다." % above_avg)


#6
nums = list(map(int, input().split()))

same_banned = []
for num in nums:
    if num not in same_banned:
        same_banned.append(num)

same_banned.sort()

print(same_banned)

#7
nums = list(map(int, input().split()))
cnt = int(input())

if cnt in nums:
    print(nums.index(cnt) + 1)
else:
    print("없음")

#8
people = input().split()
dict ={}

for i in range(people):
    name = people[i]
    age = int(people[i+1])
    dict[name] = age

check= input()
if check in dict:
    print(check, "는 ", d[check], "살입니다.", sep='')
else:
    print("없음")

print('' in dict )
