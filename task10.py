decreases = 0
prev_temp = float(input())
while True:
    current_temp = float(input())
    if current_temp == 0:
        break
    if current_temp < prev_temp:
        decreases += 1
    prev_temp = current_temp
print(decreases)
