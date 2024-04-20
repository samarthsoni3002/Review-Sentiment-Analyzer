import requests
from bs4 import BeautifulSoup

def scrape_amazon_reviews(url):



    response = requests.get(url)
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
                review_body = review.find("span", class_="a-size-base review-text review-text-content").text.strip()
            except AttributeError:
                review_body = "No review text"
            try:
                review_rating = review.find("i", class_="review-rating").text.strip()
            except AttributeError:
                review_rating = "No rating"
            print("Title:", review_title)
            print("Rating:", review_rating)
            print("Review:", review_body)
            print("="*50)
    else:
        print("Failed to fetch page")


url = "https://www.amazon.in/Monitoring-Suitable-appliances-Geysers-Assistant/dp/B0BRQCJ57Y?ref_=Oct_DLandingS_D_9ad57e8d_0&th=1"

scrape_amazon_reviews(url)
