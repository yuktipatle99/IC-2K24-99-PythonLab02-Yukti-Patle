def is_perfect(n):
    if n <= 1: return False
    total, d = 1, 2
    while d * d <= n:
        if n % d == 0:
            total += d
            pair = n // d
            if pair != d: total += pair
        d += 1
    return total == n

def read_int(prompt):
    while True:
        try: return int(input(prompt))
        except ValueError: print("Enter a valid whole number.")

def main():
    n = read_int("Enter a number to check: ")
    print("Perfect number." if is_perfect(n) else "Not a perfect number.")
    limit = read_int("Find perfect numbers up to: ")
    print("Perfect numbers:", [x for x in range(2, limit + 1) if is_perfect(x)])

if __name__ == "__main__": main()
