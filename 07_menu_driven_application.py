# Menu-driven combination of Programs 1 to 6
def read_int(prompt, low=None, high=None):
    while True:
        try:
            n = int(input(prompt))
            if low is not None and n < low: print(f"Enter a value >= {low}.")
            elif high is not None and n > high: print(f"Enter a value <= {high}.")
            else: return n
        except ValueError: print("Enter a valid whole number.")

def armstrong(n):
    return n >= 0 and sum(int(d) ** len(str(n)) for d in str(n)) == n

def prime(n):
    if n < 2: return False
    d = 2
    while d * d <= n:
        if n % d == 0: return False
        d += 1
    return True

def perfect(n):
    if n <= 1: return False
    total, d = 1, 2
    while d * d <= n:
        if n % d == 0:
            total += d
            pair = n // d
            if pair != d: total += pair
        d += 1
    return total == n

def numeric_palindrome(n):
    if n < 0: return False
    original, reverse = n, 0
    while n:
        reverse = reverse * 10 + n % 10
        n //= 10
    return original == reverse

def text_palindrome(s):
    s = "".join(c.lower() for c in s if not c.isspace())
    return s == s[::-1]

def fib_loop(n):
    result, a, b = [], 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def fib_rec(n, calls):
    calls[0] += 1
    if n <= 1: return n
    return fib_rec(n - 1, calls) + fib_rec(n - 2, calls)

def patterns(n):
    print("Star triangle:")
    for r in range(1, n + 1): print("* " * r)
    print("Number pattern:")
    for r in range(1, n + 1):
        for x in range(1, r + 1): print(x, end=" ")
        print()
    print("Centered pyramid:")
    for r in range(1, n + 1): print("  " * (n-r) + "* " * (2*r-1))

def main():
    while True:
        print("\n--- LAB 2 MENU ---")
        print("1 Armstrong  2 Prime  3 Perfect  4 Palindrome")
        print("5 Fibonacci  6 Patterns  0 Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            n = read_int("Number: ", 0)
            print("Armstrong." if armstrong(n) else "Not Armstrong.")
            a, b = read_int("Range start: ", 0), read_int("Range end: ", 0)
            if a > b: print("Invalid range.")
            else: print([x for x in range(a, b+1) if armstrong(x)])
        elif choice == "2":
            n = read_int("Number: ")
            print("Prime." if prime(n) else "Not prime.")
            limit = read_int("Print primes up to: ")
            print([x for x in range(2, limit+1) if prime(x)])
        elif choice == "3":
            n = read_int("Number: ")
            print("Perfect." if perfect(n) else "Not perfect.")
            limit = read_int("Find perfect numbers up to: ")
            print([x for x in range(2, limit+1) if perfect(x)])
        elif choice == "4":
            n = read_int("Non-negative integer: ", 0)
            print("Numeric palindrome." if numeric_palindrome(n) else "Not numeric palindrome.")
            s = input("Text: ")
            print("String palindrome." if text_palindrome(s) else "Not string palindrome.")
        elif choice == "5":
            n = read_int("Terms (0 to 20): ", 0, 20)
            print("Loop:", fib_loop(n))
            vals, total = [], 0
            for i in range(n):
                calls = [0]; vals.append(fib_rec(i, calls)); total += calls[0]
            print("Recursion:", vals, "| Function calls:", total)
        elif choice == "6":
            patterns(read_int("Rows (1 to 20): ", 1, 20))
        elif choice == "0":
            print("Program closed."); break
        else:
            print("Invalid choice. Select 0 to 6.")

if __name__ == "__main__": main()
