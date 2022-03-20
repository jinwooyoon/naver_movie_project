#%%
import pandas as pd
import numpy as np
from tqdm import tqdm

#%%
data = pd.read_csv('important_data.csv',encoding='cp949')

data['user_name'].unique()
# %%
data = data[['id','title','user_name','reple_score']]

# %%
new = data['user_name'].value_counts()

new = new.to_frame()
#%%
new.reset_index(drop=False,inplace=True)

new.rename(columns={'index':'user_name','user_name':'frequency'},inplace=True)

# %%
new2 = new[new['frequency']>60]


new3 = new[new['frequency']<3]

new3
# %%
user_list1 =list(new2['user_name'].unique())
user_list2 =list(new3['user_name'].unique())