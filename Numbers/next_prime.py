# Next Prime Number - Have the program find prime
# numbers until the user chooses to stop asking for
# the next one.


def is_prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def next_prime(current):
    current += 1
    while not is_prime(current):
        current += 1
    return current

if __name__ == "__main__":
    current_prime = 2
    while True:
        res = raw_input("Next prime ? (y/n)")
        if res.lower() == 'y':
            print current_prime
            current_prime = next_prime(current_prime)
        else:
            break
