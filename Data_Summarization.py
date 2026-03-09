import pandas as pd

data = {
    "Date": ["Mon","Mon","Tue","Tue"],
    "City": ["Pune","Mumbai","Pune","Mumbai"],
    "Sales": [200,150,300,250]
}

df4 = pd.DataFrame(data)
df4

#pivot syntax
#df.pivot(index, columns, values)

#1)pivot()


pivot_df = df4.pivot(index="Date", columns="City", values="Sales")
print(pivot_df)


#2)pivot_table()

data = {
    "City": ["Pune","Pune","Mumbai","Mumbai"],
    "Product": ["A","A","A","B"],
    "Sales": [100,200,150,300]
}


table = pd.pivot_table(df5, index="City",columns="Product",values="Sales",aggfunc="sum") #pivot table

print(table)

df5 = pd.DataFrame(data)
df5

#3)crosstab

#syntax 
#pd.crosstab(row, column)

data = {
    "Gender": ["Male","Female","Male","Female","Male"],
    "Product": ["A","A","B","B","A"]
}

df6 = pd.DataFrame(data)
df6

ct = pd.crosstab(df6["Gender"], df6["Product"]) #crosstab
print(ct)


#4)Multi Index

#Multi-Index means multiple levels of indexing in rows or columns.

#It allows hierarchical indexing.

data = {
    "City": ["Pune","Pune","Mumbai","Mumbai"],
    "Year": [2023,2024,2023,2024],
    "Sales": [100,200,150,250]
}

df7 = pd.DataFrame(data)

df7

multi = df7.set_index(["City","Year"])
print(multi)
