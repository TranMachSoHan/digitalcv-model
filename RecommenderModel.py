import joblib
import pandas
import os 
NUM_RESULT = 5

def load_data():
    print("Initializing recommender model")

    pickle_file = os.path.dirname(os.path.abspath(__file__))+'/pickle_folder/rules.pkl'

    lookup_table = joblib.load(pickle_file)

    print(lookup_table)
    return lookup_table

### convert the series consequents and list out the courses 
def to_list_recommend_course(series,unique_course_list):
    i = 0
    for item in series:
        for course in list(item):
            # avoid duplicate course 
            if course not in unique_course_list:
                unique_course_list.append(course)

    return unique_course_list

# defining a function that recommends 10 most similar movies
def rcmd(courses):
    print('Fetching recommendations')
    lookup_table = load_data()

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
    json['course_list'] = to_list_recommend_course(resul_df['consequents'],unique_course_list)    
    return json