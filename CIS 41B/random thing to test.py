import requests
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita').text
from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
#print(soup.prettify())

My_table = soup.find('table',{'class':'wikitable sortable'})
#print(My_table)

links = My_table.findAll('a')
#print(links)
areas =My_table.findAll('tr')
print(areas)
#print(links)
Countries = []
Tareas = []
for link in links:
    Countries.append(link.get('title'))
    
print(Countries)

for area in areas:
    Tareas.append(area.get('td'))
    
print(Tareas)

'''
import pandas as pd
df = pd.DataFrame()
df['Country'] = Countries

print(df)
'''