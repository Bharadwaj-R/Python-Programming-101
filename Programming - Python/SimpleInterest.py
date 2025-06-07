"""
Program to find the simple interest of a given amount
variables required - Principle amount, rate of interest, time
Formula - pa*time*rate/100
"""
pa=int(input("enter the Principle Amount: "))
rate=float(input("enter the rate of interest(<1): "))
time=int(input("enter the time in years: "))
si=pa*rate*time/100
print("Simple Interest is: ",si)
