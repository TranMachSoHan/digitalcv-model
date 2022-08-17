# importing the libraries

import numpy as np
import pandas as pd
import os 

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

from datetime import datetime

import csv
from datetime import datetime

# Here we are storing our data in a
# variable. We'll add this data in
# our csv file
rows = [['GeeksforGeeks1', 'GeeksforGeeks2'],
        ['GeeksforGeeks3', 'GeeksforGeeks4'],
        ['GeeksforGeeks5', 'GeeksforGeeks6']]
  
# Opening the CSV file in read and
# write mode using the open() module
with open(r'YOUR_CSV_FILE.csv', 'r+', newline='') as file:
  
    # creating the csv writer
    file_write = csv.writer(file)
  
    # storing current date and time
    current_date_time = datetime.now()
  
    # Iterating over all the data in the rows 
    # variable
    for val in rows:
          
        # Inserting the date and time at 0th 
        # index
        val.insert(0, current_date_time)
          
        # writing the data in csv file
        file_write.writerow(val)
    
# filepath = '/content/drive/MyDrive/DigitalCV_CourseRecommendation/'
filepath = './'

# # reading the data
# coursera_courses = pd.read_csv(f'{filepath}coursera_course/Coursera_courses.csv')
# coursera_rating = pd.read_csv(f'{filepath}coursera_course/Coursera_reviews.csv')

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
