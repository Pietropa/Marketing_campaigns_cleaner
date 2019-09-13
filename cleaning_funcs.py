#GENERALIZED FUNCTIONS
#Data cleaning functions
pattern = '\-|\@|\€|\,'
def clean_string(s):
    
    s = re.sub(pattern, '', s)
    return s.lower()

def clean_data(df1,x):

    df1[x]= df1[x].astype('str')
    df1[x]=df1[x].apply(clean_string)
    df1[x] = pd.to_numeric(df1[x], errors='coerce',downcast='signed')
    #df1[x] = df1[x].astype(int)
    
def numeric_variables(df,x):
    variables = list(df[x].unique())
    variables_count = list(range(len(df[x].unique())))
    audiences= dict(zip(variables,variables_count))
    df[f'{x}_n'] = df[x].map(audiences)
    
#Data set reshaping 

#Create new dataframe based on a metric
def new_df_db(df,x):
    y = df.loc[df.index.repeat(df[x])]
    return y

#where x needs to be the reference column identifier and m the metric on which the data set needs to be disaggregated, 
#better to start with visits and the repeating the same process for other metrics
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
            cycle = range(0, len(df)-len(cycle_list)) 

        cycle_list += cycle

    df['f'] = cycle_list
    df['ID_final']= df[x]+'-'+df['f'].astype(str)
    df[m]= 1
    df.drop(['y','a','f'], axis=1)


