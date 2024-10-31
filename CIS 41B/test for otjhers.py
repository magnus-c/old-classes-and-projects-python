from urllib.request import urlopen
import requests
import re
from bs4 import BeautifulSoup

def openHtmlSite(htmlsite):
    html= urlopen(htmlsite)
    soup = BeautifulSoup(html,'html.parser')
    return soup


souph= openHtmlSite("https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita")


thetable = souph.find('table',  class_='wikitable sortable')

headers = [header.text for header in thetable.find_all('th')]
print(headers)
           
countries= []
for country in thetable.find_all('a'):
    countries.append(country.text.strip())

print("These are the countries" ,countries)
print(souph.prettify())

years= []
for year1980 in thetable.find_all('td'):
    years.append(year1980.text.strip())

print("These are the years" ,years)


