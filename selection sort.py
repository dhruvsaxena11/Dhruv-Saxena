def linear(a,n):
    for x in a:
        if x==n:
            return True
        else:
            return False
a=list(map(int,input().split()))
n=int(input("Enter the Number to be found :"))
ans=linear(a,n)
print(ans)