answer = int(input("Введите ответ Оли: "))
k = 1
while k < answer:
    k *= 2
if k == answer:
    print("верно")
else:
    print("неверно")