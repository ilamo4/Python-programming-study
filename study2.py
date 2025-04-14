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




