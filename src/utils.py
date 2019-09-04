
import pandas as pd

def hello_world():
    print("")
    print("hello world!")


def show_df(df):
    print(df.shape)
    display(df.head())
    display(df.describe())