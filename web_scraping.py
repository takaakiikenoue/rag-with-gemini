import requests                   
from bs4 import BeautifulSoup 

def get_webpage_text(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }        
    response = requests.get(url, headers=headers)  
    soup = BeautifulSoup(response.text, 'html.parser')  

    for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'ins']):
        tag.decompose()

    text = soup.get_text()       
    lines = [line.strip() for line in text.split('\n') if line.strip()]  
    text = ' '.join(lines)  

    return text