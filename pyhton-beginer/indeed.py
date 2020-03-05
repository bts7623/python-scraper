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
      company = company_anchor.get_text(strip=True)
    else:
      company = company.get_text(strip=True)
    location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
  else:
    company = None

  data_id = html["data-jk"]
  link = f"https://kr.indeed.com/viewjob?jk={data_id}"

  return {"title":title,"company":company,"location":location, "link":link}


def extract_indeed_jobs(last_page):
  jobs = []

  # for page in range(last_page):
  for page in range(2):
    # print(f"Scrapping Indeed page: {page}")
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