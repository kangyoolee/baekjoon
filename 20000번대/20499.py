# 아무래도 우리 팀 다리우스가 고수인 것 같다. 그의 
# K/D/A를 보고 그가 「진짜」인지 판별해 보자.

#  
# K+A<D 이거나, D=0 이면 그는 「가짜」이고, 그렇지 않으면 「진짜」이다.

# 입력
#  
# K/D/A 가 주어진다.

# 출력
# 그가 「진짜」이면 gosu, 「가짜」이면 hasu를 출력한다.

a = str(input())
a_s = a.split('/')
aa1 = int(a_s[0])
aa2 = int(a_s[1])
aa3 = int(a_s[2])

if aa1 + aa3 < aa2 or aa2 == 0:
    print('hasu')
else:
    print('gosu')