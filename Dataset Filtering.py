#loc
df.loc[0:2]  #get values based on index

#iloc
df.iloc[0:2] #get values bsed on index but only return (stop-1) values

#filtering rows
df['Age']>25
df[df['Age']>25].head(5)  

#filtering rows using where
df.where(df['Age']>25) # where is use to get thesame shape of original dataset
df.where(df['Age']>25, other = "Not shown") #other attribute use



import pandas as pd

data = {
    "Name": ["Max", "Rahul", "Neha","Ram","Sham"],
    "Age": [22, 24, 23,25,26],
    "City": ["Pune", "Mumbai", "Nagpur","Amravati","Hyderabad"]
}
df1 = pd.DataFrame(data)
df1

#Rows and Column Opeation

df1['Roll_NO']=['10','20','30','40','50'] #Add columns


df1.loc[(df1['Age']>20) & (df1['Age']<24), 'City']='Nagpur'  #Update columns by conditions

df1.drop(columns=["Roll_NO"], inplace=True)  #Delete Columns
