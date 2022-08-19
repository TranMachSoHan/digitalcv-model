import pandas
import pickle
NUM_RESULT = 5

class RecommenderModel :
    def __init__(self):
        return 
        
    def load_data(self):
        print("Initializing recommender model")

        # loading rule pickle file 
        try:
            with open('pickle_folder/rules.pkl', 'rb') as f:
                lookup_table = pickle.load(f) 
        except Exception as e:
            print("None")
            # if it's wrong then return None 
            return None

        return lookup_table

    ### convert the series consequents and list out the courses 
    def to_list_recommend_course(self,series,unique_course_list):
        i = 0
        for item in series:
            for course in list(item):
                # avoid duplicate course 
                if course not in unique_course_list:
                    unique_course_list.append(course)

        return unique_course_list

    # defining a function that recommends 10 most similar movies
    def rcmd(self,courses):
        print('Fetching recommendations')
        lookup_table = self.load_data()

        # return empty course if there is exception 
        if(lookup_table is None):
            return {'courseName': []}

        # initialize the df 
        temp_df = lookup_table
        resul_df = lookup_table

        # save the course list as result with origin request param 
        unique_course_list = []

        for courseName in courses: 
            # to avoid the duplicate course name in the url param 
            if courseName not in unique_course_list:
                unique_course_list.append(courseName)

                # sort the lookup table by the factorized item
                # continue use the previous df ==> combine more courses together  
                temp_df = resul_df[resul_df["antecedents"].apply(lambda x: courseName in str(x))].sort_values(ascending=False,by='lift')
                
                # to avoid the temp df 
                if len(temp_df) < NUM_RESULT:
                    print(courseName)
                    continue
                resul_df = temp_df 

        json = {}
        json['course_list'] = self.to_list_recommend_course(resul_df['consequents'],unique_course_list)    
        return json
