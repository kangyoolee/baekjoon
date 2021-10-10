#자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

N = int(input())
print(N)
for i in range(1,N+1):
    if N-i == 0:
        break;
    print(N-i,sep='\n')