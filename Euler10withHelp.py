# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
primelist=[]
prime=[True for i in range(2000001)]
n=2
while (n*n <= 2000001):
    if (prime[n] == True):
        # Update all multiples of p
        for i in range(n * 2, 2000001, n):
            prime[i] = False
    n += 1

# Print all prime numbers
for n in range(2, 2000001):
    if prime[n]:
        primelist.append(n)

x=sum(primelist)
print(x)