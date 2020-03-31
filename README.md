## 뽐뿌 커뮤니티 크롤러
뽐뿌 커뮤니티 크롤러는 검색창에 자신이원하는 쿼리를 검색후 나오는 결과를 수집하는 크롤러입니다 <br><br>
자신이 원하는 쿼리(검색창)을 입력후 나오는 게시글을 수집합니다 <br><br>
크롤링한 사이트 주소:
http://www.ppomppu.co.kr/search_bbs.php

### 설치
Python 3 버젼으로 구축되어있습니다. 파이썬 기본환경을 세팅해 주십시오.<br><br>
download zip 혹은 git clone을 사용해 해당 파일을 다운로드 해주십시오.
```
$git clone https://github.com/ck992/pommpu_crawler.git
```

### 실행
Pomp_delay.py 파일을 열어 자신이 원하는 키워드와 해당 파일이 저장될 경로를 표시해 줍니다
```
    def run(self):
        self.setEnv()

        keyword = ""
        endYear = 
        endMonth = 
        endDay = 

        endDate = int(str(endYear) + str(endMonth).zfill(2) + str(endDay).zfill(2))

        result = self.getSearchingItems(keyword, endDate)

        DB = pd.DataFrame(result)
        DB.to_csv('result.csv')
```


## Contact
작동에 문제가 생기시거나 궁금한점이 있으시면 연락주시면 감사하겠습니다 [https://ck992.github.io/](https://ck992.github.io/).
