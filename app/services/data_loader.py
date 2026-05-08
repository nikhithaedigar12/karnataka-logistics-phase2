import pandas as pd

def load_data():
    df = pd.read_csv("app/data/sample_data.csv")
    return df