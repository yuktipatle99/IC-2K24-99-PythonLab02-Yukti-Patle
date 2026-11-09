def print_patterns(n):
    print("\n1. Right-angled star triangle")
    for row in range(1, n + 1):
        print("* " * row)
    print("\n2. Number pattern")
    for row in range(1, n + 1):
        for value in range(1, row + 1): print(value, end=" ")
        print()
    print("\n3. Centered pyramid")
    for row in range(1, n + 1):
        print("  " * (n - row) + "* " * (2 * row - 1))

def main():
    while True:
        try:
            n = int(input("Enter rows (1 to 20): "))
            if 1 <= n <= 20: break
            print("Enter a value from 1 to 20.")
        except ValueError: print("Enter a valid whole number.")
    print_patterns(n)

if __name__ == "__main__": main()
