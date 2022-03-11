#%%
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from collections import Counter


#%%

choice_filtering = [['울지마 톤즈','다큐멘터리'],['폴란드로 간 아이들','다큐멘터리'],['다크나이트','바2보']]

genre_filter = []

for genre in choice_filtering:
    genre_filter.append(genre[1])

genre_filter = Counter(genre_filter)

max_value = max(list(genre_filter.values()))


genre = None
user_movie = []
for key in list(genre_filter.keys()):
    if max_value == 1:
        genre = key
        break
    if genre_filter[key] == max_value:
        genre = key

for choice in choice_filtering:
    if choice[1] == genre:
        user_movie.append([choice[0],10])


#%%
user_movie
 # %%
data = pd.read_csv('./final_data.csv',encoding='cp949')

#%%

data = data[['movie_id','user_id','movie_title','rating','genre']]

data

#%%

data_genre = data['genre'] ==f'{genre}'
data = data[data_genre]
data

# %%
user_score = data.pivot_table(index=['user_id'],columns=['movie_title'],values='rating')
# %%
user_score.head()
# %%
user_scores = user_score.fillna(0)
user_scores = user_scores.replace(np.nan,0)
user_scores.head(10)
# %%
course_similarity_df = user_scores.corr(method='pearson')
course_similarity_df.head(10)

# %%
def get_similar_courses(course_name,user_score):
    similar_score = course_similarity_df[course_name] * (user_score - 2.5)
    similar_score = similar_score.sort_values(ascending=False)
    
    return similar_score

# print(get_similar_courses('127 시간',9))/

similar_scores = pd.DataFrame()

for course,score in user_movie:
    similar_scores = similar_scores.append(get_similar_courses(course,score),ignore_index=True)
    
similar_scores.head()
# %%
result = similar_scores.sum().sort_values(ascending=False).head(10)

result = list(result.index)

# %%
result
# %%
