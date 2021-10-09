n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

nn = n_list
nn.sort()

a = 0
left = 0
right = n-1

for i in range(m):
    target = nn[i]
    while left <= right:
        mid = (left+right)//2
        if nn[mid] == target:
            a = nn[mid+1]
            print(1)
            break
        elif nn[mid] > target:
            right = mid-1
        else:
            left = mid+1
