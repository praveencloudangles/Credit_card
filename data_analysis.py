from data_loading import data_loading

def data_analysis():
    data = data_loading()
    
    print("before null values------------",data.isnull().sum())
    print("duplicate values-------------",data.duplicated().sum())
    print("describe------------------",data.describe())

    return data

data_analysis()