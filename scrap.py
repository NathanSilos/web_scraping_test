import requests
from bs4 import BeautifulSoup

def import_countries(): 
    # open the website and take the html page with ".content"
    html = requests.get('https://scrapethissite.com/pages/simple/').content

    # Create an object as a HTML document
    soup = BeautifulSoup(html, 'html.parser')

    # Taking the countries HTMLs
    country_name = soup.find_all("h3", class_="country-name")
    country_capital = soup.find_all("span", class_="country-capital")
    country_population = soup.find_all("span", class_="country-population")
    country_area = soup.find_all("span", class_="country-area")

    country_information = {}

    # Incluinding countring in a dict
    for i in range(len(country_name)):
        country_information[' '.join(country_name[i].text.split())] = {
            'capital': ' '.join(country_capital[i].text.split()),
            'population': int(' '.join(country_population[i].text.split())),
            'area': float(' '.join(country_area[i].text.split()))
        }
    
    return country_information