n = int(input())
questions = 0
k = 1
while k < n:
    k *= 2
    questions += 1
print(questions if k > n else questions)
