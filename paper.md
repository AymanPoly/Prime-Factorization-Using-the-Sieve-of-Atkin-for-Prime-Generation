---
title: 'Prime Factorization Using the Sieve of Atkin for Prime Generation'
tags:
  - Python
  - computational number theory
  - prime factorization
  - Sieve of Atkin
  - integer factorization
  - algorithms
authors:
  - name: Ayman Timjicht
    orcid: 0009-0000-1995-2165
    equal-contrib: true
    affiliation: 1
affiliations:
 - name: Digital Social Commerce, United Kingdom
   index: 1
date: 2025
bibliography: paper.bib
---

# Summary

Integer factorization is a fundamental problem in computational number theory with applications in cryptography, number theory, and computer science. The problem of decomposing a composite integer into its prime factors has been studied for centuries, and while efficient algorithms exist for small to medium-sized numbers, the challenge remains computationally intensive for large integers.

This paper presents a Python implementation that combines the **Sieve of Atkin** [@atkin2004] for efficient prime generation with classical **trial division** for factorization. The Sieve of Atkin is a modern prime sieving algorithm that uses quadratic forms to identify primes, achieving a time complexity of $O(N / \log \log N)$, which is more efficient than the classical Sieve of Eratosthenes for large numbers. The implementation generates all primes up to $\sqrt{N}$ and then performs trial division to factorize the input integer, returning the prime factors with their respective powers.

While this approach is not novel in computational number theory, it provides a clear, educational implementation that demonstrates how advanced prime sieving algorithms can be integrated into factorization routines. The code is designed to be readable and educational, making it suitable for teaching computational number theory concepts and for understanding the relationship between prime generation and factorization algorithms.

# Statement of need

Prime factorization is a cornerstone problem in computational number theory with wide-ranging applications. In cryptography, the security of RSA encryption relies on the difficulty of factoring large integers [@rivest1978]. In pure mathematics, factorization is essential for solving Diophantine equations, studying number-theoretic functions, and exploring properties of integers. Educational contexts also benefit from clear implementations that demonstrate fundamental algorithmic techniques.

The Sieve of Atkin represents a significant improvement over classical prime sieving methods. Unlike the Sieve of Eratosthenes, which marks multiples of primes, the Sieve of Atkin uses quadratic forms to identify potential primes, reducing the number of operations required. This makes it particularly valuable when generating primes for factorization routines, where efficiency in the prime generation step directly impacts overall performance.

However, many existing implementations of factorization algorithms either use less efficient prime generation methods or are optimized for very large numbers using advanced techniques like Pollard's rho algorithm or the quadratic sieve, which can be difficult to understand for educational purposes. There is a need for clear, well-documented implementations that demonstrate the integration of modern prime sieving with classical factorization techniques.

This implementation fills this gap by providing:

1. **Educational clarity**: A readable implementation that clearly separates prime generation from factorization, making it easy to understand each component.

2. **Efficient prime generation**: The use of the Sieve of Atkin provides better performance than naive approaches while remaining comprehensible.

3. **Complete factorization**: The algorithm returns not just prime factors but their powers, providing complete factorization in the form $N = p_1^{e_1} \times p_2^{e_2} \times \cdots \times p_k^{e_k}$.

4. **No external dependencies**: The implementation uses only Python's standard library, making it easy to use and understand.

5. **Suitable for teaching**: The code structure and documentation make it ideal for educational use in courses on computational number theory, algorithms, or cryptography.

The implementation has been designed to be used by students learning computational number theory, researchers needing a reference implementation, and educators teaching factorization algorithms. It demonstrates best practices in algorithm implementation while maintaining clarity over optimization.

# Mathematics

## Sieve of Atkin

The Sieve of Atkin identifies primes using three quadratic forms. For a limit $L$, the algorithm marks numbers as potentially prime if they satisfy one of the following conditions:

1. For $n = 4x^2 + y^2$ where $x, y \in \mathbb{N}$:
   - Mark $n$ as prime if $n \equiv 1 \pmod{12}$ or $n \equiv 5 \pmod{12}$

2. For $n = 3x^2 + y^2$ where $x, y \in \mathbb{N}$:
   - Mark $n$ as prime if $n \equiv 7 \pmod{12}$

3. For $n = 3x^2 - y^2$ where $x, y \in \mathbb{N}$ and $x > y$:
   - Mark $n$ as prime if $n \equiv 11 \pmod{12}$

After marking potential primes, the algorithm eliminates composite numbers by removing all multiples of squares of primes:

$$\text{For each prime } r \text{ where } r^2 \leq L, \text{ remove } r^2, 2r^2, 3r^2, \ldots$$

The time complexity of the Sieve of Atkin is $O(L / \log \log L)$, which is asymptotically better than the Sieve of Eratosthenes' $O(L \log \log L)$.

## Factorization Algorithm

Given an integer $N$, the factorization algorithm proceeds as follows:

1. Generate all primes $p \leq \lfloor\sqrt{N}\rfloor + 1$ using the Sieve of Atkin.

2. For each prime $p$ in the generated list:
   - While $p$ divides the current value of $N$:
     - Divide $N$ by $p$
     - Increment the count for $p$
   - If $p^2 > N$, terminate early (remaining $N$ is prime)

3. If the remaining $N > 1$, it is prime itself and should be included in the factorization.

The algorithm returns the complete prime factorization:

$$N = \prod_{i=1}^{k} p_i^{e_i}$$

where $p_i$ are distinct primes and $e_i$ are their respective exponents.

## Complexity Analysis

The overall time complexity is dominated by the prime generation step:

- **Prime generation**: $O(\sqrt{N} / \log \log \sqrt{N}) = O(\sqrt{N} / \log \log N)$
- **Trial division**: $O(\pi(\sqrt{N}))$ where $\pi(x)$ is the prime-counting function
- **Overall**: Approximately $O(\sqrt{N} / \log \sqrt{N})$

The space complexity is $O(\sqrt{N})$ for storing the prime list.

# Implementation Details

The implementation consists of two main functions:

1. `sieve_of_atkin(limit)`: Generates all primes up to the given limit using the Sieve of Atkin algorithm.

2. `prime_factors_with_powers(N)`: Factorizes the integer $N$ by first generating primes up to $\sqrt{N}$ and then performing trial division.

The code handles edge cases such as:
- Numbers $\leq 2$
- Prime numbers (which factorize to themselves)
- Perfect powers
- Numbers with repeated prime factors

# Usage Example

```python
from prime_factorisation import prime_factors_with_powers

N = 120
factors = prime_factors_with_powers(N)
# Returns: {2: 3, 3: 1, 5: 1}
# Represents: 120 = 2³ × 3¹ × 5¹
```

# Limitations and Future Work

This implementation is suitable for numbers where $\sqrt{N}$ is computationally feasible. For very large numbers (hundreds of digits), more advanced algorithms would be appropriate:

- **Pollard's rho algorithm**: Probabilistic method with average time complexity $O(\sqrt{p})$ where $p$ is the smallest prime factor
- **Quadratic sieve**: Sub-exponential time complexity, suitable for numbers with 50-100 digits
- **General number field sieve**: Best known algorithm for very large numbers

Future improvements could include:
- Integration with probabilistic factorization methods for larger numbers
- Parallelization of the prime generation step
- Memory optimization for very large prime lists
- Support for factorization of multiple numbers using cached prime lists

# Acknowledgements

This implementation was developed as an educational resource for computational number theory. The algorithm combines well-established techniques from the literature on prime sieving and integer factorization.

# References

