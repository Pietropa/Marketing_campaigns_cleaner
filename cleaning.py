import pandas as pd
import numpy as np
from cleaning_funcs import clean_string, clean_data, numeric_variables,unique_ID, new_df_db, index_a

df = pd.read_csv('KAG_conversion_data.csv')
uniqueID_list =['ad_id','xyz_campaign_id','fb_campaign_id','age','gender','interest']
pattern = '\-|\@|\€|\,'

def run(df):
    clean_data(df,'Total_Conversion')
    clean_data(df,'interest')
    numeric_variables(df,'age')
    numeric_variables(df,'gender')
    unique_ID(df,uniqueID_list)
    
    Visits_tab = new_df_db(df,'Clicks')
    conversion_tab = new_df_db(df,'Total_Conversion')
    purchase_tab = new_df_db(df,'Approved_Conversion')
    index_a(Visits_tab,'uniqueID','Clicks')
    index_a(purchase_tab,'uniqueID','purchase')
    index_a(conversion_tab,'uniqueID','addtocart')
    
    Visits_tab = Visits_tab.drop(['Approved_Conversion', 'Total_Conversion'],axis=1) #,'y','a','f'
    purchase_tab = purchase_tab[['ID_final','Approved_Conversion']]
    conversion_tab =conversion_tab[['ID_final','Total_Conversion']]
    Visits_tab.head()
    
    df_d =pd.merge(Visits_tab,purchase_tab, how='left', on='ID_final')
    df_final=pd.merge(df_d,conversion_tab,how='left', on='ID_final')
    clean_data(df_final,'Total_Conversion')
    df_final.fillna(0, inplace = True)
    return df_final

df_final = run(df)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pylab as plt
from sklearn.preprocessing import MinMaxScaler

X = df_final[['age_n','gender_n','interest']]
y = df_final['Total_Conversion']
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=50)
lr=LogisticRegression()
lr.fit(Xtrain, ytrain)

print("train score :", lr.score(Xtrain, ytrain))
print("test score  :", lr.score(Xtest, ytest))
