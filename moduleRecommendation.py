import pandas
import pickle

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize

# importing required modules
from zipfile import ZipFile

NUM_RESULT = 5

class RecommenderModel :
    def __init__(self):
        return 
        
    def load_data(self):
        print("Initializing recommender model")

        filepath = './'
        zf = ZipFile('./pickle_folder/contentBaseDf.zip')
        # if you want to see all files inside zip folder
        print(zf.namelist() )

        # loading rule pickle file 
        try:
            contentBaseDf= pandas.read_csv(zf.open('contentBaseDf.csv'))
            print(contentBaseDf)
            with open('pickle_folder/similarity.pkl', 'rb') as f:
                similarity = pickle.load(f) 
                
        except Exception as e:
            print("None")
            # if it's wrong then return None 
            return None

        return similarity, contentBaseDf

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
        for token in words.split():
            if(token.lower() == found_word.lower()):
                return True
        return False

    def recommend(self, course):
        print('Fetching recommendations')
        similarity,contentBaseDf  = self.load_data()
        result = []
        for courseName in course: 
            text_tokens = word_tokenize(courseName)

            StopWords=set(stopwords.words('english')+["development"])
            tokens_without_sw = [word.lower() for word in text_tokens if word.lower() not in StopWords]

            
            for word in tokens_without_sw:
                courseIndex = contentBaseDf[contentBaseDf['CourseName'].apply(lambda x : self.check_word_the_same(word, x))]
                if(len(courseIndex) != 0):
                    courseIndex = courseIndex.index[0]
                    distances = similarity[courseIndex]
                    courseList = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])
                    for i in courseList : 
                        temp = contentBaseDf.iloc[i[0]].CourseName
                        result.insert(-1,temp)
        print(result)
        return result

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
