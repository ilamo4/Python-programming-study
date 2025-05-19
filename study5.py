# 5주차 스터디 warm-up (백준 10039)

sum=0
for i in range(5):
    score = int(input())
    if  score < 40:
        sum += 40
    else:
        sum += score
print(int(sum/5))

#5주차 스터디 문제풀이

#1
def add(a, b):
    return a + b

x, y = map(int, input("두 수를 입력하세요: ").split())
print(add(x, y))

#2
def to_upper(s):
    return s.upper()

s = input()
print(to_upper(s))

#3
def list_length(lst):
    return len(lst)

lst = list(map(int, input().split()))
print(list_length(lst))

#4
def is_same_ends(s):
    return s[0] == s[-1]

s = input()
print(is_same_ends(s))

#5
def get_even(lst):
    result = []
    for x in lst:
        if x % 2 == 0:
            result.append(x)
    return result

nums = list(map(int, input().split()))
print(get_even(nums))

#6
def clean_string(s):
    return s.replace(" ", "").lower()

s = input()
print(clean_string(s))

#7
def bigger(a, b):
    if a > b:
        return a
    else:
        return b

x, y = map(int, input().split())
print(bigger(x, y))

#8
def most_common(lst):
    max_count = 0
    result = None
    for x in lst:
        if lst.count(x) > max_count:
            max_count = lst.count(x)
            result = x
    return result

nums = list(map(int, input().split()))
print(most_common(nums))

#9
def filter_length(words):
    result = []
    for w in words:
        if len(w) >= 3:
            result.append(w)
    return result

words = input().split()
print(filter_length(words))

#10
def max_of_three(a, b, c):
    three = [a, b, c]
    max_val = max(three)
    return max_val

a, b, c = map(int, input().split())
print(max_of_three(a, b, c))

#11
def clean_alpha(s):
    result = ''
    for ch in s:
        if ch.isalpha():
            result += ch.lower()
    return result

s = input()
print(clean_alpha(s))

#12
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input())
print(sum_to_n(n))

#13
def length_list(words):
    result = []
    for w in words:
        result.append(len(w))
    return result

words = input().split()
print(length_list(words))

#14
def count_even_odd(lst):
    even = 0
    odd = 0
    for x in lst:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

nums = list(map(int, input().split()))
print(count_even_odd(nums))

#15
def initials(s):
    words = s.split()
    result = ''
    for w in words:
        result += w[0].upper()
    return result

s = input()
print(initials(s))

#16
def who_is_pass(scores):
    for i in range(len(scores)):
        if scores[i] >= 60:
            print(i + 1, end=' ')

scores = list(map(int, input().split()))
who_is_pass(scores)

#17
def char_count(s):
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d

s = input()
print(char_count(s))

#18
def get_divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

n = int(input())
print(get_divisors(n))

#19
def longest_word(s):
    words = s.split()
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

s = input()
print(longest_word(s))

#20
def find_char(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            return i
    return '없음'

s = input()
ch = input()
print(find_char(s, ch))


