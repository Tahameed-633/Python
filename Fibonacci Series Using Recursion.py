def fibonacci_generator(n):
    if(n==0):
        return 0;
    if(n==1):
        return 1
    return fibonacci_generator(n-2)+fibonacci_generator(n-1)
r=int(input("Enter the range to generate fibonacci number:"))
for i in range(0,r):
    print(fibonacci_generator(i))