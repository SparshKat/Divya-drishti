import requests 
from bs4 import BeautifulSoup
import time
nameold = ""
while(True):
    with open('data.txt', 'r') as outfile:
        name=outfile.readline()
        outfile.close()
    if name!=nameold:
        url='http://bitsotg.com:8083/api/' + name
        print(url)
        resp=requests.get(url)
        time.sleep(0.2)
    nameold = name


