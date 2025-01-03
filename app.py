from src.BHP.loggers import logging
from src.BHP.exception import CustomException
import sys
from src.BHP.components.data_ingetion import Dataingetion,Dataingetionconfig

if __name__=="__main__":
    logging.info("execution started")

    try:
        #data_ingetion_cofig=Dataingetionconfig()
        data_ingetion=Dataingetion()
        train,test=data_ingetion.initiate_data_ingetion()

        
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)        