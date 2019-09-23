#GENERALIZED FUNCTIONS

#Cleaning functions
def drop_rename(df,x,y):
    
    df=df.drop(x,axis=1)
    df.rename(columns=y,inplace =True)
    return df

def clean_string(x):
    import re
    
    s = re.sub(pattern, '', x)
    return s.lower()

def clean_data(df,x):
    import pandas as pd

    df[x]= df[x].astype('str')
    df[x] = pd.to_numeric(df[x], errors='coerce',downcast='signed')

def numeric_variables(df,x):
    variables = list(df[x].unique())
    variables_count = list(range(len(df[x].unique())))
    audiences= dict(zip(variables,variables_count))
    df[f'{x}_n'] = df[x].map(audiences)
     
 #Dataframe transformation functions  
def unique_ID(df,uniqueID_list):
    df['uniqueID'] = df[uniqueID_list].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
    

def new_df_db(df,x):
    y = df.loc[df.index.repeat(df[x])] 
    return y

def index_a(df,x,m):
    df['y'] = df[x].shift(1)

    df['a'] = (df['y'] != df[x]).astype(int)

    df.reset_index(inplace=True)

    transition_points = list(df[df['a'] == 1].index)

    cycle_list = []
    for i in range(len(transition_points)):
        try:
            cycle = range(0, (transition_points[i+1] - transition_points[i]))

        except IndexError:
            cycle = range(0, len(df)-len(cycle_list)) #think of a better way to find this number without hardcoding it!

        cycle_list += cycle

    df['f'] = cycle_list
    df['ID_final']= df[x]+'-'+df['f'].astype(str)
    df[m]= 1
    df.drop(['y','a','f'], axis=1, inplace=True)


# extra functions   
def new_value(df,x,y):
    new_value=[]
    for i in df[x]:
        d = i* y
        new_value.append(d)
    return new_value

def date_extractor(df,x):
    import datetime as dt
    df['month'] = df[x].dt.month
    df['year']= df[x].dt.year
    df['day_of_week'] = df[x].dt.weekday_name

#test for travis


