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
