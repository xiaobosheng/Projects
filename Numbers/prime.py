# Prime Factorization - Have the user enter a number
# and find all Prime Factors (if there are any) and
# display them.


from datetime import datetime


def prime_factor(n):
    result = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            result.append(i)
            n /= i
        i += 1
    if len(result) == 0:
        result.append(n)
    return result


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

startTime = datetime.now()
prime_factor(4487802352351)
print(datetime.now()-startTime)
startTime = datetime.now()
primes(4487802352351)
print(datetime.now()-startTime)

