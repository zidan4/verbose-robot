df.isnull().sum()

"""However, if you want to see the percentages, we wrote a function you can use:"""

def nulls_summary_table(df):
    """
    Returns a summary table showing null value counts and percentage

    Parameters:
    df (DataFrame): Dataframe to check

    Returns:
    null_values (DataFrame)
    """
    null_values = pd.DataFrame(df.isnull().sum())
    null_values[1] = null_values[0]/len(df)
    null_values.columns = ['null_count','null_pct']
    return null_values

nulls_summary_table(df)

"""### Dropping Null Values

Dropping nulls is the quickest and easiest method to dropping nulls. We will use the internal pandas method `dropna` which will simply drop all rows that contain nulls:
"""

drop_df = df.copy()

drop_df = drop_df.dropna()

X_d = drop_df[['age','days_on_platform','income']]
y_d = drop_df['lifetime_value']


X_train_d = X_d[:4000]
y_train_d = y_d[:4000]

X_test_d = X_d[1000:]
y_test_d = y_d[1000:]
