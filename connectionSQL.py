# importing the libraries

import numpy as np
import pandas 
import os 

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

from dotenv import dotenv_values

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

# importing required modules
from zipfile import ZipFile

Base = declarative_base()

# load all environment data values 
temp = dotenv_values(".env")

# Database parameter
host = 'hc0vm00007.apac.bosch.com'
user = 'digitalcv-dev'      
passwd = 'tXS0CZSI+x3FLz4SG'
database = 'digitalcv-dev'

try:
    # DEFINE THE ENGINE (CONNECTION OBJECT)
    engine = db.create_engine(f'mysql+pymysql://{user}:{passwd}@{host}/{database}')

    ################## CREATE THE TABLE MODEL TO USE IT FOR QUERYING ##################
    class Courses(Base):

        __tablename__ = 'courses'
        
        name = db.Column(db.String(255),
                                primary_key=True)
        description = db.Column(db.String(255))
        level = db.Column(db.String(255))

    ################ START OF READ SQL FILE ################ 




    ################ QUERY TO FETCH ALL RECORDS FOR COURSES DATABASE ################ 
    print("Getting courses from database ....")
    courses = pandas.read_sql_query(
        sql = db.select([Courses.id,
                            Courses.name,
                            Courses.url,]), con=engine
    )

    print("Succesfully retrieved courses database. Here is the information: ")
    print('- Length of the courses in the database: ', len(courses))
    print('- Number of duplicated unique name are: ',courses.name.duplicated().sum())
    print(courses)
    print('Type of courses ', type(courses))
    print('\n')
    ################ END OF QUERY TO FETCH ALL RECORDS FOR COURSES DATABASE ################ 



    ################ Start of Tags Column ################ 
    data = courses.rename(columns={'name': 'CourseName', 'level': 'DifficultyLevel', 'description':'CourseDescription'})
    data['Tags'] = data['CourseName'] + data['DifficultyLevel'] + data['CourseDescription']
    ################ End create Tags Column ################ 



    ################ Start Content Based Dataframe ################ 
    contentBaseDf = data[['CourseName','Tags']]

    # Bring back to space again 
    contentBaseDf['Tags'] = data['Tags'].str.replace(',',' ')
    contentBaseDf['CourseName'] = data['CourseName'].str.replace(',',' ')

    # lower casing the tags column
    contentBaseDf['Tags'] = contentBaseDf['Tags'].apply(lambda x:x.lower()) 
    ################ End Content Based Dataframe ################ 


    ################ Start Text Processing ################ 
    ## Lower casing
    contentBaseDf["Tags"] = contentBaseDf["Tags"].str.lower()
    
    ## Removal of Punctuations
    PUNCT_TO_REMOVE = string.punctuation
    def remove_punctuation(text):
        """custom function to remove the punctuation"""
        return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))

    contentBaseDf["Tags"] = contentBaseDf["Tags"].apply(lambda text: remove_punctuation(text))

    ################ End Text Processing ################ 

except:
    print("None")
