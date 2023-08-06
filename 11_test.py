import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

for page in range(1,3):
    url = "https://www.musinsa.com/search/musinsa/goods?q=%EB%B0%98%ED%8C%94&list_kind=small&sortCode=sale_high&sub_sort=1w&page={}&display_cnt=0&saleGoods=false&includeSoldOut=false&setupGoods=false&popular=false&category1DepthCode=&category2DepthCodes=&category3DepthCodes=&selectedFilters=%EC%8B%9C%EC%A6%8C%EC%98%A4%ED%94%84%3AsaleCampaignFilter%3AsaleCampaignFilter&category1DepthName=&category2DepthName=&brandIds=&price=&colorCodes=&contentType=&styleTypes=&includeKeywords=&excludeKeywords=&originalYn=N&tags=&campaignId=seasonoff_23ss&serviceType=&eventType=&type=&season=&measure=&openFilterLayout=N&selectedOrderMeasure=&shoeSizeOption=&groupSale=false&d_cat_cd=&attribute=&plusDeliveryYn=".format(page)
    res = requests.get(url,headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    images = soup.find_all("img", attrs={"class":"lazyload lazy"})

    for idx, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//"):
          image_url = "https:" + image_url
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("shirt_{}page_{}.jpg".format(page, idx+1), "wb") as f:
          f.write(image_res.content)

        if idx >= 4:
          break



        # error : 이미지가 안나옴!!