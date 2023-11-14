import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import numpy as np
import sys,os
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
# Data Transformation config
@dataclass 
class DataTransformationconfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')



#Data Transformation initiation
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationconfig()

    def get__data_transformation_object(self):
        try:
            logging.info("Data Transformation initiated")
            # Segregating numerical and categorical columns
            numerical_col=['carat','depth','table','x','y','z']
            categorical_col=['cut','color','clarity']
            # Define custom ranking for each ordinal variables
            cut_categories=['Fair','Good','Very Good','Premium', 'Ideal']
            color_categories=['D','E','F','G','H','I','J']
            clarity_categories=['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            logging.info('Pipeline initiated')
            #Numerical Pipeline
            numerical_pipeline=Pipeline(steps=[
                ('imputer',SimpleImputer(strategy="median")),
                ('scaler',StandardScaler())
            ])

            #Categorical Pipeline
            categorical_pipeline=Pipeline(steps=[
                ('imputer',SimpleImputer(strategy="most_frequent")),
                ('encoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
            ])

            preprocessor=ColumnTransformer([
                ('numerical_pipeline',numerical_pipeline,numerical_col),
                ('categorical_pipeline',categorical_pipeline,categorical_col)
            ])
            return preprocessor
        except Exception as e:
            logging.info('Error occurred during Data Transformation')
            raise CustomException(e,sys)
        
    def initiate_datatransformation(self,train_path,test_path):
        try:
            #Reading train and test data
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train DatFrame Head:\n{train_df.head().to_string()}')
            logging.info(f'Test DatFrame Head:\n{test_df.head().to_string()}')

            logging.info('Obtaining preprocessor object')
            preprocessing_obj=self.get__data_transformation_object()

            #features into independent and dependent features
            target_column_name='price'
            drop_columns=[target_column_name,'id']

            input_train_df=train_df.drop(columns=drop_columns,axis=1)
            target_train_df=train_df[target_column_name]

            input_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_test_df=test_df[target_column_name]
            
            #applying the transformation
            input_feature_train_arr=preprocessing_obj.fit_transform(input_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_test_df)
            
            logging.info('Applying preprocessing object on training and test data')
            train_arr=np.c_[input_feature_train_arr,np.array(target_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            logging.info('Processor pickle is created')

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
            
    
        except Exception as e:
            logging.info("exception occurred in initiating data transformation")
            raise CustomException(e,sys)      

