# count_num.py
s = 'aa3aBbb6ccc'
total = 0
for i in range(len(s)):
    if s[i].isalpha():
        continue # пропускаем шаг
    total += int(s[i])

print("Сумма цифр:", total)
