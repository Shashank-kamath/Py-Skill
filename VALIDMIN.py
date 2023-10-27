# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if(min(x,y) == min(y,z) and min(x,y) == min(z,x)):
        print("YES")
    else:
        print("NO")
