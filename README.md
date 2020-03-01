# python-scraper

python start

- [The Python Standard Library](https://docs.python.org/3/library/index.html)

# Object

- Python 기본 문법 익히기
- 크롤링을 통해 stack over flow 게시글 scrap 하기
- scrap한 데이터 엑셀에 옮기기

# History

#### 2020.02.03: #0-0 ~ #0-4

#### 2020.02.05: #1-0 ~ #1-3

#### 2020.02.06: #1-4 ~ #1-9

#### 2020.02.08: #1-10 ~ #1-12

#### 2020.02.09: #1-13 ~ #2-3

#### 2020.02.16: #2-4

#### 2020.02.19: #2-5 ~ #2-6

#### 2020.02.20: #2-7

#### 2020.02.23: #2-8

#### 2020.02.29: #2-9 ~ #2-14

# Concept

#### #0-0 ~ 0-4 Introduction

- repl.it을 통해 기본 문법 익히기

  - python으로 생성(python 2.7 아님)

---

#### #1 Theory

#### #1-0 Data Types of Python

- null, undefined 대신에 None을 씀
  - a_none = None 등으로 따옴표를 감싸지 않은 NoneType이 따로 있음
- Python 생태계에서는 변수명 표현을 snake 표현식을 주로 쓴다.
  - very_young_value
- print(type(변수))를 통해 데이터 타입을 얻을 수 있다.

  - int, float, str, NoneType, bool, List, tuple, dict

  ```python
    a = 1
    ab = 1.2
    b = "1"
    c = None
    d = False
    e = [1,2]
    f = (1,2)
    g = {"a":2}

    print(type(a))
    print(type(ab))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))
    print(type(g))

    ### 결과값 ###
    #<class 'int'>
    #<class 'float'>
    #<class 'str'>
    #<class 'NoneType'>
    #<class 'bool'>
    #<class 'list'>
    #<class 'tuple'>
    #<class 'dict'>
  ```

#### #1-1 Lists in Python

- sequence type: 열거형 타입 = List
  - list, tuple
- list
  - 대괄호로 정희
    - days = ["Mon","Tue","Wed]
  - common, mutable sequence operation 듣을 갖고 있음.
    - common: 일반적인 list data 조회, 길이, 포함여부 등
    - mutable: list data를 변경하는 연산
      - 값을 바꾸고 싶지 않다면 immutable sequence에 넣어야 함
- 변수 type 보는 법
  - print(type(변수)) 하면 해당 변수의 타입을 볼 수 있다.
- Python Document: The Python Standard Library
  - 여기서 Python들의 문법들을 확인할 수 있다.
- 참고 링크
  - [The Python Standard Library](https://docs.python.org/3/library/index.html)

#### #1-2 Tuples and Dicts

- tuple은 list와 달리 데이터 수정을 할 수 없음 = unmutable
  - 수정할 수 없는 sequence type을 만들고 싶을 때 사용한다.
  - tuple은 그래서 common operation만을 쓸 수 있다.
    - 데이터 포함 유무, 길이 등의 정보만 확인가능하다.
- 괄호로 정희
  - days = ("Mon","Tue","Wed)
- dictionary = dict type
  - key, value 형태로 다양한 type의 데이터를 한곳에 담는 데이터 타입
  - 중활호로 정의
    - bts = {"name": "bts", "age": 30, "korean": True, "fav_food": ["chicken", "water"]}
  - 추가 하고 싶은 데이터는 대활호를 통해 편하게 추가 가능
    - bts["fav_hobby"] = ["basketball", "play the guitar"]

#### #1-3 Built-in Functions

- Document에서 기본으로 제공하는 다양한 함수들을 볼 수 있다.
- 형 변환

  - str(), int() 등의 함수가 있어 바로 형 변환할 수 있다.

    ```python
      age = 18
      print(type(age))
      str_age = str(age)
      print(type(str_age))

      #<class 'int'>
      #<class 'str'>
    ```

#### #1-4 Creating a Your First Python Function

- def 으로 함수를 선언함(define)
  - def fn_name(parameter):
  - 별도의 중괄호{} 없이 들여쓰기를 하면 함수 내부로 인식

#### #1-5 Function Arguments

- parameter에 default 값을 줄 수 있음
  - def fn_name(str1="김치", str2="네번"):

#### #1-6 Returns

- function 내부에서 return을 하면 function은 즉시 종료

#### #1-7 ♡

- 강의 없음

#### #1-8 Keyworded Arguments

- 함수 파라미터 순서에 상관없이 변수명으로 입력할 수 있다.

  ```python
    def fn_name(parm1, parm2, parm3):
      return f"{parm1} < {parm2} < {parm3}"

    str = fn_name(parm3="20", parm1="10", parm2="15") # = fn_name("10", "20", "30"0)
    print(str)
  ```

- 문자열에 변수를 담을 때 문자열 앞에 f를 쓰고 변수명을 중괄호로 감싸면 된다.
  - f"{parm1} < {parm2} < {parm3}"

#### #1-9 Code Challenge!

#### #1-10 Conditionals part One

- if, else
  - Condition을 조건이라고 하나봄
  - if CONDITION: elif: else:
    - 위 처럼 조건에 콜론(:)을 쓰고 들여쓰기로 조건에 대한 실행 로직을 넣으면 됨
    - type을 체크할 때 'is'라는 비교문을 쓸 수 있다.
      - if type(b) is int
      - if type(b) is int or type(b) is float:
- 참고 링크
  - [Built-in Types](https://docs.python.org/3.7/library/stdtypes.html#truth-value-testing)

#### #1-11 if else and or

- Boolean Operation: and or not
- if CONDITION: elif CONDITION: else: 사용법
- is, is not, not, and, or

  ```python
    def age_check(age):
      print(f"you are {age}")
      if age < 18:
        print("you can't drink")
      elif age == 18:
        print("you are new to this!")
      else:
        print("enjoy your drink")

    age_check(18)
  ```

#### #1-12 for in

- for 변수명 in Sequence:

  - Sequence는 list, tuple 같은 다수의 데이터를 저장하고 있는 배열형 데이터
  - 이렇게 하고 변수명에는 아무거나 넣어줌
  - 순차적으로 Sequence 내부 데이터를 변수에 저장해서 순차적으로 뽑아 슬 수 있다.
  - break 로 반복문 종료 가능

  ```python
    days = ("Mon", "Tue", "Wed")
    for day in days:
      print(day)

    #Mon, Tue, Wed 출력
  ```

  - 흠 조건문에 type 측정에만 is를 쓰는줄 알았는데 단순 비교에도 is를 많이 쓰는듯
    - if day is "Wed": 등에 사용됨

- The for statement is used to iterate over the elements of a sequence (such as a string, tuple or list) or other iterable object:

  - 배열을 순차적으로 뽑아준다는 뜻.
  - str (String)로 배열이다.

- 참고 링크
  - [The for statement](https://docs.python.org/3.7/reference/compound_stmts.html#the-for-statement)

#### #1-13 Modules

- 기능의 집합같은 느낌. import해서 사용할 수 있음
- 다른 사람이 만든 모듈도 다운받아 import를 통해 쓸 수 있음
- 굉장히 다양한 모듈이 제공되고 있다.
- math

  - ceil 반올림, fabs 절대값

  ```python
    import math

    print(math.ceil(1.2))
    print(math.fabs(1.2))
  ```

  - math를 다 가져오는 것은 비효율적이기 때문에 필요한 것들만 가져올 수 있음

  ```python
    from math import ceil, fsum

    print(ceil(1.2))
    print(fsum([1, 2, 3, 4, 5, 6, 7]))
  ```

  - import하는 모듈의 이름도 재정의 해줄 수 있음
    - from math import ceil as my_ceil

- 파이썬 파일을 하나 생성해서 그 안에 선언하는 함수들을 모듈처럼 갖다 쓸 수 있음
  - test.py파일에 print_name(name)이라는 함수를 정의한 뒤 main.py 에서 import해서 쓸 수 있음
    - 이 때 from test import print_name 이렇게 .py 확장자와 함수 매개변수를 안써줘도 됨
- print() 함수는 인자를 무제한으로 받을 수 있다. 이것에 대해는 추후 강의한다.ㅌ
- 참고 링크
  - [Module Math](https://docs.python.org/3/library/math.html#module-math)

---

#### #2 Building a Job Scrapper

#### #2-0 What is Web Scrapping

- 웹사이트에서 필요한 정보만 추출하는 작업
  - 웹 url을 SNS에 공유 시 해당 웹페이지의 메인 사진과 제목을 가져오는 것과 같은 것
  - 여러 쇼핑몰 가격정보를 가져와 비교하는 것
- web mining, data mining 이라고도 불림 (mine, mining = 채굴)

#### #2-1 What are We Building

- 대형 구직 사이트인 Indeed, Stack Over Flow에서 python 개발자 공고글을 긁어 올 것임
- 페이지를 이동하면서 모든 데이터를 긁어오고 긁어온 데이터를 엑셀에 옮긴거임

#### #2-2 Navigating with Python

- python 내부 모듈도 훌륭하지만 외부 모듈을 통해 스크래핑을 효과적으로 더 강력하게 할 수 있다.
- repl.it 좌측 packages 버튼 클릭
  - requests 검색 > pyyhon HTTP for Humans. 패키지 클릭 > 추가
- url 모듈보다 request 모듈이 더 좋음. request는 python request들을 모아놓은 것
  - requests 모듈에대해 필요 시 검색해보는 것도 좋을듯
- import requests 하고 requests.get("URL")을 변수에 저장
  - text, header, json 등을 가져올 수 있다.
  - .text > html 전부를 가져온다
- beautiful soup library를 이용해서 html 정보를 효과적으로 추출한다.
  - package에서 beatifulsoup4 (다 붙여서 풀로 검색해야됨) 검색해서 추가
    - Screen-scraping library
- 참고 링크
  - [Requests 모듈](https://2.python-requests.org/en/master/)
  - [Requests 모듈 Github](https://github.com/psf/requests)
  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
  - [Beauriful Soup Doc](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

#### #2-3 Extracting Indeed Pages

- extracting : 추출
- a tag는 anchor(앵커)라 하나봄
- indeed 페이지 정보 추출하기
  - div.pagination에 페이징 정보가 들어있음
  - div 안에 a tag를 추출하고 거기에 span에 있는 숫자를 가져온다
  - span 마지막에는 Next(다음) 이라는 데이터가 있기 때문에 마지막 줄을 빼고 배열에 담아준다.
- 배열 spans = []

  - spans.append()로 데이터를 추가해준다
  - spans[0:5] 라고 하면 0부터 5번까지 데이터를 보여준다.
  - spans[0:-1], spans[:-1]라고 하면 마지막에서 첫번째 항을 제외하고 보여준다.
  - spans[-1] 이라고 하면 마지막에서 첫번째 항을 보여준다.
  - 마지막 항은 필요가 없으므로 spans = spans[:-1] 로 저장한다.

  ```python
    import requests
    from bs4 import BeautifulSoup

    indeed_resul = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&l=%ED%8C%90%EA%B5%90&limit=50")
    indeed_soup = BeautifulSoup(indeed_resul.text, "html.parser")

    pagination = indeed_soup.find("div", {"class":"pagination"})

    pages = pagination.find_all("a")
    spans = []
    for page in pages:
      spans.append(page.find("span"))

    spans = spans[:-1]

    print(spans)
  ```

#### #2-4 Extracting Indeed Pages part Two

- 복습
  - requests import
    - resul = requests.get("URL"): 해당 URL 페이지의 정보를 담는다.
    - resul.text: 해당 페이지의 text를 담는다.
  - beatifulSoup import
    - soup = BeautifulSoup(resul.text, "html.parser"): 해당 페이지 텍스트 정보에서 html 데이터를 효과적으로 불러올 수 있도록 담는다.
    - soup.find, find_all 등으로 html 데이터를 효과적으로 가져와 뿌린다.
  - 현재 Indeed 페이지의 페이지 넘버를 불러왔다.
- 목표
  - 페이지 번호만 뽑아서 숫자로바꾸고 최대 값을 뽑아 변수에 저장한다.
- page.find("span").string
  - span tag에서 String만 가져옴 > 페이지 번호만 가져옴
  - 해당 tag 안에 String이 단 하나만 있을 경우 .string을 통해 뽑아낼 수 있음
  - 이 때 string은 value 값 같음. 화면에 표출되는 text 느낌
- 반복문 반복 횟수 설정
  - for page in links: 구문에서 links[a:b]: 로 적어주면 a항부터 ~ b항까지 반복할 수 있음
    - for page in links[:-1]: > 첫 항 부터 마지막 항 빼고 반복
- 뽑아낸 페이지 번호를 int(page)로 형 변환한다.
- max_val = max(pages)로 페이지 최대값을 저장
- 헷갈리는 부분
  - list[-1]이 마지막항이고, list[:-1]이 마지막 항을 제외 한 값인 이유
    - list[-1]은 결국 list[len(list)-1] 값이 라는 것이다.
    - 6개의 항을 갖고 있을 경우 len(list)는 6이고, -1은 5이다.
    - 따라서 list[-1] = list[5]로 마지막 항을 가리킨다.
    - 마찬가지로 list[:-1] = list[0:5]라는 뜻이니까.. int i=0, i<5, i++ 느낌으로 되는건가?

#### #2-5 Requesting Each Page

- 목표
  - 페이지 수 만큼 Request를 만듦
  - extract_indeed_pages() function 만들기
  - extract_indeed_job(last_page) function 만들기
- range(n) 크기가 n인 배열을 생성해주는 함수 활용
  - print(range(n)) 하면 range(0, n)일 출력
  - for output in range(n): 해서 output을 출력하면 0~n-1까지 출력됨
- indeed.py 페이지를 만들어서 기존 requests, beatifulsoup 작업들을 function으로 만들어준다.
  - extract_indeed_pages()
    - 기존 마지막 페이지를 return해주는 function
    - URL, LIMIT를 변수에 담아 동적으로 활용가능 하도록 진행
  - extract_indeed_job(last_page)
    - extract_indeed_pages()에서 last_page를 받아 매개변수로 넣음
    - 페이지 수만큼 range(last_page)를 만들어 for문으로 돌려줌
    ```python
      for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}") #페이지별 URL을 request하여 페이지별 데이터를 가져온다.
        print(result.status_code) #페이지별 request가 정상 작동하였는지 상태 값만 출력해본다.
    ```
- 결과는 200이 페이지수 만큼 출력되면 정상작동 한 것이고, 이후 작업은 다음 강의에서 진행

#### #2.6 Extracting Titles

- 목표
  - Indeed 공고글의 title 가져오기
- URL을 동적으로 받아 soup를 만듦

```python
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
```

- find, find_all
  - find_all은 해당 조건의 태그를 모두 가져오는 것
  - find는 해당 조건의 태그 하나만 가져오는 것. 2개 이상일 시 가장 위에 것 1개
- find, find_all 조건 작성(둘 다 조건 거는 것은 같다)

  - find("태그명", {"속성":"속성값"})
  - find("태그명")["속성"]

  ```python
    results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"}) #class명이 jobsearch-SerpJobCard인 div 태그를 모두 가져온다.

    .
    .
    .

    title = result.find("div",{"class":"title"}) #class명이 title인 div tag 1개를 가져온다.
    anchor_title = title.find("a")["title"] #title의 첫번쨰 a태그에서 title 값을 가져온다.
  ```

- find_all, find, for문을 이용해서 페이지별 채용공고글 제목을 출력한다.

  ```python
    def extract_indeed_jobs(last_page):
    jobs = []

    for page in range(last_page):
      result = requests.get(f"{URL}&start={page*LIMIT}")
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
      for result in results:
        title = result.find("div",{"class":"title"}).find("a")["title"]
        print(title)

    return jobs
  ```

  - 의문점
    - 데이터는 잘 나오는데 실제 화면과 비교 시 데이터 누락이 많음

#### #2.7 Extracting Companies

- 뜬금없지만 BeautifulSoup, soup 모두 많은 것들을 담는다는 뜻으로 쓰는듯. like 김치찌개
- 목표
  - Indeed 채용 공고의 회사명 출력
  - .strip()으로 공백 지우기
  - if, else문 활용
- 회사명은 class명이 company인 span에 들어있다.

  - 이 때 span에 회사명이 a tag에 들어 있는 것이있고, a tag 없이 text만 있는 것이 있다.
  - 따라서 find("span",{"class":"company"}).find("a").string을 했을 때 None 데이터가 나올 수 있음
  - if, else 활용
    - 결과값을 str 형변환 해서 변수에 넣어줌

  ```python
    company = result.find("span", {"class": "company"})
    company_anchor = company.find("a")

    if company_anchor is not None:
      company = str(company_anchor.string)
    else:
      company = str(company.string)
  ```

- 회사명에 공백이 많으므로 공백 제거
  - trim() 같은 역할을 파이썬에서는 .strip() 함수가 함
    - str.strip() 시 str 양쪽 공백이 지워짐
    - .strip("F") 하면 str 내부의 F가 지워짐
    ```python
      company = company.strip()
    ```

#### #2.8 Extracting Locations and Finishing up

- 목표
  - extract_indeed_jobs에서 extract_indeed_job 분리
  - 공고문에서 위치 수집
  - 공고문에서 지원 링크로 넘기는 link_id 수집
- title, company, location을 추출하고 함수를 정리해서 데이터를 return 받도록 한다.

  - title: div.title > a tag의 title property에 있다.
  - company: span.company에 들어있는데 anchor tag가 있는 것도 있고 없는 것도 있다.
    - if문을 통해 span.company > anchor가 None type이면 span.company.string return
    - anchor가 있으면 span.company.find("a").string
  - location: div.recJobLoc의 data-rc-loc property
  - link_id: 현재 기본적으로 구인 공고의 카드 div를 html로 받아오는데, 해당 html의 data-jk property
  - 데이터는 dictionary type으로 return

- return 받은 데이터를 모든 페이지에서 추출

  ```python
    # indeed.py
    import requests
    from bs4 import BeautifulSoup

    LIMIT = 50
    URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

    def extract_indeed_pages():
      resul = requests.get(URL)
      soup = BeautifulSoup(resul.text, "html.parser")

      pagination = soup.find("div", {"class":"pagination"})

      links = pagination.find_all("a")
      pages = []
      for page in links[:-1]:
        pages.append(int(page.find("span").string))

      max_val = max(pages)

      return max_val

    def extract_indeed_job(html):
      title = html.find("div",{"class":"title"}).find("a")["title"]

      company = html.find("span",{"class":"company"})
      company_anchor = company.find("a")
      if company:
        if company_anchor is not None:
          company = company_anchor.string
        else:
          company = company.string
        location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
      else:
        company = None

      data_id = html["data-jk"]
      link = f"https://kr.indeed.com/viewjob?jk={data_id}"

      return {"title":title,"company":company,"location":location, "link":link}

    def extract_indeed_jobs(last_page):
      jobs = []

      for page in range(last_page):
        print(f"Scrapping Indeed page: {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
        for result in results:
          jobs.append(extract_indeed_job(result))

      return jobs

    def get_jobs():
      last_page = extract_indeed_pages()
      jobs = extract_indeed_jobs(last_page)
      return jobs
  ```

#### #2.9 StackOverflow Pages

- Indeed는 #2.8로 끝이다. main.py에 있는 로직을 indeed.py로 옮겨준다.
- StackOverflow는 데이터에 국가 컬럼이 있는지 몰라도 데이터 추출 시 전 세계 게시글, 페이지가 추출되는 것 같다.
- 내 화면에는 python 검색 시 12페이지인데 soup에 추출되는 페이지는 172이고 게시글에도 각지 언어로 되어있는 것을 보면 그렇다.
- 목표
- stackOverFlow pagination 추출

#### #2.10 StackOverflow extract_jobs

- 목표
- StackOverflow에서 직업 id 가져오기 > extract_jobs
- .string, .get_text()
- string의 경우 해당 태그의 text가 단일할 경우 해당 값을 return해줌
  - 자식 태그가 있으면 자식 태그가 1개이고 그 태그에 text가 1개일 경우에만 return하고 그 외는 에러
- .get_text()는 공백을 포함한 1개 이상의 모든 text를 return 해주는 것 같음(\n같은 것도 반환함)
  - 해당 데이터의 공백 제거를 위해 strip을 할 경우 .get_text(strip=True)라고 쓰면 된다.
- 아래와 같은 구문은 작동하질 않음.

```python
  results = soup.find_all("div",{"class":"-job"})["data-jobid"]
```

- find_all 한 것이 배열로 담기고 그것을 for문으로 풀면서 거기에다가 ["data-jobid"]값을 추출해야함

#### #2.11 StackOverflow extract_job

- 목표
  - 공고의 직업, 회사명 return
  - unpacking value : 해당 요소의 개수를 알 때 다중 변수명으로 바로 할당 받는 것
  - recursive = False: 추출 요소를 깊게 탐색하지 않고 한단계만 탐색하기
- ~~공고글 card에서 직업 title을 가져오는 것인데, stackoverflow에서 막았는지 잘 추출되지 않아서 강의만 듣기로함.~~
- html을 읽어 본 결과 grid class를 가진 div가 상단에 하나 있어서 find할 시 그것만 가져와서 오류처럼 느껴졌었음.
  - 결과적으로 우리가 필요로하는 데이터는 div.grid 자식 요소였는데 접근할 방법을 몰랐음.
  - div.grid 자식 요소의 유일한 자식인 div.grid--cell.fl1 > a.s-link에 있는 것을 보고 div.grid를 건너뛰고 추출함
  ```python
    def extract_so_job(html):
      title = html.find("a",{"class":"s-link"})["title"]
      print(title)
  ```
- 회사와 지역은 한 tag 아래 2개의 span에 각각 있었고, 강의영상에서는 회사 span 안에 여러 깊이의 span이 있었다.
  - 그래서 니코는 recursive=False라는 추출 Depth를 1로 하는 설정을 하였는데, 내가 보고있는 데이터는 span 하위에 더 이상 span이 없었기 때문에 쓰나 안쓰나 데이터는 비슷했지만 넣어주었다.
  - unpacking value는 h3 tag 하위에 2개의 span에 각각 company, location이 담겨있음을 알고 있으면
    - company_row[0], company_row[1] 이런 식으로 구분해서 print할 수 있다.
    - 또한 company_row로 받지 말고 애초에 company, location = 데이터 이런 식으로 하면 각각 나뉘어서 변수에 담긴다.
    - 받은 데이터는 get_text(strip=true)로 공백을 제거한 데이터만 받는다.
    ```python
      def extract_so_job(html):
        title = html.find("a",{"class":"s-link"})["title"]
        company, location = html.find("h3").find_all("span", recursive=False)
        print(company.get_text(strip=True), location.get_text(strip=True))
    ```

#### #2.12 StackOverflow extract_job part Two

- 목표
  - 불필요한 문자, 공백을 제거한 company, location 가져오기
- 나의 경우는 해당 사항이 없어 불필요하지만 내용 정리
  - .get_Text(strip=True).strip("-").strip("\n").strip("\r")
  - \n, \r 을 제거해줌

#### #2.13 StackOverflow finish

- 목표

  - 해당 공고 링크 추출(apply_link)
  - Indeed와 StackOverflow 추출 데이터 return

  ```python
      # so,py
      import requests
      from bs4 import BeautifulSoup

      URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

      def extract_last_page(): # 마지막 페이지 수 찾기
        result = requests.get(URL)
        soup = BeautifulSoup(result.text, "html.parser")
        pagination = soup.find("div",{"class":"s-pagination"})
        pages = pagination.find_all("a")
        last_page = pages[-2].get_text(strip=True) #-1은 next고 -2는 마지막 page를 return함
        return int(last_page)

      def extract_so_jobs(last_page): # 직업 추출 * 페이지 수
        jobs = []
        for page in range(last_page):
          print(f"Scrapping SO page: {page}")
          result = requests.get(f"{URL}&pg={page+1}")
          soup = BeautifulSoup(result.text, "html.parser") # 공고글 card div를 가져온
          results = soup.find_all("div",{"class":"-job"})
          for result in results:
            job = extract_so_job(result)
            jobs.append(job)
        return jobs

      def extract_so_job(html):
        title = html.find("a",{"class":"s-link"})["title"]
        company, location = html.find("h3").find_all("span", recursive=False)
        company = company.get_text(strip=True)
        location = location.get_text(strip=True)
        url_id = html["data-jobid"]
        apply_link = f"https://stackoverflow.com/jobs/{url_id}"
        return {'title':title, 'company':company, 'location':location, 'apply_link':apply_link}

      def get_so_jobs():
        last_page = extract_last_page()
        jobs = extract_so_jobs(last_page)
        return jobs
  ```

#### #2.14 What is CSV

- 목표
  - excel, 구글 드라이브 등으로 변환할 수 있는 CSV로 데이터 담기
- CSV
  - Comma Separated Values: 쉼표로 구분된 값
  - 단순하게 라인이 다르면 row가 다르고
  - 콤마로 다뒤면 column으로 나눈다.
  - .CSV로 저장해서 엑셀로도 열고(콤마 구분) Preview로도 볼 수 있다.

#### #2.15 Saving to CSV

- 목표
  - python open function을 이용해서 csv 파일 만들기
  - open function의 mode property 알기
  - csv library import하고 csv 파일에 데이터 작성하기
