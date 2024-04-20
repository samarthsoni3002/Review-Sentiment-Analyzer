import requests
from bs4 import BeautifulSoup
import random


proxies = {
   'http': 'http://103.105.196.176:80',
   'https': 'http://35.185.196.38:3128'
}

url = 'https://www.amazon.in/Monitoring-Suitable-appliances-Geysers-Assistant/dp/B0BRQCJ57Y?ref_=Oct_DLandingS_D_9ad57e8d_0'


review_list = []

review_url = url.replace("dp","product_reviews")

response = requests.get(review_url, proxies=proxies)
print(response.status_code)