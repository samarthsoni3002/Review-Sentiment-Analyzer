import requests
from bs4 import BeautifulSoup

def scrape_amazon_reviews(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    all_reviews = []
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        reviews = soup.find_all('div', {'data-hook': 'review'})
        
        for review in reviews:
            
            review_text = review.find('span', {'data-hook': 'review-body'}).text.strip()
            all_reviews.append(review_text)
            
    
    else:
        print("Failed to fetch page")

    return all_reviews



