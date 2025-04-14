#1
print("Hello, World!!")

#2
print("I love python!!")

#3
num = float(input())
print("%.1f" % num)

#4
a = int(input())
b = int(input())
print(a + b)

#5
a = int(input())
b = int(input())

print("%d + %d = %d" % (a, b, a + b))
print("%d - %d = %d" % (a, b, a - b))
print("%d * %d = %d" % (a, b, a * b))
print("%d / %d = %f" % (a, b, a / b))

#6
print("I am a student.\n *\n\t^^Nice to meet you~")

#7
name = input("당신의 이름은? ")
age = int(input("당신의 나이는? "))
height = input("당신의 키는? ")

print("이름은 %s, 나이는 %d살, 키는 %scm입니다." % (name, age, height))

#8
num = int(input())
print(num ** 0.5)
print(num ** 2)
print(num ** 3)

# 9.
# 답 9-1 a // b = 2 (//는 몫 구하기)

# 10. 
# 답 10-1 PythonPythonPython

# 11.

# 답 11-3 에러 발생  (문자열과 정수를 더할 수 없음음)

# 12.
# 답 12-1 1500원

# 13.
# 답 13-1  3 (정수 형식 지정자로 출력하면 소수점이 버려진다)

# 14.
# 답 14-4  나누기-몫-나머지

# 15.
# 답 15-1  2 (정수 나누기에서 //는 몫만 출력한다)

#16
num = int(input())
if num == 0:
    print("0입니다.")
elif num > 0:
    print("양수입니다.")
else:
    print("음수입니다.")

#17
age = int(input())
if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

#18
score = int(input())
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

#19
time = int(input())
if time < 12:
    print("오전입니다.")
else:
    print("오후입니다.")

#20
a, b, c = map(int, input().split())
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

#21
a, b = map(int, input().split())
if (a + b) % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

#22
num = int(input())
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
else:
    print(num)

#23
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")

#24
a, b = map(int, input("두 정수를 입력하세요: ").split())

if a == b:
    print("두 수는 같습니다.")
elif abs(a - b) >= 10:
    print("차이가 10 이상입니다.")
else:
    print("차이가 10 미만입니다.")

#25
a, b, c = map(int, input("세 정수를 입력하세요: ").split())

if a == 0 or b == 0 or c == 0:
    print("0은 포함될 수 없습니다.")
elif a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print("모두 짝수입니다.")
elif a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
    print("모두 홀수입니다.")
else:
    print("홀수와 짝수가 섞여 있습니다.")


