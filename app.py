import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://www.ibge.gov.br/explica/codigos-dos-municipios.php"
page = requests.get(URL)

# with open("dados.txt",'w') as f:
#     f.write(page.text)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify('utf-8'))

cidades = soup.find_all("tr", class_="municipio data-line")
# print(cidades)
dados = []
for c in cidades:
    d = {}
    d['municipio']= c.find("a").get_text()
    d['codigo']= c.find("td", class_="numero").get_text()
    dados.append(d)
    
df = pd.DataFrame(dados)
print(df)
df.to_csv('cdmunicipios.csv', sep="|", index=False)