from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Okt
from matplotlib import pyplot as plt
import pandas as pd
import operator
import numpy as np

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
        
        
def color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return("hsl({:d},{:d}%, {:d}%)".format(np.random.randint(200,240), np.random.randint(80,100), np.random.randint(70,90)))
        
wordcloud = WordCloud(font_path = r'C:\Users\say_s\AppData\Local\Microsoft\Windows\Fonts\SB 어그로 B.ttf', background_color='black', colormap = "Accent_r", width=1000, height=800, max_words=50, min_font_size=20, color_func=color_func).generate_from_frequencies(c)
plt.imshow(wordcloud) 
plt.axis('off') 
plt.show()


