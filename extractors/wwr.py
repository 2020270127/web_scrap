from bs4 import BeautifulSoup
import requests

results = []
def extract_wwr_jobs(term):
  url = f"https://weworkremotely.com/remote-jobs/search?term={term}"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    # write your ✨magical✨ code here

    
    jobs = soup.select("li.feature > a")


    for job in jobs:
      company = job.select("span.company")[0]    
      if company:
        company = company.string#.strip() #span company가 두개라서 이렇게 함
        
      position = job.find("span",class_="title")
      if position:
        position = position.string
      
      location = job.find("span",class_="region company")
      if location:
        location = location.string#.strip()

      link = job.get('href')
      if link:
        link = link#.string.strip()
        
      job_data = {
          'company': company.replace(",",""),
          'position': position.replace(",",""),
          'location' : location.replace(",",""),  #list에 추가하기 전에 dict으로 집합 만들기
          'link' : f"https://weworkremotely.com{link}"
      }  
      results.append(job_data)
    return results
        
  else:
    print("Can't get jobs.")
print(extract_wwr_jobs("java"))
