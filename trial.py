import requests
from bs4 import BeautifulSoup

def scrape_amazon_reviews(url):

    proxies = {
        'http': 'http://103.105.196.176:80',
        'https': 'http://35.181.9.127:12453'
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url,headers=headers,proxies=proxies,verify=False)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        reviews = soup.find_all("div", class_="a-section review aok-relative")
        for review in reviews:
            try:
                review_title = review.find("a", class_="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold").text.strip()
            except AttributeError:
                review_title = "No title"
            try:
                review_body = review.find("span", class_="a-size-base review-text review-text-content").text
            except AttributeError:
                review_body = "No review text"
            try:
                review_rating = review.find("i", class_="review-rating").text
            except AttributeError:
                review_rating = "No rating"
            print("Title:", review_title)
            print("Rating:", review_rating)
            print("Review:", review_body)
            print("="*50)
    else:
        print("Failed to fetch page")


url = "https://www.amazon.in/Monitoring-Suitable-appliances-Geysers-Assistant/dp/B0BRQCJ57Y?ref_=Oct_DLandingS_D_9ad57e8d_0&th=1"

review_url = url.replace("dp","product-reviews")

scrape_amazon_reviews(url)
