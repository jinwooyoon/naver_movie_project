#%%
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# %%
data = pd.read_csv('./real_data22222.csv',encoding='cp949')

#%%

data

#%%

len(data['user_name'].unique())
# %%
user_score = data.pivot_table(index=['user_id'],columns=['movie_title'],values='reple_score')
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

print(get_similar_courses('127 시간',9))
# %%
haha = [("범죄도시",10),("신세계",10),("살인의 추억",10)]
similar_scores = pd.DataFrame()

for course,score in haha:
    similar_scores = similar_scores.append(get_similar_courses(course,score),ignore_index=True)
    
similar_scores.head()
# %%
similar_scores.sum().sort_values(ascending=False)[:10]
# %%
