import pandas as pd

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

def build_df(csv_addy):
    df= pd.read_csv(csv_addy)
    df["correct"]= df.apply(lambda row: correct(row), axis= 1)

    return df

def get_accuracy(df):
    counts= df["correct"].value_counts().to_list()
    accuracy= counts[0]/ (counts[0] +counts[1]) # correct / (total)
    return accuracy

def get_reach_mean(df):
    return df["reach"].mean()

def get_N(df):
    return len(df)


def get_data(df):

    return {"accuracy": get_accuracy(df),
            "reach prediction mean": get_reach_mean(df),
            "number of observations": get_N(df)
    }
