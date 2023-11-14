import pickle
import os,sys

from sklearn.metrics import r2_score
from src.logger import logging
from src.exception import CustomException

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as f:
            pickle.dump(obj,f)

    except Exception as e:
        raise CustomException(e,sys)        

def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report={}
        for i in range(len(list(models))):
                    model=list(models.values())[i]
                    model.fit(X_train,y_train)

                    #Make Predictions
                    y_predict=model.predict(X_test)
                    
                    test_model_score=r2_score(y_test,y_predict)
                    report[list(models.keys())[i]]=test_model_score
        return report     
    except Exception as e:
         logging.info('Exception occurred during model training')
         raise CustomException(e,sys)       

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
         
    except Exception as e:
        logging.info('Exception Occurred in load_object function utils')  
        raise CustomException(e,sys) 