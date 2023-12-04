import pandas as pd

# filepath = input("Name of xlsx file: ")
df = pd.read_excel('sheet.xlsx',header=None)

def getName(col):
    name = df.iloc[0, col]  # `iloc` is used for integer-location based indexing
    if not pd.isna(name):
        return name
    
    return "Empty " + str(col)

def getCourses(col): 
    return df.iloc[1:15, col]  # Slicing from row index 1 to 9, column 'B'

def getYear():
    return input("Year: (Format: \"20XX-20XX\"): ")


print(getName(2))