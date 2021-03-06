import json

import config
import pandas as pd

with open(config.factor_codes) as file:
    factor_codes = json.load(file)

def decoder_features(Sex, Age, Department, Education, recruitment_channel, length_of_service, KPIs_met, Awards_won, Avg_training_score):
    """ Performing Decoding 
    return: a decoded oject with input features"""
    Sex = factor_codes['gender'][Sex]
    Age_label = pd.cut(x=[Age], bins=[20,35,55,60], labels = ['Young Adult','Middle Age','Senior citizen'])
    Age = factor_codes['Age'][Age_label[0]]
    Department = factor_codes['department'][Department]
    Education = factor_codes['education'][Education]
    recruitment_channel = factor_codes['recruitment_channel'][recruitment_channel]
    len_service_label= pd.cut(x=[length_of_service], bins=[0,5,10,20,30,40], labels = ['<5','5-10','10-20','20-30','30-40'])
    length_of_service = factor_codes['Length_of_service'][len_service_label[0]]
    KPIs_met = factor_codes['KPIs_met'][KPIs_met]
    Awards_won = factor_codes['Awards_won'][Awards_won]
    avg_train_label = pd.cut(x=[Avg_training_score], bins=[39,50,75,100], labels = ['Third class','Second class','First class'])
    Avg_training_score = factor_codes['Avg_training_score'][avg_train_label[0]]
    return Sex, Age, Department, Education, recruitment_channel, length_of_service, KPIs_met, Awards_won, Avg_training_score
##print(decoder_features("Male",23,"Finance","Below Secondary","other",6,"Yes","Yes",100))


def organise_features(Sex, Age, Department, Education, recruitment_channel, No_of_Trainings, Previous_year_rating, length_of_service, KPIs_met, Awards_won, Avg_training_score):
    Sex, Age, Department, Education, recruitment_channel, length_of_service, KPIs_met, Awards_won, Avg_training_score = decoder_features(Sex, Age, Department, Education, recruitment_channel, length_of_service, KPIs_met, Awards_won, Avg_training_score)
    final_factors= [Sex, Age, Department, Education, recruitment_channel, No_of_Trainings, Previous_year_rating, length_of_service, KPIs_met, Awards_won, Avg_training_score]
    return [final_factors]





##print(organise_features("Male",23,"Analytics","Below Secondary","other",5,4,6,"Yes","Yes",50))













