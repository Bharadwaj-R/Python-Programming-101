"""
Finding the sum of squares of n natural numbers
Formula : (n)*(n+1)*(2*n+1)/6 -> total sum of n squared numbers
            n**2 -> odd sum
            sum total - sum odd = sum even
"""

n=int(input('enter the number of numbers: '))
neven=n//2
nodd=n-neven
tsum=n*(n+1)*(2*n+1)/6
oddsum=nodd**2
evensum=tsum-oddsum
print('Squared sum of natural numbers is = ',tsum)
print('the sum of squares of odd numbers is = ',oddsum)
print('the usm of squares of even numbers is = ',evensum)

