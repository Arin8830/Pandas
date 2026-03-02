import pandas as pd

data = {
    "Name": ["Max", "Rahul", "Neha","Ram","Sham"],
    "Age": [22, 24, 23,25,26],
    "City": ["Pune", "Mumbai", "Nagpur","Amravati","Hyderabad"]
}

df = pd.DataFrame(data)


print(df)

print(df.index)

print(df.columns)

print(df.dtypes)

print(df.head(2))

print(df.tail(2))

print(df.size)

print(df.shape)





