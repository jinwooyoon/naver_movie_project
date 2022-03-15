#%%
from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Okt
from matplotlib import pyplot as plt
import pandas as pd
import operator
#%%

del_word = ['영화','정말','우리','진짜','지금','대해','보고','놀란','한번']

df = pd.read_csv('./wordcloud.csv',encoding='cp949')

df = df[df['id'] == 24452] #여기에 영화 id를 넣어주세요.

text = df['text'].tolist()

text = [x for x in text if pd.isnull(x) == False]

text = "".join(str(_)for _ in text)

okt = Okt()
nouns = okt.nouns(text) # 명사만 추출

words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외

c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함  

for key in list(c.keys()):
    if c[key] <10:
        del c[key]  

for word in del_word:
    if word in c.keys():
        del c[word]
        
        
wordcloud = WordCloud(font_path = 'HMFMPYUN', width=400, height=400, scale=2.0, max_font_size=250).generate_from_frequencies(c)
plt.imshow(wordcloud) 
plt.axis('off') 
plt.show()


# %%
