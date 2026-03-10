#Vectorization

# 1) Vectorization means applying operations to an entire column (array) at once instead of using loops.

# 2) Pandas and NumPy are optimized for vectorized operations, so they run much faster than Python loops. 

import pandas as pd

df8 = pd.DataFrame({
    "salary": [20000, 30000, 40000]
})

# Vectorized operation
df8["bonus"] = df8["salary"] * 0.10
print(df8)

# Vectorized operations:

# 1) Run in C-level optimized code

# 2) Avoid Python loop overhead

# 3) Are much faster

#Avoiding Loops in Pandas

#Because Pandas is designed for column operations, not row-by-row processing

# | Method        | Purpose          |
# | ------------- | ---------------- |
# | vectorization | fastest          |
# | `apply()`     | medium speed     |
# | `map()`       | mapping values   |
# | `transform()` | group operations |


#Memory Usuage In Pandas

#Large datasets can consume a lot of RAM, so memory optimization is important.

print(df8.memory_usage())

#Techniques to Reduce Memory

#1) Use correct data types

#  2) Use categorical dtype

# ️⃣ 3) Drop unnecessary columns

# ️⃣4)  Read only required columns


#Others Optimization Concepts

# | Function     | Use                                 |
# | ------------ | ----------------------------------- |
# | `map()`      | element-wise operation on series    |
# | `apply()`    | apply function to rows/columns      |
# | `applymap()` | element-wise operation on dataframe |

