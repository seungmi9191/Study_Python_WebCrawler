import requests
from bs4 import BeautifulSoup

def naver_movie() :

    url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    html = requests.get(url).text #요청 온 것 중에 텍스트만 달라고 하기

    soup =  BeautifulSoup(html, "html.parser") #컨트롤 할 수 있는 html
    tags = soup.find_all("div", {"class" : "tit3"}) #태그가 td인 아이 찾아오기

    for index, tag in enumerate(tags) :
        #태그 제외한 글씨만 보이기
        tag.a.get_text() #태그의 a태그의 텍스트를 가져와, #tag.a.text로 써도 됨

        print(index+1 , tag.a.get_text())


naver_movie()