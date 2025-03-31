n = int(input("Введите максимальный объем кубика: "))
i = 1
while i ** 3 <= n:
    print(i ** 3, end=" ")
    i += 1
print()
