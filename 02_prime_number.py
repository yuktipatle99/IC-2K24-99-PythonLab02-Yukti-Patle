def is_prime(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True

def read_int(prompt):
    while True:
        try: return int(input(prompt))
        except ValueError: print("Enter a valid whole number.")

def main():
    n = read_int("Enter a number to check: ")
    print("Prime number." if is_prime(n) else "Not a prime number.")
    limit = read_int("Print primes up to: ")
    print("Prime numbers:", [x for x in range(2, limit + 1) if is_prime(x)])

if __name__ == "__main__": main()
