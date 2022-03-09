#%%
import pandas as pd


#%%
data = pd.read_csv('./data_result.csv',encoding='utf-8')


#%%

data2  = pd.read_csv('./dabinnim.csv',encoding='cp949')
data2
#%%
data2 = data2['title']
# %%
data_list = data['user_name'].unique()
# %%
data_list = list(data_list)

#%%

data_list

#%%

data['title'] = data2
#%%

data
#%%

data_add = []
for i in range(len(data['user_name'])):
    data_add.append(i+1)
    
    


# %%

data['user_id'] = data_add
#%%

data
# %%
data.drop('user_name',axis=1,inplace=True)
# %%
data = data[['user_id','id','title','reple_score']]
# %%
data.to_csv('./test_data.csv',encoding='utf-8',index=None)
# %%
