import pandas as pd

df3 = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["Max", "Rahul", "Neha", "Priya"]
})

df4 = pd.DataFrame({
    "id": [3, 4, 5],
    "salary": [50000, 60000, 70000]
})

print(df3)
print(df4)

pd.merge(df3, df4, on="id", how="inner")  #inner join
pd.merge(df3, df4, on="id", how="left") #left join
pd.merge(df3, df4, on="id", how="right")  #right join
pd.merge(df3, df4, on="id", how="outer")  #outer join


#join()


df3_index = df3.set_index("id")
df4_index = df4.set_index("id")

df3_index.join(df4_index, how="left")

#join() works using index


#concat()

pd.concat([df3, df4])

pd.concat([df3, df4], axis=1) #Column-wise (horizontal)

pd.concat([df3, df4])  #Row-wise (vertical)
