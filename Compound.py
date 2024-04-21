# Take P, N and R as input from user

P=float(input('Please enter Principal in INR:'))
N=float(input('Please enter Period in Years:'))
R=float(input('Please enter Rate of Interest in %p.a.:'))

# Calculate Compound Interest amount

A=P*(1+R/100)**N
I=A-P

# Print above results

print(f'Amount for Compound interest: {A:.2f} INR')
print(f'Total Interest:{I:.2f} INR')