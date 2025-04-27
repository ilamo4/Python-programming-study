#list는 함수이름이므로 새로운 list 이름을 문제 상황에 맞게 작성하자.
#문제 상황에 맞는 적절한 변수 이름 고민해서 코드 짜기.
#1
num=[1, 2, 3, 4, 5]
print(num[-1])

#2
list=[3, 6, 9]
list.append(12)
print(list)

#3
num= int(input('몇 번 입력받을래?: '))
list =[]
for i in range(num):
    list.append(int(input()))
print(sum(list))

#4
list = [1, 2, 3, 4, 5, 6]
even = []
for i in list:
    if i % 2 == 0:
        even.append(i)
print(even)

#5
list = [10, 2, 5, 8]
print(max(list), min(list))

#6
num = list(map(int.input().split()))
even =[]
odd =[]

for i in num:
    if i % 2 ==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#7 ???
word= input().split()
len= []
for i in word:
    if (i == word[-1]):
        print(len(word, end=''))
    print(len(word, end=''))

if (word == words[-1]):
        print(len(word), end='')
        break 는 python 에만 적용됨.

i는 보통 인덱스, 숫자 몇번쨰 이럴때 변수로 쓰임.


#8
list = [0, 1, 0, 2, 3, 0]
print(list.count(0))

#9 ???
num= list(map(int.input().split()))
sum =[]
res=0
for i in num:
# word와 words num과 nums 변수로 같이 자주 쓰인다.

#10
list = [1, 2, 3, 4, 5]
print(list[:: -1])


#2주차 warm-up 
A,B= input().split()
A= int(A), B= int(B)
print(A+B)
print(A-B)
print(A*B)
print(int(A//B))
print(A%B)