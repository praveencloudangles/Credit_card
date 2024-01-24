from data_analysis import data_analysis

def data_cleaning():
    data = data_analysis()
    data['MINIMUM_PAYMENTS'].fillna(data['MINIMUM_PAYMENTS'].median(),inplace=True)
    data['CREDIT_LIMIT'].fillna(data['CREDIT_LIMIT'].mean(),inplace=True)
    print("after null values------------", data.isnull().sum())
    df = data.drop(['CUST_ID', 'TENURE', 'CASH_ADVANCE_FREQUENCY', 'ONEOFF_PURCHASES'], axis=1)

    print(df)
    
    return df

data_cleaning()
