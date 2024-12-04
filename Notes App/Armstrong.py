n=int(input("Enter n digit number\n"))
num=n
sum=0
while n>0:
    d=n%10
    sum=sum+(d*d*d)
    n=n//10 
if sum==num:
        print("armstrong")
else:
        print("not armstrong")    
    