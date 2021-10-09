num = int(input())
num_a = num
result = 0
count = 0

while True:
    result = (num_a%10 + num_a//10)%10 + (num_a%10)*10
    num_a = result
    count = count+1
    if result==num:
        break

print(count)