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
host = temp['DBHOST']       
user = temp['DBUSER']          
passwd = temp['DBPASS']    
database = temp['DBNAME']

# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine(f'mysql+pymysql://{user}:{passwd}@{host}/{database}')

################## CREATE THE TABLE MODEL TO USE IT FOR QUERYING ##################
class Courses(Base):
 
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),
                           primary_key=True)
    url  = db.Column(db.String(300),
                           primary_key=True)

class Reviews(Base): 
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.BIGINT)
    employee_id = db.Column(db.BIGINT)

class Employees(Base): 
    __tablename__ = 'employees'
    id = db.Column(db.BIGINT, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

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
print('Type of courses ', type(courses))
print('\n')

################ QUERY TO FETCH ALL RECORDS FOR REVIEWS DATABASE ##################
print("Getting reviews from database ....")

reviews = pandas.read_sql_query(
    sql = db.select([Reviews.id,
                     Reviews.course_id,
                     Reviews.employee_id,]), con=engine
)


print("Succesfully retrieved reviews database. Here is the information: ")
print('- Length of the reviews in the database: ', len(reviews))
print('Type of reviews ', type(reviews))
print(reviews)
print('\n')

################ QUERY TO FETCH ALL RECORDS FOR EMPLOYEES DATABASE ################ 
print("Getting employees from database ....")

employees = pandas.read_sql_query(
    sql = db.select([Employees.id,
                     Employees.first_name,
                     Employees.last_name,]), con=engine
)
# Let the reviewers name to be first_name and last_name 
employees['reviewers'] = employees['first_name'] + ' ' + employees['first_name']
employees = employees.rename(columns={'id': 'employee_id'})

print("Succesfully retrieved employees database. Here is the information: ")
print('- Length of the employees in the database: ', len(employees))
print('Type of employees ', type(employees))
print(employees)
print('\n')
######################## END OF READ SQL FILE ##############################



######################## START OF PROCESSED SQL DATA #######################
course_reviews = reviews.merge(employees,on = 'employee_id',how = 'inner')
print(course_reviews)
######################## END OF PROCESSED SQL DATA #######################



######################## READ COURSERA REVIEWS FILE ######################
filepath = './'
zf = ZipFile(f'{filepath}final.zip')
# if you want to see all files inside zip folder
print(zf.namelist() )
# read csv coursera reviews from the zip 
coursera_reviews = pandas.read_csv(zf.open('final/Coursera_reviews.csv'))
print(coursera_reviews)

# since the reviewers name has by which is not expected , then we will remove By word 
coursera_reviews['reviewers'] = coursera_reviews['reviewers'].str.replace('By ','', regex=True)
######################## END READ COURSERA REVIEWS FILE ######################



######################## START MERGE THE COURSERA REVIEWS WITH REVIEW FROM SQL ################################

######################## END MERGE THE COURSERA REVIEWS WITH REVIEW FROM SQL ################################




# print("############################")
# print(f"Coursera rating value counts: ")
# print(f"{coursera_rating.course_id.value_counts()}")

# # Merging dataset 
# merge = coursera_courses.merge(coursera_rating,on = 'course_id',how = 'inner')

# merge['reviewers'] = [f"{x.replace('By ', '')}" for x in merge['reviewers']]
# merge.drop(columns=['institution','date_reviews','rating', 'reviews'],inplace=True)
# merge.rename(columns={'name': 'CourseName',
#                  'course_url': 'UrlLink',
#                  'reviewers': 'UserId', 'course_id':'ourseId' }, inplace=True)

# print("\n############################")
# print(f"Length of the merge unique user id: {len(merge.UserId.unique())}")

# # Finalize merge list 
# merge_list = merge.groupby(by = ["UserId"])["CourseName"].apply(list).reset_index()
# merge_list = merge_list["CourseName"].tolist()

# ## DATA TRANSFORMATION
# te = TransactionEncoder()
# te_ary = te.fit(merge_list).transform(merge_list)
# df = pd.DataFrame(te_ary, columns=te.columns_)

# # Generate frequen itemsets 
# fpgrowth_frequent_itemsets = fpgrowth(df, min_support=0.0001, use_colnames=True,max_len=5)
# fpgrowth_frequent_itemsets.head()
# fpgrowth_frequent_itemsets['itemsets'].apply(lambda x: len(x)).value_counts()

# # Association rules 
# rules = association_rules(fpgrowth_frequent_itemsets,metric="lift",min_threshold=0.01)

# # Save rule to pickle 
# print("\n############################")
# print("#### CONVERTING RULES TO PICKLE ####")
# rules.to_pickle('./pickle_folder/rules.pkl')
