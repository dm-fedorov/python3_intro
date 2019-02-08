# count_lst.py
numbers = [3, 5, 9, -1, 3, 1]
result = 0
for item in numbers:
    if item < 0:
        break
    result += item
print(result)
