import pandas as pd

def getSheet(path):
    # filepath = input("Name of xlsx file: ")
    print(path)
    global df
    df = pd.read_excel(path, header=None)

def getName(col):
    name = df.iloc[0, col]  # `iloc` is used for integer-location based indexing
    if not pd.isna(name):
        return name
    
    return "Empty " + str(col)

def getCourses(col): 
    return df.iloc[1:15, col]  # Slicing from row index 1 to 9, column 'B'
