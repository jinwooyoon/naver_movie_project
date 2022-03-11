#%%
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from collections import Counter


#%%

choice_filtering = [['신세계','애니메이션'],['알라딘','범죄'],['다크나이트','범죄']]

genre_filter = []

for genre in choice_filtering:
    genre_filter.append(genre[1])

a = Counter(genre_filter)

print(a)


user_movie = []


#%%
for i,item in enumerate(choice_filtering):
    if choice_filtering[0][1] == item[1]:
        user_movie.append(item)




#%%

user_movie

 # %%
data = pd.read_csv('./final_data.csv',encoding='cp949')

#%%

data = data[['movie_id','user_id','movie_title','rating','genre']]





#%%


# data_genre = (data.genre =='드라마') | (data.genre =='애니메이션')


#%%

data_genre = data['genre'] =='범죄'
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


user_choice = [("신세계",10),("범죄와의 전쟁 : 나쁜놈들 전성시대",10),("대부",10)]
for course,score in user_choice:
    similar_scores = similar_scores.append(get_similar_courses(course,score),ignore_index=True)
    
similar_scores.head()
# %%
similar_scores.sum().sort_values(ascending=False).head(10)
# %%
