import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") #newline ="" : 줄바꿈 못하게 만듦, 이 코드는 파일을 어떻게 열것인가 설정하는 코드다
writer = csv.writer(f) # csv 모듈은 CSV 파일을 읽고 쓰기 위한 기능을 제공합니다

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# ["N", "종목명", "현재가", ...]
print(type(title)) # list
writer.writerow(title) # writerow 함수는 CSV 파일에 한 줄(하나의 행)을 작성하는데 사용되며, 리스트나 튜플 형태의 데이터를 받아 해당 데이터를 CSV 파일에 쓰게 됩니다.

for page in range(1, 5):
    res = requests.get(url + str(page)) #str쓰는 이유: url이 문자열이라 +로 더해줄려면 page도 문자열이 되야하므로 변환해준거다
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns] # columns를 column에 넣고 그 column을 가져와서 data에 넣는다
        #print(data)
        writer.writerow(data)
