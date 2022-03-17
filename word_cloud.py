
from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Okt
from matplotlib import pyplot as plt
import pandas as pd
import operator
import numpy as np

#제외할 단어
del_word = ['영화','정말','우리','진짜','지금','대해','보고','놀란','한번']

#데이터 불러오기

df = pd.read_csv('./wordcloud.csv',encoding='cp949')


# 영화 id에 맞는 데이터가 들어옴
df = df[df['id'] == 213746] #여기에 영화 id를 넣어주세요.

# text 칼럼 데이터만 추출
text = df['text'].tolist()

# null 값 제외하고 list로 변환
text = [x for x in text if pd.isnull(x) == False]

# text 리스트에 있는 데이터를 str로 변경 
text = "".join(str(_)for _ in text)

# Okt 를 사용하여 text에 있는 데이터 명사만 추출
okt = Okt()
nouns = okt.nouns(text) # 명사만 추출


# 단어의 길이가 1개인 것은 제외
words = [n for n in nouns if len(n) > 1]

 # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함  
result = Counter(words) 

# 단어의 빈도가 10개 이하인것을 없앰
for key in list(result.keys()):
    if result[key] <10:
        del result[key]


# del_word 변수에 있는 단어들이 있을 시 없앰

for word in del_word:
    if word in result.keys():
        del result[word]


# 결과 추출

def color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl({:d},{:d}%, {:d}%)".format(np.random.randint(200,240), np.random.randint(80,100), np.random.randint(70,90)))
        
wordcloud = WordCloud(font_path = r'C:\Users\say_s\AppData\Local\Microsoft\Windows\Fonts\SB 어그로 B.ttf', background_color='black', colormap = "Accent_r", width=1000, height=800, max_words=50, min_font_size=20, color_func=color_func).generate_from_frequencies(result)
plt.imshow(wordcloud)
plt.axis('off') 
plt.show()
# %%
