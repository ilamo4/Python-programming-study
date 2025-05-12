#3주차 스터디 warm-up (백준 10430 )

# 2 ≤ A, B, C ≤ 10000이므로 A, B, C를 정수형 int로 바꿔줘야 하고, input 함수로 A, B, C를 입력받을 때 
# split()을 통해 공백을 기준으로 각각 입력 받을 수 있게 해야 한다.

A, B, C = input().split()
A, B, C = int(A), int(B), int(C)
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A B) % C)
print(((A % C) (B % C)) % C)

# 맨 위의 코드 두 줄을 map 함수를 통해
# A, B, C = map(int, input().split()로 작성할 수도 있다.
# 또한 사칙연산 과정에서 계산 우선순서대로 괄호를 묶어 코드 읽기에 좋게 나타내는 것이 좋다.

#3주차 스터디 문제풀이 (리스트, 딕셔너리 문제 다시 보기)
#list는 함수이름이므로 새로운 list 이름을 문제 상황에 맞게 작성하자.
#문제 상황에 맞는 적절한 변수 이름 고민해서 코드 짜기.


#리스트 문제 10개

#1
num=[1, 2, 3, 4, 5]
print(num[-1])

#2
arr=[3, 6, 9]
arr.append(12)
print(arr)

#3
a = int(input('몇 번 입력받을래?: '))
nums =[]
for i in range(a):
    nums.append(int(input()))
print(sum(nums))

#4
nums = [1, 2, 3, 4, 5, 6]
evens = []
for n in nums:
    if n % 2 == 0:
        even.append(n)
print(evens)

#5
nums = [10, 2, 5, 8]
diff = max(nums)-mine(nums)
print(diff)

#6
nums = list(map(int.input().split()))
even =[]
odd =[]

for n in nums:
    if i % 2 ==0:
        even.append(n)
    else:
        odd.append(n)
print(even)
print(odd)

#7 hard 다시 풀어보기
words = input().split()
lengths = []
for word in words:
    if (word == words[-1]):
        print(len(word),end='')
        break
    print(len(word), end='')


#8
list = [0, 1, 0, 2, 3, 0]
print(list.count(0))

#9  hard 다시 풀어보기
num= list(map(int.input().split()))
sum = []
total = 0
for n in nums:
    total += n
    sum.append(total)
print(sum)


#10
list = [1, 2, 3, 4, 5]
print(list[:: -1])


#딕셔너리 문제 10개

#1
d = {"a": 1, "b": 2, "c": 3}
print(d["b"])

#2
d = {}
d['x'] = 10
print(d)

#3
d = {'name': 'Alice', 'age': 25}
print(d.keys())

#4
d = {'name': 'Alice', 'age': 25}
print(d.values())

#5
kor, eng, math = map(int, input().split(', '))
scores = {'국어': kor, '영어': eng, '수학': math}
print(max(scores.values()))

#6
string = input()

d = {}
for s in string:
    d[s] = d.get(s, 0) + 1
    
print(d)

#7
entries = input().split()

d = {}
for i in range(0, len(entries), 2):
    name = entries[i]
    score = int(entries[i+1])
    d[name] = score
    
avg = sum(d.values()) / len(d)

print(round(avg, 1))

#8
entries = input().split()

d = {}
for i in range(0, len(entries), 2):
    subject = entries[i]
    score = int(entries[i+1])
    d[subject] = score

for subject in d:
    score = d[subject]
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    if grade in ['A', 'B']:
        print(subject, end=' ')

#9
d = {'수학': 90, '영어': 80}
key = input()
print(d.get(key, '키 없음'))

#10
nums = list(map(int, input().split()))

d = {}
for i in range(0, len(nums), 2):
    key = nums[i]
    value = nums[i+1]
    d[key] = value
    
print(d)


#튜플 문제 5개

#1
tpl = (10, 20, 30)
print(tpl[1])

#2
tpl1 = (1, 2)
tpl2 = (3, 4)
print(tpl1 + tpl2)

#3
tpl = tuple(map(int, input().split()))
print(max(tpl))
print(min(tpl))

#4
tpl = tuple(map(int, input().split()))
avg = sum(tpl) / len(tpl)
print("%.1f" % avg)

#5
nums = tuple(map(int, input().split()))
target = int(input("무슨 값을 셀까요? "))
print(nums.count(target))

