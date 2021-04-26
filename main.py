def binary_search(sort, element, left, right):
    if left > right:
        return left-1

    middle = (right + left) // 2
    if sort[middle] == element:
        return middle
    elif element < sort[middle]:

        return binary_search(sort, element, left, middle - 1)
    else:
        return binary_search(sort,element, middle + 1, right)
def mysort():
    global a
    for i in range(len(a)-1):
        for j in range(len(a) - 1):
            if a[j]>a[j+1]:
                a[j],a[j + 1]=a[j + 1],a[j]

s=input().split()
n=int(input())
a=[]
for i in range(len(s)):
    a.append(int(s[i]))
mysort()
print(a)
print(binary_search(a, n, 0, len(a)-1))
