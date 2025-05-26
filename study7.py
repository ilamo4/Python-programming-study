#7주차 스터디 warm-up (백준 7120)

# word=input()
# string=word[0]
# for i in range(len(word)-1):
#     if word[i] != word[i+1]:
#         string += word[i+1]
# print(string)

#7주차 스터디 문풀 
#1
# name = input()
# with open("name.txt", "w") as f:
#     f.write(name)

#2
# with open("hello.txt", "r") as f:
#     line = f.readline()
# print(line.strip())

#3
# with open("data.txt", "r") as f:
# 	text = f.read()

# word = text.split()
# print(len(word))


#4

# with open("log.txt", "r") as f:
#     for line in f:
#         if "error" in line:
#             print(line.strip())

#5 오래 걸림..

# with open("words.txt", "r") as f:
#     text = f.read()

# words = text.split()
# count ={}

# for word in words:
#     if word in count:
#         count[word] +=1
#     else:
#         count[word] =1 
# print(count)



#6 이스케이프 문자 \n 쓰는 위치

# with open("num.txt", "r") as f:
#     nums = list(map(int, f.read().split()))

# with open("even.txt", "w") as f:
#     for n in nums:
#         if n % 2 == 0:
#             f.write("%d/n" %n)


#7 어려움
file = open("student.txt", "r")

max_score = 0
min_score = 100
top_student = ''
bottum_student = ''
total_score = 0
count = 0

for line in file:
    name, score = line.split()
    score = int(score)

    total_score += score
    count += 1

    if max_score < score:
        max_score = score
        top_student = name

    if score < min_score:
        min_score = score
        bottum_student = name


file.close()

average = total_score / count


print("우등생은 %s입니다." % top_student)
print("열등생은 %s입니다." % bottum_student)
print("평균은 %.1f점입니다." % average)


# with as 안 쓸거면 f.close 써주기.

