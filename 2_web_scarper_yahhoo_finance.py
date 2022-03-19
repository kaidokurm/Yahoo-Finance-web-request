#
# This is for collecting webpages from finance.yahoo and store them
#


import requests
import time
from bs4 import BeautifulSoup

def saveToFile(data, file): #save collected data to stock named file 
    with open("stockStatistic/"+file, "a+", encoding='utf-8') as file_object:
        file_object.write(data)

def check(continueFrom):
    url='https://finance.yahoo.com/quote/'
    key='/key-statistics'
    with open('stocklist.txt') as fo:
        for i, line in enumerate(fo):
            if i>continueFrom:
                symbol=line.split(";")[0]
                w=url+symbol+key
                try:
                    page= requests.get(w, headers={'User-Agent': 'Custom'}) #without header it wont work
                    if(page):
                        soup = BeautifulSoup(page.content, 'html.parser')
                        saveToFile(str(soup), symbol+".txt")
                        print(str(i)+ " " +symbol)
                        continueFrom=i
                except ValueError:
                    print('Error')
                    time.sleep(10)
                    check(continueFrom)
                    return()#exit()        
    print("done!")

continueFrom=12903#Continue from line
check(continueFrom-1)