import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from collections import Counter

#유저가 선택한 영화제목 + 장르 3개 저장

choice_filtering = [['68695','판타지'],['천녀유혼 2 - 인간도','판타지'],['신세계','범죄']]

genre_filter = []
genre = None
user_movie = []

#장르로 필터링 하기위해 중복된 장르 선택
for genre in choice_filtering:
    genre_filter.append(genre[1])

genre_filter = Counter(genre_filter)

max_value = max(list(genre_filter.values()))

# 만약에 중복된 장르가 없으면 첫번째로 선택한 영화로 진행
for key in list(genre_filter.keys()):
    if max_value == 1:
        genre = key
        break
    if genre_filter[key] == max_value:
        genre = key

for choice in choice_filtering:
    if choice[1] == genre:
        user_movie.append([choice[0],10])
        
user_movie

#영화 데이터 불러오고 칼럼 분류
data = pd.read_csv('./final_data.csv',encoding='cp949')

data = data[['movie_id','user_id','movie_title','rating','genre']]


# 데이터 프레임 장르 필터링
data_genre = data['genre'] ==f'{genre}'
data = data[data_genre]

#데이터 프레임 피봇테이블로 변경
user_score = data.pivot_table(index=['user_id'],columns=['movie_title'],values='rating')
# user_score.head()
# nan값 처리 후 corr 상관분석
user_scores = user_score.fillna(0)
user_scores = user_scores.replace(np.nan,0)
user_scores.head(10)
course_similarity_df = user_scores.corr(method='pearson')
course_similarity_df.head(10)

def get_similar_courses(course_name,user_score):
    similar_score = course_similarity_df[course_name] * (user_score - 2.5)
    similar_score = similar_score.sort_values(ascending=False)
    
    return similar_score

# print(get_similar_courses('127 시간',9))/

similar_scores = pd.DataFrame()

# 유저가 선택한 영화로 영화추천
for course,score in user_movie:
    similar_scores = similar_scores.append(get_similar_courses(course,score),ignore_index=True)
    
similar_scores.head()

#결과값 리스트로 추출
result = similar_scores.sum().sort_values(ascending=False).head(10+len(user_movie))
result = list(result.index)
result = result[len(user_movie):]

print(result)
