# Import for Data Manipulation
import pandas as pd

# Import for scaling and splitting data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Acquire function
def acquire_student_data():   
    '''
    This function reads in a excel file and returns it as a dataframe.
    '''   
    # Read excel into df
    df = pd.read_excel('college_retention_data.xlsx',sheet_name=1) 
    # Return df
    return df

# manipulate cip df for ease of use and create function
def get_cip_codes():
    # read in df
    cip = pd.read_csv('cip_codes.csv')
    # Narrow down df
    cip = cip[['Title','CIP Code']]
    # Fix columns
    cip.columns = [col.lower().replace(' ','_') for col in cip]
    # fix cip values
    cip['cip_code'] = cip.cip_code.apply(lambda x: x[2:4])
    # make int
    cip['cip_code'] = cip.cip_code.astype('int')
    # Rename cip column
    cip = cip.rename(columns={'cip_code':'cip'})
    # fix title vlaues
    cip['title'] = cip.title.apply(lambda x: x.lower().replace(' ' , '_').replace( '.' , ''))
    # return df
    return cip

# Create prep function
def prep_student_data(df):
    
    '''
    This function takes in the acquired dataframe and prepare the data for exploration.
    '''
    
    # Lowercase all column names
    df.columns = [col.lower() for col in df]
    
    # Change column names for ease of use
    df = df.rename(columns={'fakeid':'id','enrolled_1_back':'enrolled_between','student_classif':'student_year',\
                                    'originaltype':'enroll_type','cip_2dig':'cip','astd':'academic_standing',\
                                    'dubya_count_term':'w_count','span':'yrs_since_start','days_between':'reg_before_start'})
    
    # Drop UN cip value
    df = df[df['cip'] != 'UN']
    
    # Retrieve cip codes with descriptions and return dataframe
    cip = get_cip_codes()
    
    # Merge the df's
    df = pd.merge(df,cip, on='cip', how='left')
    
    # fix age at start term variables (23 - 29, to 23-29)
    df['age_at_start_term'] = df.age_at_start_term.str.replace(' ','').str.replace('or','-')
    
    # One hot encode categorical columns
    # Replace (1,0): retained, enrolled_between, sex, time_status, pell_ever, academic_standing, fa_recd, w_count
    df['retained'] = df.retained.str.replace('Y', '1').str.replace('N', '0')
    df['enrolled_between'] = df.enrolled_between.str.replace('Y', '1').str.replace('N', '0')
    df['sex'] = df.sex.str.replace('F', '1').str.replace('M', '0')
    df['time_status'] = df.time_status.str.replace('FULL', '1').str.replace('PART', '0')
    df['pell_ever'] = df.pell_ever.str.replace('Y', '1').str.replace('N', '0')
    df['academic_standing'] = df.academic_standing.str.replace('GOODBIN', '1').str.replace('ISSUEBIN', '0')
    df['fa_recd'] = df.fa_recd.str.replace('Y', '1').str.replace('N', '0')
    df['w_count'] = df.w_count.str.replace('ONE_OR_MORE', '1').str.replace('NONE', '0')
    
    # Reassign as int type
    df[['retained','enrolled_between','sex','time_status','pell_ever','academic_standing','fa_recd','w_count']] = \
    df[['retained','enrolled_between','sex','time_status','pell_ever','academic_standing','fa_recd','w_count']].astype('int')
    
    # Create dummies: race_ethn, fgen, student_year, enroll_type, cip, age_at_start_term, act, depend_status, yrs_since_start
    dummy_name = pd.get_dummies(df[['race_ethn','fgen','student_year','enroll_type','title','age_at_start_term','act',\
                                    'depend_status','yrs_since_start']],dummy_na=False)
    # Combine df's
    df = pd.concat([df,dummy_name],axis=1)
    
    # Leaving in to note that before hs_gpa and efc were dropped and all null values were dropped instead these columns only showed up as 1 to 5 values
    # now they show up as over 100_000 so there is a relation to lack of data between efc, hs_gpa, depend_status, and fgen. 
    # Could this part of the population be considered a subset for analysis. how are they related?
#     # Drop depend_status_unk, fgen_1Gx, id for dimensionailty reduction
#     df = df.drop(columns=['depend_status_unk','fgen_1GX'])
    
    # Drop hs_gpa and efc for initial pass
    df = df.drop(columns=['hs_gpa','efc'])
    
    # Drop Nulls for initial pass
    df = df.dropna()
    
    # Return cleaned df
    return df, dummy_name

def split_data(df,target):
    '''
    This funciton splits the dataset for modeling into:
    train - for exploring the data, and fitting the models
    validate - for ensuring the model is not overfit
    test - for testing the model on unseen data
    '''
    # This seperates out the test data from the train and validate data. Test makes up 20 % of the data.
    train_validate, test = train_test_split(df, random_state=1729, test_size=0.2, stratify=df[target])
    
    # This seperates out the train and validates sets. Train makes up 56 % of the data and Validate makes up 24 %.
    train, validate = train_test_split(train_validate, random_state=1729, test_size=0.3, stratify=train_validate[target])
    
    # The funciton returns the split sets
    return train, validate, test

def scale_data(train, validate, test, return_scaler=False):
    '''
    This function scales the split data and returns a scaled version of the dataset.
    
    If return_scaler is true, the scaler will be returned as well.
    '''
    
    # Add pack hs_gpa after impute
    col = ['reg_before_start','term_gpa']

    train_scaled = train[col]
    validate_scaled = validate[col]
    test_scaled = test[col]

    scaler = MinMaxScaler()
    scaler.fit(train[col])
    
    train_scaled[col] = scaler.transform(train[col])
    validate_scaled[col] = scaler.transform(validate[col])
    test_scaled[col] = scaler.transform(test[col])
    
    if return_scaler:
        return train_scaled, validate_scaled, test_scaled, scaler
    else:
        return train_scaled, validate_scaled, test_scaled

def model_split(df, target):
    
    # Assign x for testing the model, y as target for modeling
    X = df.drop(columns=[target])
    y = df[target]
    
    return X, y
