def fibonacci_loop(n):
    result, a, b = [], 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def fibonacci_recursive(n, counter):
    counter[0] += 1
    if n <= 1: return n
    return fibonacci_recursive(n - 1, counter) + fibonacci_recursive(n - 2, counter)

def main():
    while True:
        try:
            n = int(input("Enter number of terms (0 to 20): "))
            if 0 <= n <= 20: break
            print("Enter a value from 0 to 20.")
        except ValueError: print("Enter a valid whole number.")
    print("Loop version:", fibonacci_loop(n))
    recursive, total_calls = [], 0
    for i in range(n):
        counter = [0]
        recursive.append(fibonacci_recursive(i, counter))
        total_calls += counter[0]
    print("Recursive version:", recursive)
    print("Total recursive function calls:", total_calls)

if __name__ == "__main__": main()
