#to find the factorial
def finding_fact(n):
    if n<0:
        print("No negative values")
    elif n==0 or n==1:
        print("factorial is : 1")
    else:
        fact=1
        while n>1:
            fact*=n
            n-=1
        print("factorial is:",fact)

finding_fact(4)










