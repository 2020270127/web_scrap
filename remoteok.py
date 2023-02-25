from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    # write your ✨magical✨ code here
    results = []
    jobs = soup.find_all("tr",class_="job")
    
    for job in jobs:
      company = job.find("h3", itemprop="name")
      if company:
        company = company.string.strip()
      
      position = job.find("h2", itemprop="title")
      if position:
        position = position.string.strip()

      location = job.find("div", class_="location")
      if location:
        location = location.string.strip()

      job_data = {
        'company': company,
        'position': position,
        'location' : location  #list에 추가하기 전에 dict으로 집합 만들기
      }  
      results.append(job_data) #append는 리스트에서만 가능

    
    return results
    

    
  else:
    print("Can't get jobs.")



