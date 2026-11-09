# Python Programming Lab - Lab 02

**Student Name:** Yukti Patle  
**Subject:** Python Programming Lab  
**Lab:** 02

## Section C - Programs

### 1. Armstrong Number
**Aim:** Check an Armstrong number and list Armstrong numbers in a user-given range.  
**Logic:** Count the digits, raise each digit to that count, and add the results. If the sum equals the original number, it is Armstrong. Apply the same check to each number in the range.  
**Sample Input:** Number `153`; range `100` to `1000`.  
**Sample Output:** `153 is an Armstrong number.` Range result: `[153, 370, 371, 407]`.

### 2. Prime Number
**Aim:** Check whether a number is prime and print primes up to a limit.  
**Logic:** Numbers below 2 are not prime. Test divisors starting at 2 while divisor squared is at most the number. If none divides exactly, the number is prime.  
**Sample Input:** Number `17`; limit `20`.  
**Sample Output:** `17 is a prime number.` Prime list: `[2, 3, 5, 7, 11, 13, 17, 19]`.

### 3. Perfect Number
**Aim:** Check whether a number is perfect and list perfect numbers up to a limit.  
**Logic:** Add all positive proper divisors, excluding the number itself. The number is perfect when this sum equals the number.  
**Sample Input:** Number `28`; limit `1000`.  
**Sample Output:** `28 is a perfect number.` Perfect list: `[6, 28, 496]`.

### 4. Palindrome
**Aim:** Check a numeric palindrome using arithmetic and check a string palindrome.  
**Logic:** Reverse the integer with remainder and integer division, without converting it to text. For text, compare a lowercase, space-free version with its reverse.  
**Sample Input:** Number `121`; string `Never odd or even`.  
**Sample Output:** `121 is a numeric palindrome.` The string is a palindrome.

### 5. Fibonacci Series
**Aim:** Print the first n Fibonacci terms using a loop and recursion, and count recursive calls.  
**Logic:** The loop repeatedly updates the previous two terms. The recursive function returns the sum of the two preceding terms and increments a counter on each call. Input is limited to 20 terms for this simple recursive demonstration.  
**Sample Input:** `n = 10`.  
**Sample Output:** Both versions: `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`; total recursive calls for the ten separate term calculations: `276`.

### 6. Pattern Printing
**Aim:** Print a star triangle, number triangle, and centered pyramid.  
**Logic:** Nested loops control rows and the values or symbols printed in each row. The pyramid prints leading spaces followed by an odd number of stars.  
**Sample Input:** `n = 4`.  
**Sample Output:**
```text
Star triangle:
*
* *
* * *
* * * *

Number pattern:
1
1 2
1 2 3
1 2 3 4

Centered pyramid:
      *
    * * *
  * * * * *
* * * * * * *
```

### 7. Menu-Driven Application
**Aim:** Combine Programs 1 to 6 in one menu-driven application.  
**Logic:** Display a menu and call the selected operation. After each operation, return to the menu. Continue until Exit is selected; invalid choices show a message without crashing.  
**Sample Input:** Choose `2`, enter number `17`, prime limit `20`, then choose `0`.  
**Sample Output:** `Prime.` Prime list: `[2, 3, 5, 7, 11, 13, 17, 19]`; `Program closed.`

### 8. Number Guessing Game
**Aim:** Guess a random number from 1 to 100 in at most seven attempts.  
**Logic:** Generate a random integer. For each valid guess, display too high, too low, or correct. Stop on a correct guess or when all attempts are used.  
**Sample Input:** Example run where the generated number is `42`; guesses are `20`, `60`, `42`.  
**Sample Output:** `Too low.` `Too high.` `Correct! You guessed it in 3 attempt(s).` (The actual random number varies each run.)

## Analysis

**1. For loop vs while loop:** I used `for` when the number of repetitions was known, such as range checks, Fibonacci terms, patterns, and the game’s maximum attempts. I used `while` when repetition depended on a condition, such as input validation, divisor checks, digit reversal, and repeating the menu until Exit.

**2. Loop-based vs recursive Fibonacci:** The recursive version repeats calculations because the same earlier Fibonacci terms are calculated many times. Its function calls grow rapidly as n increases, while the loop calculates each term once and is more efficient.

**3. Largest divisor for prime checking:** It is sufficient to test divisors up to the square root of n (implemented as `divisor * divisor <= n`). Any factor larger than the square root must have a matching factor smaller than the square root, so a divisor would already have been found.

**4. Guessing strategy:** **Binary Search**. Guess the middle of the remaining range each time and discard the half that cannot contain the answer. This minimizes the maximum number of guesses.

## Files
- `01_armstrong_number.py`
- `02_prime_number.py`
- `03_perfect_number.py`
- `04_palindrome.py`
- `05_fibonacci_series.py`
- `06_pattern_printing.py`
- `07_menu_driven_application.py`
- `08_number_guessing_game.py`
- `README.md`
