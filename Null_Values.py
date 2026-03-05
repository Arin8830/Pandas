import pandas as pd
import numpy as np

data = {
    "ID": range(1, 53),
    
    "Age": [23, 25, np.nan, 29, 31, 22, 28, np.nan, 35, 27, 24, 30, 26,
            np.nan, 33, 21, 29, 34, np.nan, 28, 32, 25, np.nan, 27, 36,
            31, 22, np.nan, 24, 30, 29, np.nan, 33, 21, 28, 35, np.nan,
            26, 32, 27, 34, np.nan, 23, 31, 29, np.nan, 24, 33, 28, 36,
            np.nan, 30],

    "Salary": [45000, 50000, 52000, np.nan, 61000, 48000, 53000, 55000,
               np.nan, 49000, 47000, 62000, np.nan, 51000, 60000, 45000,
               52000, np.nan, 58000, 54000, 61000, 50000, np.nan, 53000,
               62000, 59000, np.nan, 48000, 47000, 61000, 52000, np.nan,
               60000, 45000, 54000, 58000, np.nan, 49000, 62000, 50000,
               53000, np.nan, 47000, 61000, 52000, np.nan, 54000, 58000,
               60000, 49000, np.nan, 51000],

    "City": ["Pune", "Mumbai", "Delhi", "Pune", np.nan, "Delhi", "Mumbai",
             "Pune", "Delhi", np.nan, "Mumbai", "Pune", "Delhi", "Mumbai",
             np.nan, "Pune", "Delhi", "Mumbai", "Pune", np.nan, "Delhi",
             "Mumbai", "Pune", "Delhi", np.nan, "Mumbai", "Pune", "Delhi",
             "Mumbai", np.nan, "Pune", "Delhi", "Mumbai", "Pune", np.nan,
             "Delhi", "Mumbai", "Pune", "Delhi", np.nan, "Mumbai", "Pune",
             "Delhi", "Mumbai", np.nan, "Pune", "Delhi", "Mumbai", "Pune",
             np.nan, "Delhi", "Mumbai"]
}

df2 = pd.DataFrame(data)

#
#Handlinh null values by using different function

#1 Function

df2.fillna(0)  
#but categorical data is not handle by this function

df2.head(5)

df2['City'].fillna("Unknown", inplace=True) #categorical data also handle
df2.head(5)

#2 Function 

df2.fillna(method='ffill',inplace=True)
df2.head(5)

#3 Function 

df2.fillna(method='bfill',inplace=True)
df2.head(5)

# 4 function

df2.replace("Unknown","USA",inplace=True)
df2.head(5)

#5 Function

df2.interpolate(method='linear') #Interpolation fills missing values using neighboring values (pattern between points).
df2.head()

#different types of Interpolate() Methods
#1)Linear Interpolation
#2️) Time Interpolation
#3)Polynomial Interpolation
#4)Spline Interpolation
#5)Nearest Interpolation
#6)Quadratic Interpolation
#7)Cubic Interpolation

#6 Function

#df2['Age'].mean()

#7 Function

#df2['Age'].median()

#8 Function

#df2['Age'].mode()

#9 Function

#df2.dropna()


# **Note= If handling Null Values or Missing Values ,  First Convert Into Numerical Form (in most cases thes pattern Follow)# **
