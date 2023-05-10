import pandas

class DataPreparation:
    def __init__(self,path_to_csv):
        self.dataset_df = pandas.read_csv(path_to_csv,sep=",")
        print(self.dataset_df)