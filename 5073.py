while True:
    lst = list(map(int, input().split()))
    a=lst[0]
    b=lst[1]
    c=lst[2]
    if a == 0 and b==0 and c==0:
        break
    else:
        if max(lst)<sum(lst)-max(lst):
            # print(a == b == c)
            # print(a != b != c)
            if a == b and b == c and a == c:
                print('Equilateral')
            elif a != b and a != c and b != c:
                print('Scalene')
            else:
                print('Isosceles')
        else:
            print('Invalid')
