n = int(input())
result = list()

for i in range(n):
    lst = list(input())
    result.append(lst)

for i in range(n):
    count = 0
    score = 0
    for j in range(len(result[i])):
        if result[i][j] == 'O':
            count = count + 1
            score = score + count
        else:
            count = 0
    print(score)

