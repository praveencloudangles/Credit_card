from data_cleaning import data_cleaning

def feat_eng():
    data = data_cleaning()
    data.to_csv("credit card.csv", index=False)

    return data

feat_eng()