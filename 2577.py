a = int(input())
b = int(input())
c = int(input())

arr = str(a*b*c)
print(arr.count('0'))
for i in range(1,10):
    print(arr.count(str(i)))
    