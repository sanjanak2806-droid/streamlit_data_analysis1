import pandas as pd

def get_basic_info(df):

    info = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Duplicates": df.duplicated().sum()
    }

    return info


def missing_values(df):

    missing = pd.DataFrame({
        "Column": df.columns,
        "Missing Count": df.isnull().sum(),
        "Missing Percentage":
        (df.isnull().sum()/len(df))*100
    })

    return missing.sort_values(
        by="Missing Count",
        ascending=False
    )


def statistical_summary(df):

    return df.describe(include="all")
