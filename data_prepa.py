import pandas
import numpy

class DataPreparation:
    def __init__(self,path_to_csv):
        self.dataset_df = pandas.read_csv(path_to_csv,sep=",")
        self.get_prepared_data


    def get_prepared_data(self):
        """Ajouter une colonne index_time"""

        self.dataset_df["index_time"] = numpy.arrange(1, (self.dataset_df)+1, 1)

        "Normaliser les données"

        self.dataset_mean = self.dataset_df["Passengers"].mean() 
        self.dataset_std = self.dataset_df["Passengers"].std()

        self.dataset_df["Passengers"] = (self.dataset_df["Passengers"] - self.dataset_mean)/self.dataset_std

        dataset_length = len(self.dataset_df)
        index_split = int(dataset_length*0.75)
        train_df = self.dataset_df[ : index_split]
        test_df = self.dataset_df[index_split: ]

        self.x_train = train_df[["index_time"]].values
        self.y_train = train_df[["passengers"]].values

        self.x_test = test_df[["index_time"]].values
        self.y_test = test_df[["passengers"]].values