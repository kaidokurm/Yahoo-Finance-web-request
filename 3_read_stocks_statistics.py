#
# Read data from Yahoo imported file
#

import os
def opendatafile():
    priceToBook=',"priceToBook":{"raw":'
    returnAssets='returnOnAssets":{"raw":'
    enterpriseToRevenue='"enterpriseToRevenue":{"raw":'
    price='<div class="D(ib) Va(m) Maw(65%) Ov(h)" data-reactid="29"><div class="D(ib) Mend(20px)" data-reactid="30"><span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid="31">'
    profitmargin=',"profitMargins":{"raw":'
    
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open("stockStatistic/"+filename, encoding='utf-8') as f:
                pv=0.0#price value
                bv=0.0#priceToBookValue
                ra=0.0#Return assets
                erv=0.0#enterpriseValueToRevenue
                pm=0.0#Profitmargin
                for li in f:
                    if profitmargin in li:
                        x=li.split(profitmargin)[1]
                        xi=x.split(',"fmt"')[0]
                        try:
                            pm=float(xi)
                        except ValueError:
                            pm=0
                    if enterpriseToRevenue in li:
                        x=li.split(enterpriseToRevenue)[1]
                        xi=x.split(',"fmt"')[0]
                        try:
                            erv=float(xi)
                        except ValueError:
                            erv=0

                    if price in li:
                        x=li.split(price)[1]
                        xi=x.split('</span>')[0]
                        try:
                            pv=float(xi)
                        except ValueError:
                            pv=0
                    if returnAssets in li:
                        x=li.split(returnAssets)[1]
                        xi=x.split(',"fmt"')[0]
                        try:
                            ra=float(xi)
                        except ValueError:
                            ra=0
                    if priceToBook in li:
                        x=li.split(priceToBook)[1]
                        xi=x.split(',"fmt"')[0]
                        try:
                            bv=float(xi)
                        except ValueError:
                            bv=0
                    if bv!=0 and pv!=0 and ra!=0 and bv!=0 and erv!=0 and pm!=0:#
                        addtoarray(filename,pv,bv,ra,erv,pm)
                        break

#add data to array
def addtoarray(e,pv,bv,ra,erv,pm):
    stocks.append([e,pv,bv,ra,erv,pm])
    print(e+ ' PriceToBook:' +str(bv)+' Price:'+ str(pv)+' ReturnOnAssets:' +str(ra)+' EvR:' +str(erv)+' ProfitMargin:' +str(pm))

#read the peratio file
def readFile():

    opendatafile()        
    stocks.sort(key=lambda x: x[3])

    #write sorted result to file
    with open("result.txt", 'w') as r:
        r.write("Stock Price PriceToBook ReturnOnAssets EnterpriceValueToRevenue ProfirMargin \n")
        for i in stocks:
            for j in i:
                r.write(str(j)+" ")
            r.write("\n")
    print("Done!")

#create stocks empty list
stocks=[]
directory = 'stockStatistic'
readFile()