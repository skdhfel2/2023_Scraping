import csv
import requests
from bs4 import BeautifulSoup



filename = "KBO리그 기록 및 순위.csv"
f = open(filename, "w", encoding = "utf-8-sig", newline = "")
writer = csv.writer(f)

title = "년도 순위 팀  경기수 승 패 무 승률 게임차 연속 출루율 장타율 최근 10경기".split("\t")
print(type(title))
writer.writerow(title)

for year in range(2020,2024):
    url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year={}".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"cellpadding" :"0"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        data =[column.get_text().strip() for column in columns]        
        writer.writerow(data)



