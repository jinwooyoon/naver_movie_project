
from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm
import logging
from selenium import webdriver



Df_list = []


for i in tqdm(range(1,41)):
    url = f'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20220207&page={i}'
    req = requests.get(url)
    
    if req.ok:
        html = req.text
        soup = BeautifulSoup(html,'html.parser')


    a = soup.find_all('tr')



    for i in range(57):
        if 'None' == str(a[i].find('a')):
            pass
        
        else:
            item = str(a[i].find('a')).split('"')
            id = item[1].split('=')[1]
            title = item[3]
            url = 'https://movie.naver.com'+item[1]
            
            Df_list.append([id,title,url])

    Df_movie = pd.DataFrame(Df_list,columns=['Id','Title','Url'])
    

#%%

#Url만 가지고 오기
Df_url = Df_movie['Url']
test_list = []


for i in tqdm(Df_url):
    req = requests.get(i)
    if req.ok:
        html = req.text
        soup = BeautifulSoup(html,'html.parser')


    #관람객 평점

    try:
        spectator_grade = soup.select_one('#actualPointPersentBasic > div > span').text[-6:-1]
        spectator_grade =float(spectator_grade)
        

        
    except:
        spectator_grade = '데이터 없음'

    
    #네티즌 평점
    try:
    
        netizen_grade = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > div.main_score > div.score.score_left > div.star_score')
        netizen_grade = float(netizen_grade.text.replace('\n',''))
    except:
        netizen_grade = '데이터 없음'

    #썸네일 사진
    try:
        images = soup.select_one('#content > div.article > div.mv_info_area > div.poster > a')
                        
        images=str(images).split('src=')[2].split('"')[1]
    except:
        images = '데이터 없음'
    
    # 기자 평점
    try:
        reporter_grade = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > div.main_score > div:nth-child(2) > div > a > div')
        reporter_grade =float(reporter_grade.text.replace('\n',''))

    except:
        reporter_grade = '데이터 없음'    
    

    # 장르
    try:   
    
        genre = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a').text
    except:
        genre = '데이터 없음'
        

    #국가
    try:
    
        country = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2) > a').text
    except:
        country = '데이터 없음'
    
    #런타임
    try:
        runtime = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)').text.replace(' ','')
    #개봉일
    except:
        runtime = '데이터 없음'


    try:
        release = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4)').text[1:13].replace('\n','')
    except:
        release = '데이터 없음'

    #감독
    try:
        director = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a').text
        
    except:
        director = '데이터 없음'
    
    
    #배우
    
    try:
        actor = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p').text
        if '\t' in actor:
            actor = '데이터 없음'
    except:
        actor = '데이터 없음'
    
    # 연령제한
    try:
        age = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(8) > p > a:nth-child(1)').text
    except:
        age = '전체관람가'
    
    # 줄거리
    try:
        summary = soup.select_one('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p')
        summary = summary.text.replace('\r','').replace('\xa0','').replace('\xa1','')
    except:
        
        summary = '데이터 없음'

    try:            
        age_search = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > div.viewing_graph > div > div.bar_graph').text
        age_list = age_search.replace('\n','').split('대')[:5]
        age_10 = age_list[0][:-2]
        age_20 = age_list[1][:-2]
        age_30 = age_list[2][:-2]
        age_40 = age_list[3][:-2]
        age_50 = age_list[4][:-2]
        
    except:
        age_10 = '데이터 없음'
        age_20 = '데이터 없음'
        age_30 = '데이터 없음'
        age_40 = '데이터 없음'
        age_50 = '데이터 없음'

    test_list.append([spectator_grade,netizen_grade,images,reporter_grade,genre,country,runtime,release,director,actor,age,summary,age_10,age_20,age_30,age_40,age_50])

test_list_df = pd.DataFrame(test_list,columns=['spectator','netizen','thumbnail','reporter','genre','country','rumtime','release','director','actor','age','summary','age_10','age20','age30','age40','age50'])


#%%

# Id값으로 데이터프레임 merge

test_list_df['Id'] = Df_movie['Id']
result = pd.merge(Df_movie,test_list_df,on='Id')
result.to_csv('./result3.csv',encoding='utf-8-sig',index=False)


#%%

# 셀레니움이 필요한 데이터 (크롤링 시간이 너무 오래 걸려서 따로 분류해놓음.)

gender_ratio = []

for i in tqdm(Df_url):
    chromedriver = './chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    driver.get(f'{i}')
    try:
        man = driver.find_element_by_css_selector('#actualGenderGraph > svg > text:nth-child(4) > tspan').text
        woman = driver.find_element_by_css_selector('#actualGenderGraph > svg > text:nth-child(6) > tspan').text

    except:
        man = '데이터 없음'
        woman = '데이터 없음'
        
    gender_ratio.append([man,woman])