import requests
from bs4 import BeautifulSoup
import csv

url="https://www.moneycontrol.com/markets/indian-indices/?classic=true"
page = requests.get(url)

filename = 'stocksdata.csv'
csv_writer = csv.writer(open(filename,'w'))


soup = BeautifulSoup(page.content,"html.parser")
table = soup.find('table',class_='responsive')
#print(table)

for tr in table.find_all('tr'):
    data = []
    
    for th in tr.find_all('th'):
        data.append(th.text)
    
    if(data):
        print("Inserting Headers: {}".format(','.join(data)))
        csv_writer.writerow(data)
        continue

    for td in tr.find_all('td'):
        data.append(td.text.strip())
    
    if(data):
       print("Inserting Data: {}".format(','.join(data)))
       csv_writer.writerow(data)
       continue


quit()