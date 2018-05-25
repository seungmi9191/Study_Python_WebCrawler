import time
from selenium import webdriver
from bs4 import BeautifulSoup
from itertools import count
import pandas as ps

def goobneStore() :

    goobneStoreList = []

    wd = webdriver.Chrome("/usr/local/bin/chromedriver")
    wd.get("https://www.goobne.co.kr/store/search_store.jsp")

    #page = 15

    for page in range(47,49) :#count(start=48) :
        wd.execute_script("store.getList(%s)" % page)
        time.sleep(5) #브라우저 충분히 열린 시간 줘서 잘 읽히도록~
        html = wd.page_source
        soup = BeautifulSoup(html, "html.parser")

        tbody_tag = soup.find("tbody", {"id" : "store_list"})
        tr_tags = tbody_tag.find_all("tr")

        #<tr class>가 없으면 비정상, 있으면 정상
        if tr_tags[0].get("class") is None :
            break

        for tr_tag in tr_tags :
            stringList = list(tr_tag.strings)
            name = stringList[1]
            tel = stringList[3]
            address = stringList[5] if stringList[3] ==' ' else stringList[6] #if문 [3]의 컬럼 내용이 없을 때 [5]를 넣고 else면 [6]

            goobneStoreList.append([name, tel, address])

            print(stringList)

    wd.quit() #브라우저 강제로 닫음

     # 파일저장
    table = ps.DataFrame(goobneStoreList, columns=["name", "tel", "address"])
    table.to_csv("/Users/WOOSEUNGMI/Desktop/2018/javaStudy/webdata/goobne_table.csv", encoding="utf-8-sig", mode="w", index=True)

    return goobneStoreList

result = goobneStore()
print(result)