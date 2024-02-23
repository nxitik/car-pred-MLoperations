import os
from carPred import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from carPred.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up


    def eda(self):
        data = pd.read_csv(self.config.data_path)
        data = data.drop(['ind'], axis = 1)

        cat = []
        num = []
        for i in data.columns:
            if data[i].dtypes == 'O':
                cat.append(i)
            else:
                num.append(i)
        data_n=data[num]   # new dataframe just type numeric
        data_c=data[cat]

        label_encoders = {}
        categorical_columns = data_c.columns  # I would recommend using columns names here if you're using pandas. If you're using numpy then stick with range(n) instead

        for column in categorical_columns:
            label_encoders[column] = LabelEncoder()
            data_c[column] = label_encoders[column].fit_transform(data_c[column])

        frames = [data_c, data_n]
  
        data = pd.concat(frames,axis=1)
        print(data.head())
        return data



    def train_test_spliting(self):
        data = DataTransformation.eda(self)

        # Split the data into training and test sets. (0.75, 0.25) split.
        
        

        
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)