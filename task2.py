s = input("Введите вашу строку: ")
result = ""
for i in range(1, len(s), 2):
    result += s[i]
print(result)
