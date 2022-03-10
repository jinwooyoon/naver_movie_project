#%%
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

#%%
data = pd.read_csv('./real_data22222.csv',encoding='cp949')

#%%
data

#%%

data['user_id'].unique()
#%%
data.drop('Unnamed: 0',axis=1,inplace=True)
#%%
data
# %%
ratings_matrix = data.pivot_table('reple_score',index='user_id',columns='movie_title')

# %%
ratings_matrix = ratings_matrix.fillna(0)
# %%
ratings_matrix
# %%
R = np.array(ratings_matrix)
# %%
S = cosine_similarity(R.T)
#%%

S

# %%
np.round(S,3)
# %%
user_id = 17
top_n = 30
movie_n = 10

seen_idx = np.where(R[user_id,:]>0)[0]
unseen_idx = np.where(R[user_id,:]<=0)[0]

pred_R = []

for unseen in unseen_idx:
    top_idx = np.argsort(S[unseen,seen_idx][::-1][:top_n])
    
    iS = S[unseen,seen_idx][top_idx]
    iR = R[user_id,seen_idx][top_idx]
     
    sumS = np.abs(iS).sum()
    
    if sumS == 0:
        pred_R.append(0)
    else:
        pred_R.append(np.dot(iS,iR)/sumS)
        
    
#%%

seen_idx
#%%
items = list(ratings_matrix.columns)
#%%
items.sort(revesed=True)
#%%
unseen_idx


#%%

print(pred_R.sort(reverse=True))
#%%
items
#%%
print('\n영화 추천 목록 :User ={}'.format(user_id))
print('---{:s} {:s}'.format('-'*35,'-'*15))
print('No {:35s} {:s}'.format('Title','expected rating'))
print('---{:s}{:s}'.format('-'*35,'-'*15))
for i ,p in enumerate(pred_sort_index):
    
