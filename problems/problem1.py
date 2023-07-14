# If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.
# Find the sum of all the multiples of $3$ or $5$ below $1000$.


def sum_of_multiples(n, upper):
    num_elements = (upper // n)
    lower = n
    higher = num_elements * n
    return (lower + higher) * num_elements / 2
    

a = 3
b = 5
n = 1000

sum_multiples_of_a = sum_of_multiples(a, n-1)
sum_multiples_of_b = sum_of_multiples(b, n-1)
sum_multiples_of_ab = sum_of_multiples(a * b, n-1)

total = sum_multiples_of_a + sum_multiples_of_b - sum_multiples_of_ab
print("Total:", total)
