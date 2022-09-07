import pandas
import pickle

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize

NUM_RESULT = 5

class RecommenderModel :
    def __init__(self):
        return 
        
    def load_data(self):
        print("Initializing recommender model")

        # loading rule pickle file 
        try:
            try:
                with open('pickle_folder/rules.pkl', 'rb') as f:
                    lookup_table = pickle.load(f) 
            except:
                print("error file")
                with open('C:/Users/RHT9HC/Documents/Digital_CV_Dataset/RecommendFlask-AssociationRule/pickle_folder/rules.pkl', 'rb') as f:
                    lookup_table = pickle.load(f)
        except Exception as e:
            print("None")
            # if it's wrong then return None 
            return None

        return lookup_table

    ### convert the series consequents and list out the courses 
    def to_list_recommend_course(self,series_ant,series_cons,unique_course_list):
        for item in series_ant:
            for course in list(item):
                # avoid duplicate course 
                if course not in unique_course_list:
                    unique_course_list.append(course)

        for item in series_cons:
            for course in list(item):
                # avoid duplicate course 
                if course not in unique_course_list:
                    unique_course_list.append(course)

        return unique_course_list

    def check_word_the_same(self, found_word , words):
        if(found_word.lower() in str(words).lower()):
            for text in list(words): 
                for token in text.split():
                    if(token.lower() == found_word.lower()):
                        return True
        return False
            
    # defining a function that recommends 10 most similar movies
    def rcmd(self,courses):
        print('Fetching recommendations')
        lookup_table = self.load_data()

        # return empty course if there is exception 
        if(lookup_table is None):
            return {'courseName': []}

        # initialize the df 
        resul_df = pandas.DataFrame()

        # save the course list as result with origin request param 
        unique_course_list = []

        for courseName in courses: 
            # to avoid the duplicate course name in the url param 
            if courseName not in unique_course_list:
                unique_course_list.append(courseName)

                text_tokens = word_tokenize(courseName)

                StopWords=set(stopwords.words('english')+["development"])
                tokens_without_sw = [word.lower() for word in text_tokens if word.lower() not in StopWords]
                
                for word in tokens_without_sw:
                    print(word)
                    
                    temp_df = lookup_table[lookup_table["antecedents"].apply(lambda x: self.check_word_the_same(word, x))].sort_values(ascending=False,by='lift')
                    print(temp_df)

                    
                    resul_df = pandas.concat([resul_df, temp_df]).drop_duplicates()
 
        print(resul_df['consequents'])
        json = {}
        json['course_list'] = self.to_list_recommend_course(resul_df['antecedents'],resul_df['consequents'],unique_course_list)    
        return json
