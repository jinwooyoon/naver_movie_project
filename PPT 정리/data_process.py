import pandas as pd
import numpy as np
from tqdm import tqdm

# 데이터 빈도수 가공 코드
data = pd.read_csv('comment_reply.csv',encoding='cp949')

data = data[['id','title','user_name','reple_score']]

new = data['user_name'].value_counts()

new = new.to_frame()

new.reset_index(drop=False,inplace=True)

new.rename(columns={'index':'user_name','user_name':'frequency'},inplace=True)

new2 = new[new['frequency']>60]

new3 = new[new['frequency']<3]

user_list1 =list(new2['user_name'].unique())
user_list2 =list(new3['user_name'].unique())

for i in tqdm(user_list1):
    del_data = data[data['user_name'] == f'{i}'].index
    data.drop(del_data,inplace=True)

for i in tqdm(user_list2):
    del_data = data[data['user_name'] == f'{i}'].index
    data.drop(del_data,inplace=True)
    
    
# user_name 고유번호로 변겅
data = pd.read_csv('./important_data.csv',encoding='cp949')

data_name = list(data['user_name'].unique())

data_id = data['user_name']

for i,name in tqdm(enumerate(data_name)):
    data['user_name'] = data['user_name'].replace(f'{name}',f'{i+1}')

all_data = pd.read_csv('./result_data.csv',encoding='utf-8')

data.rename(columns={'id':'movie_id'},inplace=True)

all_data = all_data[['movie_id','genre']]

result_data  = pd.merge(data,all_data,on='movie_id')

# genre 고유번호로 변경

genre_number = pd.read_csv('./genre_number_result.csv',encoding='cp949')

genre_name = list(genre_number['genre'].unique())

for i,name in tqdm(enumerate(genre_name)):
    result_data['genre'] = result_data['genre'].replace(f'{name}',f'{i}')

result_data.to_csv('./final_data.csv',encoding='cp949')


