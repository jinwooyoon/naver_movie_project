#%%
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from collections import Counter

class Movie:
    
    def __init__(self,genre,*args):
        self._data_path = './final_data.csv'
        # self._choice_filtering = args[0]
        # self._genre_filter = []
        self._user_movie = args[0]
        self._genre = genre
        self._course_similarity_df = None
        
    def start(self):
        
        self.data_process()
        
        return self.result_movie()
        
                
    def data_load(self):
        # self.genre_filtering()
        #영화 데이터 불러오고 칼럼 분류
        data = pd.read_csv(self._data_path,encoding='cp949')

        # data = data[['movie_id','user_id','rating','genre']]

        # 데이터 프레임 장르 필터링
        data_genre = data['genre'] == self._genre
        data = data[data_genre]
        
        return data
        
    def data_process(self):
                   
        #데이터 프레임 피봇테이블로 변경
        user_score = self.data_load().pivot_table(index=['user_id'],columns=['movie_id'],values='rating')
        # nan값 처리 후 corr 상관분석
        user_scores = user_score.fillna(0)
        user_scores = user_scores.replace(np.nan,0)
        self._course_similarity_df = user_scores.corr(method='pearson')
                
    def get_similar_courses(self,course_name):

        similar_score = self._course_similarity_df[course_name]
        similar_score = similar_score.sort_values(ascending=False)
        return similar_score

    def result_movie(self):

        similar_scores = pd.DataFrame()
        
        for course in self._user_movie:
            similar_scores = similar_scores.append(self.get_similar_courses(course),ignore_index=True)
            
        result = similar_scores.sum().sort_values(ascending=False).head(10+len(self._user_movie))
        result = list(result.index)
        result = result[len(self._user_movie):]
        
        return result 
    
movie_recommend = Movie(10,[82540,10072,10561])

movie_list = movie_recommend.start()
print(movie_list)





#%%

ff = [[82540],[10072],[10561]]
for i in ff:
    print(i[0])
    
    

#%%

class Movie:
    def __init__(self,genre,*args):
        self._data_path = './final_data.csv'
        # self._choice_filtering = args[0]
        # self._genre_filter = []

        self._genre = genre
        self._user_movie = args[0]
        self._course_similarity_df = None




movie_recommend = Movie(10,[82540,10072,10561])



#%%

movie_recommend._user_movie
#%%

movie


# movie_list = movie_recommend.start()
# print(movie_list)
# %%
