#N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

N = int(input())
arr = list(map(int, input().split()))
max = arr[0]
min = arr[0]

for i in range(0,N):
    if max < arr[i]:
        max = arr[i]
    elif min > arr[i]:
        min = arr[i]

print(min , max)