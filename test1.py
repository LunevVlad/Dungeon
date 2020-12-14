def bubble_sort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                for k in a:
                    print(k,end=' ')
                print('\n',end = '')

a=[]
b = input().split()
for l in b:
    x = float(l)**2
    a.append(x)
print(a)
input()
    
