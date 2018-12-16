# list_range2.py
print([x for x in range(5) if x%2 == 0])

print(list(filter((lambda x: x%2 == 0), range(5))))

res = []
for x in range(5):
    if x%2 == 0:
        res.append(x)
print(res)
