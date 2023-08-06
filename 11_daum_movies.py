import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)    
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        #print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
        
        print(image_url)
        image_res = requests.get(image_url) # requests.get(): 함수는 웹 페이지 또는 파일을 요청하여 그 결과를 응답 객체로 반환합니다. 응답 객체에는 다운로드한 데이터가 content 속성에 바이너리 형태로 저장되어 있습니다., 
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f: # movie...jpg 경로에서 f파일 변수를 사용해서 wb(w:파일을 쓰기 모드로 열기를 의미, b: 파일을 이진(binary) 모드로 열기를 의미, -> 파일을 바이너리 쓰기모드로 열기) 모드를 사용
            f.write(image_res.content) # image_res.content는 실제로 다운로드한 이미지의 바이너리 데이터를 가리킵니다.

        if idx >= 4: # 상위 5개 이미지까지만 다운로드
            break

        #이 코드에서 바이너리 데이터를 쓰는 이유는 웹 페이지에서 이미지 데이터를 다운로드하여 파일로 저장하기 위해서다. 그래서 with open 함수를 사용한 것이다.