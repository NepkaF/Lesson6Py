#Первое задание
First = int(input())
dif = int(input())
n=int(input())
a=[First]
for i in range(1,n):
    a.append(a[i-1]+dif)
for i in range(n):
    print(a[i])
#Второе задание
Min = int(input())
Max = int(input())
for i in range(n):
    if a[i]<=Max and a[i] >= Min :
        print(a[i])

