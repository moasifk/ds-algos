Here is the Big O [Complexity chart](../big_o_complexity_chart.png)

# Big O Cheat Sheet:
-Big Os-
- O(1) Constant- no loops
- O(log N) Logarithmic- usually searching algorithms have log n if they are sorted (Binary Search)
- O(n) Linear- for loops, while loops through n items
- O(n log(n)) Log Liniear- usually sorting operations
- O(n^2) Quadratic - every element in a collection needs to be compared to ever other element. Two nested loops
- O(2^n) Exponential- recursive algorithms that solves a problem of size N
- O(n!) Factorial- you are adding a loop for every element
- Iterating through half a collection is still O(n)
## Two separate collections: O(a * b)
- What can cause time in a function?-
- Operations (+, -, *, /)
- Comparisons (<, >, ==)
- Looping (for, while)
- Outside Function call (function())
# Big O Rule Book
- Rule 1: When calculating Big O, always think about the worst case
- Rule 2: Remove constants // O(1000 + n) = O(n)
- Rule 3: Different terms for input // O(n + m) - for each input use different terms
    - For Nested loops, instead of addition, it is multiplication O(n) * O(n) = O(n^2) - Quadratic Time
    - + for steps in order
    - * for nested steps
- Rule 4: Drop Non Dominants // O(n^2 + 2n + 10000) => O(n^2)

# The three pillars of programming
- Readable
- Scalable Big O
    - Speed (Time Complexity)
    - Memory (Space Complexity)

# What causes Space complexity?-
- Variables
- Data Structures
- Function Call
- Allocations