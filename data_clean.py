import pandas as pd

def clean_data():
    df = pd.read_csv('/workspaces/loandash/data/loan_data.csv')
    df.head()

    df['Gender'] = df['Gender'].map({'male': 1, 'female': 0})
    df = df.drop('education', axis=1)
    df = df.drop(['paid_off_time', 'due_date', 'effective_date','Loan_ID'], axis=1)

    for i in df.index:
        if pd.isna(df.at[i, 'past_due_days']):
            df.at[i, 'past_due_days'] = 0

    df = df.reset_index(drop=True)

    unique_class = df['loan_status'].unique()

    class_to_num = {}
    num = 0
    for cls in unique_class:
        class_to_num[cls] = num
        num += 1

    encoded_target = []
    for val in df['loan_status']:
        encoded_target.append(class_to_num[val])

    df['loan_status_encoded'] = encoded_target
    df = df.drop('loan_status', axis=1)

    return df

df = clean_data()
df