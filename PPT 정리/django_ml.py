#%%
import pandas as pd
import numpy as np

#%%

class Movie:
    def __init__(self,genre,*args):
        
        self._genre = genre #유저가 선택한 영화장르입니다.
        self._user_movie = args[0]   #유저가 선택한 영화제목입니다.
        self._course_similarity_df = None   # 상관관계 데이터프레임 변수

        
    def start(self):
        
        self.data_process()   
        
        return self.result_movie()
        
    def data_load(self):
        data = MMovie.objects.filter(movie_genre = self._genre).select_related('item')
        return data
        
    def data_process(self):
        
        #데이터 프레임 피봇테이블로 변경
        user_score = self.data_load().pivot_table(index=['comment_username'],columns=['movie_id'],values='comment_point')
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


a = Movie(1,['14241','54545','12342'])


#%%

a._genre


# %%
