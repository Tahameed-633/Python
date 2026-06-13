lr=int(input("Enter lower range:"))
hr=int(input("Enter higher range:"))
cnt=0
for i in range(lr,hr+1):
    if(i%2!=0):
        cnt=cnt+1
print("Odd number's count=",cnt)