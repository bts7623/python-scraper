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
  # for page in range(last_page):
  for page in range(2):
    # print(f"Scrapping SO page: {page}")
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
  return {'title':title, 'company':company, 'location':location, 'link':apply_link}



def get_so_jobs():
  last_page = extract_last_page()
  jobs = extract_so_jobs(last_page)
  return jobs
