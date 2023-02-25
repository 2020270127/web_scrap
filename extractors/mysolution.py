from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    # write your ✨magical✨ code here
    

    results = {}
    outputs = {}
    # 결과값 저장할 dic 선언  

    page = soup.find('div',class_="page")
    container = page.find('div',class_="container")
    jobsboard = container.find('table',id="jobsboard")
    company = jobsboard.select("tr")
    if(len(company)<6): #검색 결과가 없을경우. 6인 이유는 슈퍼광고 직장이 있기 때문이다.
       print("Can't get jobs.")
       exit('정상 종료') # 더 부드럽게 종료하는 방법은 없을까?


    for i in range(20): #직업 리스트 크롤링시 최대 20개로 확인 
        results[i] = {}
        
        results[i]['title'] = company[3*(i+1)].select_one("td a h2")
        results[i]['company'] = company[3*(i+1)].select_one("td span h3")
        results[i]['options'] = company[3*(i+1)].find_all("div",class_="location")
        results[i]['tags'] = company[3*(i+1)].select("td a h3")
        #솔직히 이렇게 접근하는게 구린거 같음

    # for i in range(20):
    #     if(results[i]['title'] == None):
    #        exit('정상 종료') #close 된 직장들의 집합이 시작할때 분리자가 1개가 아니라 2개다.
    #        # 그럴경우 None타입이므로 프로그램 종료

    #     print("Title : ",results[i]['title'].string.replace("\n",''))
    #     print("\n")

    #     print("Company : ",results[i]['company'].string.replace("\n",''))
    #     print("\n")

    #     print("Options : ")
    #     for text in results[i]['options']: #리스트의 html 제거를 위해서 for로 각각 접근
    #         print(text.string.replace("\n",''))
    #     print("\n")

    #     print("Tags : ")
    #     for text in results[i]['tags']:
    #         print(text.string.replace("\n",''))#리스트의 html 제거를 위해서 for로 각각 접근
    #     print("\n")

    #     print("/////////////////////////////\n/////////////////////////////\n")
    #     #분리
    for i in range(20):
        outputs[i] = {}

        if(results[i]['title'] == None):
           exit('정상 종료') #close 된 직장들의 집합이 시작할때 분리자가 1개가 아니라 2개다.
           # 그럴경우 None타입이므로 프로그램 종료

        print(results)


  else:
    print("Can't get jobs.")


