def find_date(x,y):
    day = 0
    for i in range(1,x):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            day = day + 31
        elif i in [4, 6, 9, 11]:
            day = day + 30
        elif i == 2:
            day = day + 28
    day = day + y

    days = day % 7
    date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return date[days-1]



a,b = map(int,input().split())
print(find_date(a,b))