def BinSearch(a,i,j,x):
    if i == j:
        if a[i] == x:
            return f"Element is present at index {i}"
        else:
            return "Element is not present"
    else:
        mid = int((i+j)//2)
        if a[mid] == x:
            return f"Element is present at index {mid}"
        elif a[mid] > x:
            return BinSearch(a,i,mid-1,x)
        else:
            return BinSearch(a,mid+1,j,x)
            
a = list(map(int,input().split()))
i = 0
j = len(a)-1
x = int(input())
print(BinSearch(a,i,j,x))