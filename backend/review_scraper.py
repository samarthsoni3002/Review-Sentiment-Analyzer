import requests
from bs4 import BeautifulSoup

def scrap_reviews(url):
    proxies = {
        'http': 'http://103.105.196.176:80',
        'https': 'http://35.72.118.126:80'
    }



    review_list = []

    review_url = url.replace("dp","product-reviews")

    print(review_url)

    response = requests.get(review_url,proxies=proxies, verify=False)

    print(response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    if response.status_code == 200:
        
        reviews = soup.findAll('div', {'data-hook':'review'})
        

        
        
        if reviews:
            for item in reviews:
                review_text = item.find("span", {"data-hook": "review-body"})
                if review_text:
                    review_list.append(review_text.text.strip())
    
    return review_list



url = 'https://www.amazon.in/Monitoring-Suitable-appliances-Geysers-Assistant/dp/B0BRQCJ57Y?ref_=Oct_DLandingS_D_9ad57e8d_0&th=1'
reviews = scrap_reviews(url)
print(reviews)
