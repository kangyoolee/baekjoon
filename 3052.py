lst = [int(input()) for i in range(10)]
lst = list(map(lambda lst: lst%42, lst)) 
count = []

for i in range(42):
    if 1<=lst.count(i):
        count.append('True')
    elif lst.count(i)==0:
        count.append('False')
    
print(count.count('True'))