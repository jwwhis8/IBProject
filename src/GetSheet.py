import pandas as pd

def setStudentCount(count):
    global NumberOfStudents
    NumberOfStudents = count

def getSheet(path):
    global df
    df = pd.read_excel(path, header=None)
    print(f"Loaded sheet from {path}")

def getName(col):
    # Fetch the student's name from the first row of the specified column
    name = df.iloc[0, col]
    if not pd.isna(name):
        return name
    return "Empty " + str(col)

def getCourses(col):
    # Fetch courses from the second row up to the specified number of rows for this student
    # This approach assumes that 'num_rows' includes the maximum number of courses any student can have
    # Adjust '1:num_rows+1' as needed if your data starts from a different row or if you need to check more/less rows
    return df.iloc[1:NumberOfStudents, col].dropna().tolist()
