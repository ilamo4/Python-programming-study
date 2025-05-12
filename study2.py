#2주차 스터디 warm-up (백준 10869)

# 두 자연수 A, B의 사칙연산을 하는 문제이다. (1 ≤ A, B ≤ 10,000)
# Python에서 입력받을 때는 input 함수를 사용한다. 
# 그리고 A, B 각각에 입력받아야 하므로 split 함수를 사용한다. 
# 이 문제에서는 기본형인 input().split() 에 자연수를 받아야 하므로 map에 정수형 술연산자를 이용하여 
# 코드를 짜고 그 결과를 한줄씩 출력하고자 구분자(sep)와 이스케이프 문자 중 줄 바꿈 문자(\n)을 사용하였다.


#방법1

A,B = input().split()
A = float(A)
B = float(B)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

#방법2

num = input().split()
A = int(num[0])
B = int(num[1])

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

#방법3

A, B = map(int, input().split())
print(A + B, A - B, A * B, A // B, A % B, sep="\n")


#2주차 스터디 문제풀이
#1
for i in range(1,11):
    print('%d'%i, end=' ')
#2
n=int(input())
for i in range(1,n+1):
    print('%d' %i)

#3
n=int(input())
for i in range(1,n+1,2):
    print(i)
#####range 안에 2부터 시작해도 ㄱㅊ#############

#4
n=int(input())
for i in range(1,10):
    print('%d x %d = %d' %(n,i,n*1))
#5
n=int(input())
sum=0
for i  in range(1,n+1):
    sum += i
print('합: %d' %sum)


#6
n=int(input())
for i in range(1,10):
    print('2 *%d = %d' %(i,2*i))

#7
n=int(input())
for i in range(1,n+1):
    if n % i ==0:
        print('%d' %i)
#8
a, b = map(int, input().split())
for i in range(a, b + 1):
    print("%d" % i)

#9
for i in range(3, 101, 3):
    print("%d" % i)

#10
n=int(input())
factorial=1
for i in range(1,n+1):
    factorial *= i
print('%d' %factorial)

#11
n = int(input())
for i in range(1, n + 1):
    print("%s" % ('*' * i))

#12
for i in range(1, 6):
    print("2 * %d = %d" % (i, 2 * i), end=' ')
    if i + 5 != 10:
        print("2 * %d = %d" % (i + 5, 2 * (i + 5)))
    else:
        print()
        
#13 팰린드롬############
s = input()
if s == s[::-1]:
    print("YES")
else:
    print("NO")

s = input("")
length = len(s)
flag = False
for i in range(length // 2):
    if s[i] != s[length - i - 1]:
        break
else:
    flag = True

if flag:
    print("YES")
else:
    print("NO")


#14 
n = int(input())
for i in range(n):
    print("%s%s" % (' ' * (n - i - 1), '*' * (2 * i + 1)))


#15 hard
n = int(input())

# 상단 모래시계 부분
for i in range(n):
    print(" " * i + "*" * (2 * (n - i) - 1))

# 하단 모래시계 부분
for i in range(1, n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

#16 hard
n = int(input())

# 상단 부분
for i in range(n):
    print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))

# 하단 부분
for i in range(1, n):
    print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))




