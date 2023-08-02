import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

for i in range(1, 10):

  url = "https://www.musinsa.com/search/musinsa/goods?q=%EB%B0%98%ED%8C%94%EB%8B%88%ED%8A%B8&list_kind=small&sortCode=pop&sub_sort=&page={}&display_cnt=0&saleGoods=&includeSoldOut=&setupGoods=&popular=&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&campaignId=&serviceType=&eventType=&type=&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&shoeSizeOption=&groupSale=&d_cat_cd=&attribute=&plusDeliveryYn=".format(i)

  res = requests.get(url, headers=headers)
  res.raise_for_status()
  soup = BeautifulSoup(res.text, "lxml")

  items = soup.find_all("li", attrs = {"class" :re.compile ("^li_box")})

  for item in items:

    # 성별
    gender = item.find("li", attrs ={"class" : "icon_man sight_out"})
    if gender:
      gender = gender.get_text().strip()
    else:
      continue

  # 상품 이름
    name = item.find("p", attrs = {"class" : "list_info"}).get_text().strip()

    # 가격
    price = item.find("p", attrs = {"class" : "price"}).get_text().strip()

    #리뷰 
    rate = item.find("p", attrs ={"class" : "point"})

    if rate:
      rate = rate.get_text().strip()
      rate = float(rate.replace("," , ""))  
    else:
      continue

    rate_cnt = item.find("span", attrs ={"class" : "count"})
    if rate_cnt:
      rate_cnt = rate_cnt.get_text().strip()
      rate_cnt = int(rate_cnt.replace("," , ""))  

    else:
      continue

    

    link = item.find("a", attrs ={"name" : "goods_link"})["href"]

    if rate >= 4.5 and rate_cnt <= 10:
      
        print(f"제품명 :{name}",end =" | ")
        print(f"가격 : {price}",end =" | ")
        print(f"평점 : {rate}점 ({rate_cnt}개)",end =" | ")
        print(f"성별 : {gender}",end =" | ")
        print(f"바로가기 :{link}")
        print("_" * 100)





