
import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)

import requests
from bs4 import BeautifulSoup as b
import pandas as pd
from sqlalchemy import create_engine
from variables import get_var

item=[]
for count in range(1,int(get_var("page_number"))):
    URL = "https://petrolpump.hpretail.in/location/karnataka?page="+str(count)
    print(URL)
    resp = requests.get(URL)
    s = b(resp.text, "html.parser")
    data = s.findAll('div', attrs={'class': 'store-info-box'})

    for i in data:
        name = i.find('li', attrs={'class': 'outlet-alternate-name'}).find('div', attrs={'class': 'info-text'}).getText()
        address_merged = i.find('li', attrs={'class': 'outlet-address'}).find('div', attrs={'class': 'info-text'})
        address_spans= address_merged.findAll('span', recursive=False)
        address=""
        for x in address_spans:
            address += ","+x.getText()
        address = address[1:]
        pincode = address.split('-')[1]
        phone = i.find('li', attrs={'class': 'outlet-phone'}).find('div', attrs={'class': 'info-text'}).getText()
        hours = i.find('li', attrs={'class': None}).find('div', attrs={'class': 'info-text'}).getText()
        more_details = i.find('li', attrs={'class': 'outlet-actions'}).find('a', attrs={'class': 'btn-website'}).get('href')
        item.append([int(pincode), name.strip(), address.strip(), phone.strip(), hours.strip(), more_details])
    print("iteration going on >>>>", count)

df = pd.DataFrame (item, columns = ['pincode', 'name', 'address', 'phone', 'hours', 'more'])
print("READY to upload")
engine = create_engine(get_var("DATABASE_URL"))
df.to_sql('information', engine, index=False, if_exists='append')
print("uploaded to DB")