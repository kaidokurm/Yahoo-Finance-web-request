#
# Get the stock symbol list from LHV 
#

import requests

stocksList=[]
first=('<tr bgcolor="#eeeeee">\\n\\t\\t\\t<td class="small-text" valign=top nowrap>')
def saveToFile(data):
    with open("stocklist.txt", "a+", encoding='utf-8') as file_object:
        for e in data:
            oe=''
            for ie in e:
                oe=oe+str(ie)+';'
            file_object.write(oe+'\n')

def readlines(page):
    lines=str(page).split(first)
    lines.pop(0)
    for line in lines:
        e=line.split('</td>\\n\\t\\t\\t<td class="small-text" valign=top>')
        s=[]
        for u in e:
            a=u.split('</td>\\n\\t\\t\\t<td class="small-text" valign=top nowrap>')
            for n in a:
                n1=n.split('</td>')[0]
                s.append(n1)
        stocksList.append(s)

def readdata():
    url='https://www.lhv.ee/search/shortname.cfm?submit=1&type=12001&flag_short=0&flag_game=0&query=&exchange=&x=2&y=7&page='
    maxpage=119
    i=1
    while i<maxpage+1:
        w=url+str(i)
        page= requests.get(w, headers={'User-Agent': 'Custom'})
        if(page):
            readlines(page.content)
        i=i+1
        print(i)
    saveToFile(stocksList)
    print("done!")
    print(stocksList)
readdata()