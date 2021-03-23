st = input("Введите строку: ")

wLen = 0  # Длина текущего слова
maxLen = 0  # Длина самого длинного слова
minLen = 30000  # Длина самого короткого слова

for s in st:
    if s == ' ' or s == '.':
        if maxLen < wLen:
            maxLen = wLen
        if (minLen > wLen) and (wLen != 0):
            minLen = wLen
        wLen = 0
        continue #можно решить без него заменив тут на else
    wLen += 1

print("Длина самого длинного слова: " + str(maxLen))
print("Длина самого короткого слова: " + str(minLen))