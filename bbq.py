import requests
from bs4 import BeautifulSoup
from itertools import count
import pandas as ps

#ajax --> url을 알아내야함

def bbqStore() :

    bbqStoreList = []

    #page = 1
    for page in count(start=1): #range(140,149) #count는 시작점만 정해주고 계속 무한
        url = "http://changup.bbq.co.kr/findstore/findstore_ajax.asp?page=%s" %page

        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        tbody_tag = soup.find("tbody")
        tr_tags = tbody_tag.find_all("tr")

        print(tr_tags)

        if len(tr_tags) <= 1 :
            break

        for i, tr_tag in enumerate(tr_tags) :

            if i != 0 :
                stringList = list(tr_tag.strings)

                name = stringList[1]
                tel = stringList[5]
                address = stringList[3]

                #print(name,tel,address)

                bbqStoreList.append([name, tel, address])

    #파일저장
    table = ps.DataFrame(bbqStoreList, columns=["name", "tel", "address"])
    table.to_csv("/Users/WOOSEUNGMI/Desktop/2018/javaStudy/webdata/bbq_table.csv", encoding="utf-8-sig", mode="w", index=True)


    return bbqStoreList

result = bbqStore()
print(result)