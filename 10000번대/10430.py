# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

a,b,c = map(int, input().split())
a1 = (a+b)%c
a2 = ((a%c) + (b%c)) %c
a3 = (a*b)%c
a4 = ((a%c) * (b%c)) %c
print(f'''{a1}
{a2}
{a3}
{a4}''')