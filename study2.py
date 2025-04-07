#1
for i in range(1,11):
    print('%d'%i)
#2
n=int(input())
for i in range(1,n+1):
    print('%d' %i)

#3
n=int(input())
for i in range(1,n+1,2):
    print(i)


#4
n=int(input())
for i in range(1,10):
    print('%d * %d = %d' %(n,i,n*1))
#5
n=int(input())
sum=0
for i  in range(1,n+1):
    sum += i
print('합: %d'%sum)


#6
n=int(input())
for i in range(1,10):
    print('2 *%d = %d %(i,2*i)')

n=int(input())
for i in range(1,n+1):
    if n % i ==0:
        print(n)


n=int(input())
for i in range(1,101,3):
    if n % 3 ==0:
        print(n)

#10
n=int(input())
factorial=1
for i in range(1,n+1):
    factorial *= i
print('%d'%factorial)

for i in range()

n = int(input('정수를 입력해 주세요 : '))