def is_armstrong(n):
    if n < 0: return False
    p = len(str(n))
    return sum(int(d) ** p for d in str(n)) == n

def read_nonnegative(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n >= 0: return n
            print("Enter a non-negative number.")
        except ValueError:
            print("Enter a valid whole number.")

def main():
    n = read_nonnegative("Enter a number: ")
    print("Armstrong number." if is_armstrong(n) else "Not an Armstrong number.")
    a = read_nonnegative("Range start: ")
    b = read_nonnegative("Range end: ")
    if a > b: print("Invalid range: start must not exceed end.")
    else: print("Armstrong numbers:", [x for x in range(a, b + 1) if is_armstrong(x)])

if __name__ == "__main__": main()
