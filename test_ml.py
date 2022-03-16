#%%
import pandas as pd

from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from collections import Counter

data = pd.read_csv('./final_data.csv',encoding='cp949')
# %%
data
# %%

choice_filtering = [['대부 3','범죄'],['신세계','범죄'],['대부 2','범죄']]

genre_filter = []

genre = None

user_movie = []

#장르로 필터링 하기위해 중복된 장르 선택

for genre in choice_filtering:

    genre_filter.append(genre[1])
    
genre_filter = Counter(genre_filter)

max_value = max(list(genre_filter.values()))

#%%

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

#%%
# 데이터 프레임 장르 필터링


#%%

#영화 데이터 불러오고 칼럼 분류

data = data[['movie_id','user_id','movie_title','rating','genre']]


data_genre = data['genre'] ==f'{genre}'
data = data[data_genre]

# %%
data
# %%
movie_usr_rating = data.pivot_table('rating',index='movie_title',columns='user_id')

movie_usr_rating

# %%
usr_movie_rating = data.pivot_table('rating',index='user_id',columns='movie_title')
# %%
movie_usr_rating.fillna(0,inplace=True)
movie_usr_rating
# %%
similarity_rate = cosine_similarity(movie_usr_rating,movie_usr_rating)
#%%
similarity_rate




#%%




# %%
similarity_rate_df = pd.DataFrame(data=similarity_rate,index=movie_usr_rating.index,columns=movie_usr_rating.index)

#%%
similarity_rate_df


#%%

def get_similar_courses(course_name,user_score):
    similar_score = similarity_rate_df[course_name] * (user_score)
    similar_score = similar_score.sort_values(ascending=False)
    
    return similar_score


similar_scores = pd.DataFrame()

# 유저가 선택한 영화로 영화추천
for course,score in user_movie:
    similar_scores = similar_scores.append(get_similar_courses(course,score),ignore_index=True)
    
similar_scores.head()


#%%
similar_scores




#%%

result = similar_scores.sum().sort_values(ascending=False).head(10+len(user_movie))


#%%

result
# %%
# def recommend_movie(title):
#     return similarity_rate_df[title].sort_values(ascending=False)[:6]

# recommend_movie('악마는 사라지지 않는다')
# %%
