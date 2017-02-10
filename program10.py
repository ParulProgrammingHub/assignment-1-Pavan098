def simple_interest(p,t,r):
    simple_interest=float(p*r*t/100)
    print simple_interest
p=int(input("enter the principal amount:"))
r=float(input("enter the rate:"))
t=int(input("enter the time:"))
simple_interest(p,t,r)
