#%%
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from collections import Counter


#%%
#유저가 선택한 영화제목 + 장르 3개 저장

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

user_movie
#%%
user_movie = [[82540,10],[10072,10],[10561,10]]
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

#영화 데이터 불러오고 칼럼 분류
data = pd.read_csv('./final_data.csv',encoding='cp949')


#%%
data = data[['movie_id','user_id','movie_title','rating','genre']]


#%%
data

#%%


# 데이터 프레임 장르 필터링
data_genre = data['genre'] == genre
data = data[data_genre]

#%%
data

#%%
#데이터 프레임 피봇테이블로 변경
user_score = data.pivot_table(index=['user_id'],columns=['movie_title'],values='rating')


user_score


#%%
# user_score.head()
# nan값 처리 후 corr 상관분석
user_scores = user_score.fillna(0)
user_scores = user_scores.replace(np.nan,0)


#%%


user_scores



#%%
course_similarity_df = user_scores.corr(method='pearson')

course_similarity_df

#%%

user_scores


# course_similarity_df.to_csv(r'C:\Users\say_s\Desktop\naver_movie_project\비교\비교4.csv',encoding='cp949')
#%%
#%%

bb = pd.read_csv('./gaha.csv',encoding='cp949')

bb
#%%
test1 = bb['21 그램'].mean()

test2 = bb['21 그램'].mean()


#%%

test1 = bb['21 그램'] - test1
test1
#%%

test2 = bb['21 그램'] - test2
test2

#%%

test3 = np.sum(test1 * test2)

test3
#%%
test3 / np.sqrt(np.sum(test1 **2) * np.sum(test2 **2))


#%%

s1_c = data['영화1'] - data['영화1'].mean()
s2_c = data['영화2'] - data['영화2'].mean()


pearson_result = np.sum(s1_c *s2_c) /np.sqrt(np.sum(s1_c**2) * np.sum(s2_c **2))



#%%


# course_similarity_df.to_csv('./test.set.csv',encoding='cp949')



#%%

# course_similarity_df['13층']


#%%

def get_similar_courses(course_name,user_score):
    similar_score = course_similarity_df[course_name] * (user_score)
    similar_score = similar_score.sort_values(ascending=False)

    return similar_score


#%%
# print(get_similar_courses('127 시간',9))/

similar_scores = pd.DataFrame()


#%%
# 유저가 선택한 영화로 영화추천
for course,score in user_movie:
    similar_scores = similar_scores.append(get_similar_courses(course,score),ignore_index=True)
    
similar_scores.head()


#%%

similar_scores.to_csv(r'C:\Users\say_s\Desktop\naver_movie_project\비교\비교3.csv',encoding='cp949')

#%%
#결과값 리스트로 추출
result = similar_scores.sum().sort_values(ascending=False).head(13)

result = list(result.index)
result = result[3:]

print(result)
# %%
