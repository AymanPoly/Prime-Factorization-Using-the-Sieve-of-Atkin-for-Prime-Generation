# Prime Factorization Using the Sieve of Atkin for Prime Generation

A Python implementation of integer factorization that combines the **Sieve of Atkin** for efficient prime generation with classical **trial division** for factorization. This educational project demonstrates how advanced prime sieving algorithms can be integrated into factorization routines.

## Overview

This algorithm factorizes a given integer `N` by:
1. Generating all primes up to `√N` using the Sieve of Atkin
2. Performing trial division using the generated prime list
3. Returning the prime factors with their respective powers

While not a novel approach in computational number theory, this implementation provides a clear, educational exploration of how modern prime sieves can enhance classical factorization methods.

## Algorithm Components

### 1. Sieve of Atkin

The Sieve of Atkin is a modern prime generation algorithm that marks primes based on quadratic forms. It has a time complexity of **O(N / log log N)** and is more efficient than the classical Sieve of Eratosthenes for large numbers.

**Key Properties:**
- Uses three quadratic forms to identify potential primes:
  - `4x² + y²` where `n ≡ 1 or 5 (mod 12)`
  - `3x² + y²` where `n ≡ 7 (mod 12)`
  - `3x² - y²` where `n ≡ 11 (mod 12)` and `x > y`
- Eliminates perfect squares of primes in a final sieving step
- More memory-efficient than naive approaches

### 2. Trial Division with Prime List

After generating primes up to `√N`, the algorithm performs trial division:
- Iterates through the prime list
- Divides `N` by each prime as many times as possible
- Records the count (power) of each prime factor
- Handles the case where the remaining number is prime itself

## Features

- ✅ Efficient prime generation using Sieve of Atkin
- ✅ Complete prime factorization with powers
- ✅ Handles edge cases (primes, small numbers)
- ✅ Clean, readable implementation
- ✅ Educational code with clear structure

## Usage

### Basic Example

```python
from prime_factorisation import prime_factors_with_powers

N = 120
factors = prime_factors_with_powers(N)
print(f"Prime factors of {N} with their powers: {factors}")
# Output: {2: 3, 3: 1, 5: 1}  # 120 = 2³ × 3¹ × 5¹
```

### More Examples

```python
# Factorize a composite number
factors = prime_factors_with_powers(100)
# {2: 2, 5: 2}  # 100 = 2² × 5²

# Factorize a prime number
factors = prime_factors_with_powers(17)
# {17: 1}  # 17 is prime

# Factorize a large number
factors = prime_factors_with_powers(1000)
# {2: 3, 5: 3}  # 1000 = 2³ × 5³
```

## Time Complexity

- **Sieve of Atkin**: O(N / log log N) for generating primes up to `√N`
- **Trial Division**: O(π(√N)) where π(x) is the prime-counting function
- **Overall**: Approximately O(√N / log √N) for the factorization

**Space Complexity**: O(√N) for storing the prime list

## Limitations

- Suitable for numbers where `√N` is computationally feasible
- For very large numbers (hundreds of digits), more advanced algorithms like Pollard's rho or the quadratic sieve would be more appropriate
- Memory usage grows with the square root of the input number

## Educational Value

This implementation serves as an excellent learning resource for:
- Understanding the Sieve of Atkin algorithm
- Learning how to combine different algorithmic techniques
- Exploring the relationship between prime generation and factorization
- Studying computational number theory concepts

## Requirements

- Python 3.6+ (uses `math.isqrt()` which requires Python 3.8+, but can be replaced with `int(math.sqrt())` for older versions)
- No external dependencies

## File Structure

```
.
├── Prime Factorisation of N.py    # Main implementation
└── README.md                       # This file
```

## Algorithm Details

### Sieve of Atkin Implementation

The algorithm marks potential primes using quadratic forms, then eliminates composite numbers by removing multiples of squares of primes. The final step collects all marked numbers as primes.

### Factorization Process

1. Generate primes up to `⌊√N⌋ + 1`
2. Initialize an empty dictionary for factors
3. For each prime `p`:
   - While `N` is divisible by `p`, divide and increment count
   - If count > 0, add `p: count` to factors
   - Early termination if `p² > remaining_N`
4. If remaining number > 1, it's prime itself

## References

- **Sieve of Atkin**: A. O. L. Atkin and D. J. Bernstein (2004). "Prime sieves using binary quadratic forms"
- **Trial Division**: Classical factorization method dating back to ancient mathematics

## License

This is an educational implementation. Feel free to use and modify for learning purposes.

## Contributing

This is an educational project. Suggestions and improvements are welcome!

---

**Note**: This implementation prioritizes clarity and educational value over absolute performance optimization. For production use with very large numbers, consider more advanced factorization algorithms.

