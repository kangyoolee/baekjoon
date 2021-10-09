n = int(input())
lst = list(map(int, input().split()))
max_lst = max(lst)
result = 0

for i in range(n):
    result = result + lst[i]/max_lst*100

print(result/n)