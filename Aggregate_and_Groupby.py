#Most Common Aggregation Functions

# sum()

# mean()

# median()

# min()

# max()

# count()

# std()

df['Age'].sum()

df['Age'].mean()

df['Age'].median()
df['Age'].min()
df['Age'].max()
df['Age'].count()
df['Age'].std()

df["Age"].agg(["sum","mean","median","min","max","count","std"])


#Groupby  Function

#Basic Syntax:

#df.groupby("column_name").aggregation_function()




df.groupby('City') ['Age'].mean()

df.groupby('City') ['Age'].count()
