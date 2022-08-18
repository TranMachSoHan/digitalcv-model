# importing the libraries

import numpy as np
import pandas as pd
import os 

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

from dotenv import dotenv_values

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

# load all environment data values 
temp = dotenv_values(".env")
engine = db.create_engine(temp['SQLALCHEMY_DATABASE_URI'])

# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
class Students(Base):
 
    __tablename__ = 'courses'
 
    first_name = db.Column(db.String(50),
                           primary_key=True)
    last_name  = db.Column(db.String(50),
                           primary_key=True)
    course     = db.Column(db.String(50))
    score      = db.Column(db.Float)
    
# # CONNECT WITH MYSQL DATABASE 
try:
    if connection.is_connected():
        # notify mysql successfully connected 
        cursor = connection.cursor()
        cursor.execute("select database();")
        db = cursor.fetchone()
        print("You're connected to dtabase: ", db)
        print("\n*****************")

        # get dataframe from mysql 
        query = "Select * from courses;"
        result_dataFrame = pd.read_sql(query,connection)
        print(result_dataFrame.head())
        
except Error as e:
    print("Error while connecting to MySQL", e)


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

if connection.is_connected():
  cursor.close()
  connection.close()
  print("MySQL connection is closed")
