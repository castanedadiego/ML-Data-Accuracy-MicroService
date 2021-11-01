import pandas as pd

df = pd.read_csv("./sample_data.csv")

def actual(row):
    REACHES = ["X1", "X2", "X3", "HR", "BB", "HBP"]
    if row["outcome"] in REACHES:
        return True
    else:
        return False

def prediction(row):
    if row["reach"] > 50.00: return True
    else: return False

def correct(row):
    if actual(row) == prediction(row):
        return True
    else: return False

df["correct"]= df.apply(lambda row: correct(row), axis= 1)

print(df["correct"].value_counts())
