def compound_interest(p,t,r):
    c=float(p*((1+r)**t)-p)
    print c
p=int(input("enter the principal amount:"))
r=float(input("enter the rate:"))
t=int(input("enter the time:"))
r=r/100
compound_interest(p,t,r)
            
