"""
Calculating the compound interest from the given data
Formula ->  CI=P*(1+(r/n))**(n*t)-P
CI is the compound interest
p is the principle amount
r is the rater of interest
n is the number of times per year (per 12 months or per 6 months)
t is the time
"""
p=int(input('enter the Principle Amount : '))
r=float(input('enter the rate of interest (0-1): '))
t=int(input('enter the time in years: '))
n=int(input('enter 1 for yearly interest and 2 for 6 months interest: '))
ci=(p*(1+(r/n))**(n*t))-p
print('compount interest is = ',ci)
