




n = int(input())

for i in range(n):
    a,b = map(int, input().split())
    yaksu_list = [] 
    for i in range(1,a):
        if a%i==0:
            yaksu_list.append(i)

    if sum(yaksu_list) == b+1:
        print('yes')
    else:
        print('no')



