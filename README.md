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
