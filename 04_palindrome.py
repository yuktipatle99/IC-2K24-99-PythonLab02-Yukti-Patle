def number_palindrome(n):
    if n < 0: return False
    original, reverse = n, 0
    while n > 0:
        reverse = reverse * 10 + n % 10
        n //= 10
    return original == reverse

def string_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if not ch.isspace())
    return cleaned == cleaned[::-1]

def main():
    while True:
        try:
            n = int(input("Enter a non-negative integer: "))
            if n >= 0: break
            print("Enter a non-negative number.")
        except ValueError: print("Enter a valid whole number.")
    print("Numeric palindrome." if number_palindrome(n) else "Not a numeric palindrome.")
    text = input("Enter a word or sentence: ")
    print("String palindrome." if string_palindrome(text) else "Not a string palindrome.")

if __name__ == "__main__": main()
