#%%
import pandas as pd


#%%
data = pd.read_csv('important_data.csv',encoding='cp949')

#%%

data
#%%

data2 = pd.read_csv('important_data.csv',encoding='cp949')

data2


# %%
data.drop('user_id',axis=1,inplace=True)
# %%

data_name = list(data['user_name'].unique())

#%%


for i,name in enumerate(data_name):
    data[data['user_name'] == f'{name}'] = i+1


#%%

user_name = data['user_name']
#%%

data2.drop('user_name',axis=1,inplace=True)
#%%

data2['user_id'] = user_name
#%%

data2.rename(columns={'id':'movie_id','title':'movie_title'},inplace=True)
#%%

data2
#%%

data2 = data2[['user_id','user_name','movie_id','movie_title','reple_score']]
#%%
data2
#%%

data2.to_csv('./real_data22222.csv',encoding='cp949',index=False)
#%%
data_name.to_csv('./name_list.csv',encoding='cp949')
# %%
data[data['user_name']=='꾸믈꾸어(yoon****)'] = 1

# %%
data['user_name'].value_counts()
# %%

import pandas as pd

data1 = pd.read_csv('./real_data22222.csv',encoding='cp949')


# %%
data2 = pd.read_csv('project_data/result_data.csv',encoding='utf-8')
# %%
data1
# %%
data2
# %%

data1 = data1.values.tolist()
data2 = data2.values.tolist()
#%%
data2

#%%
new_data = []

for i in data1:
    for j in data2:
        if i[0] == j[0]:
            

# %%

for i,item in enumerate(data1):
    for j in data2:
        if item[0] ==j[0]:
            for k in j:
                data1[i].append(k)

#%%


# %%

result = pd.DataFrame(data1)

#%%

res
#%%
result.to_csv('./real_dataee321421e.csv',encoding='utf-8')
# %%
