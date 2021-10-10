n = int(input())
lst_r = list()

for i in range(n):
    lst = list(input())
    lst_r.append(lst)

for i in range(n):
    result = 0
    cnt = 0
    for j in range(1,int(lst_r[i][0])):
        result = result+int(lst_r[i][j])
        if int(lst_r[i][j]) > result/int(lst_r[0]):
            cnt = cnt + 1
    print(int(lst_r[i][0])/cnt*100)
