a=0
b=1
n = int(input("Enter value of n: "))
print("Fibonacci Series:", end=" ")
for _ in range(n):
    print(a, end=" ")
    c=a+b
    b=a
    a=c
