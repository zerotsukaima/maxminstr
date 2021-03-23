s = input("Введите строку ")
if s[len(s) - 1] != ".":
    s = input("Введите строку с точкой ")
print(len(s))
p = 0
l = 0
for i in s:
    if i == " ":
        p = p + 1
    l = p + 1
print(l)
#print('i=', i)
count_p = 0
count_l = 0
max = 0
min = 3000
for i in s:
    if i == " ":
        count_p += 1
for i in s:
    if i != '.' and i != " ":
        count_l += 1
        continue
    if count_l > max:
        max = count_l
    if count_l < min: # и тут
        min = count_l
    count_l = 0
print('max=', max)
print('min=', min)
for i in s:
    if i != "*":
        print(i * 2, end = "")
