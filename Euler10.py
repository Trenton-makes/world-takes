# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

primelist = []


def primefind(x):
    templist = []
    for num in range(2, x+1):
        num==True
        for i in range(1, sqrt(x)):
            if num % i == 0:
                templist.append(num)
            else:
                pass
        if len(templist) == 2:
            primelist.append(num)
            templist = []
            continue
        else:
            templist = []
            continue


primefind(200000)
y = sum(primelist)
print(y)
