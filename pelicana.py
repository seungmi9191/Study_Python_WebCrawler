import requests
from bs4 import BeautifulSoup
from itertools import count


#http://pelicana.co.kr/store/stroe_search.html?page=1&branch_name=&gu=&si=
def pelicanaStore() :

    pStoreList = []

    for page in range(1, 117) : #(start=1) :

        url = "http://pelicana.co.kr/store/stroe_search.html?page=%s" %page
        html = requests.get(url).content

        soup = BeautifulSoup(html, "html.parser")  # 컨트롤 할 수 있는 html

        table = soup.find("table", {"class" : "table mt20"})

        table_tbody = table.find("tbody") #긁어올 규칙의 태그가 없으면 안써도 됨

        tr_tags = table_tbody.find_all("tr")

        for tr_tag in tr_tags :
            storeData = list(tr_tag.strings) #tr안에 있는 string을 다 빼줌
            name = storeData[1]
            tel = storeData[5].strip()
            address = storeData[3]

            print(name, tel, address)
            pStoreList.append([name,tel,address])

    return pStoreList

result = pelicanaStore()
print(result)

