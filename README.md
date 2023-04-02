# PI

Uses the
https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula to compute the nth digit of PI.

Todo
1. Optimise Algorithm
2. Verification of hexdigits
3. Distributed Computing

## Case Specific Optimisations for modular exponentiation used in PI compute

To simplify, doing `a^k modulo m`  is the general problem statement, whose optimisations are compiled here https://stackoverflow.com/questions/21367824/how-to-evalute-an-exponential-tower-modulo-a-prime/21368784#21368784

To compute PI using the BBP method we use a triangle, one for each
each factor of the denominator

for 8 * k + 1 that triangle looks like
```
0  |
0  |1  |
0  |7  |1  |
0  |4  |16 |1  |
0  |1  |1  |16 |1  |
0  |7  |16 |6  |16 |1  |
0  |4  |1  |21 |25 |16 |1  |
0  |1  |16 |11 |4  |10 |16 |1  |
0  |7  |1  |1  |31 |37 |11 |16 |1  |
0  |4  |16 |16 |1  |18 |29 |28 |16 |1  |
0  |1  |1  |6  |16 |1  |23 |49 |61 |16 |1  |
0  |7  |16 |21 |25 |16 |25 |43 |1  |37 |16 |1  |
0  |4  |1  |11 |4  |10 |8  |4  |16 |8  |13 |16 |1  |
0  |1  |16 |1  |31 |37 |30 |7  |61 |55 |46 |78 |16 |1  |
0  |7  |1  |16 |1  |18 |39 |55 |1  |4  |7  |2  |62 |16 |1  |
0  |4  |16 |6  |16 |1  |36 |25 |16 |64 |31 |32 |22 |46 |16 |1  |
0  |1  |1  |21 |25 |16 |37 |1  |61 |2  |10 |67 |61 |1  |30 |16 |1  |
0  |7  |16 |11 |4  |10 |4  |16 |1  |32 |79 |4  |6  |16 |28 |14 |16 |1  |
0  |4  |1  |1  |31 |37 |15 |28 |16 |1  |49 |64 |96 |46 |109|103|127|16 |1  |
0  |1  |16 |16 |1  |18 |44 |49 |61 |16 |55 |45 |81 |1  |49 |75 |97 |119|16 |1  |
0  |7  |1  |6  |16 |1  |18 |43 |1  |37 |70 |8  |35 |16 |106|111|4  |123|111|16 |1  |
0  |4  |16 |21 |25 |16 |43 |4  |16 |8  |67 |39 |75 |46 |1  |82 |64 |50 |36 |103|16 |1  |
0  |1  |1  |11 |4  |10 |2  |7  |61 |55 |19 |1  |36 |1  |16 |102|121|115|141|118|95 |16 |1  |
0  |7  |16 |1  |31 |37 |32 |55 |1  |4  |61 |16 |91 |16 |30 |59 |1  |59 |81 |52 |71 |87 |16 |1  |
0  |4  |1  |16 |1  |18 |22 |25 |16 |64 |4  |78 |1  |46 |28 |97 |16 |122|136|67 |9  |40 |79 |16 |1  |
0  |1  |16 |6  |16 |1  |9  |1  |61 |2  |64 |2  |16 |1  |109|100|127|34 |1  |1  |144|133|25 |71 |16 |1  |
0  |7  |1  |21 |25 |16 |46 |16 |1  |32 |52 |32 |62 |16 |49 |27 |97 |133|16 |16 |50 |100|46 |26 |63 |16 |1  |
```

each row here is responsible one hex digit of pi, notice how the columns are
repeating, this is due the https://en.wikipedia.org/wiki/Euler%27s_totient_function
which implies modular exponentiation is periodic for co-prime a, m in `a^k modulo m`

The function directly gives us the period at which a coulmn repeats this allows us
to speed up `a^(n-k) modulo (8*k + 1)` = `a^(n-k modulo phi(8 * k + 1)) modulo (8*k + 1)` This speeds up the exponentiation to `O(log(phi(8 * k + 1)))` = `O(log(k))`
from `O(log(n-k))` (k <= n which is why it is a triangle as well, n = rows, k = cols)
To compute one digit we have to sum up the fractions formed by these remainders and
their respective divisor (`8 * k + 1` in example)

For one digit, the complexity of computation (assuming contant sized integers)
is `O(Sum{n}(log(n) + log(n-1) + ... log(0)))` (`log(0)` as `n >= k` in `16^0 modulo 8 * k + 1`)

which works out to equal `O(nlog(n))` per row (nth digit)

Not surprisingly the totient method also works out to `O(nlog(n))` how ever
using the fast modular exponentiation based on the period is more effective for the earlier columns, where n exceeds k by a large amount, for eg: k < n / 2.

## Towards An efficient algorithm for PI

It is trivial to see that in the triangle we can combine `m` columns togather
with a greater period and use that column as a backbone for further computation.
This combined column might be representable as a ratio of two polynomials, or even be memoized. In another line of thinking, the computation of different
parts of the triangle can be handed off to multiple machines and the final
result can be later combined.