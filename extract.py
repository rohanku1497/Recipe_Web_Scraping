from recipe_scrapers import scrape_me
import csv_write as cw

def main(weblist,sitenames):
    outlist=[]
    cnt=0
    for web in weblist:
        scrapeitems=weblist[web]
       
        #outlist.append(["Recipe extracted from: ",sitenames[cnt]])
        cnt=cnt+1
        for si in scrapeitems:
        
            scraper = scrape_me(si)
            inlist=[]
            # Q: What if the recipe site I want to extract information from is not listed below?
            # A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
            #scraper = scrape_me('https://www.feastingathome.com/tomato-risotto/', wild_mode=True)
            
            host=scraper.host()
            print(host)
            
            title=scraper.title()
            print(title)
            inlist.append(title)
            try:
                json=scraper.to_json()
                print(json['description'])
                inlist.append(json['description'])
            except:
                inlist.append(["No Description available on website"])
            tt=scraper.total_time()
            print(tt)
            inlist.append(tt)
            img=scraper.image()
            print(img)
            inlist.append(img)
            ind=scraper.ingredients()
            print(ind)
            inlist.append(ind)
            ins=scraper.instructions()
            print(ins)
            inlist.append(ins)
            insl=scraper.instructions_list()
            print(insl)
            inlist.append(insl)
            yl=scraper.yields()
            print(yl)
            inlist.append(yl)
            
            #lk=scraper.links()
            #print(lk)
            nut=scraper.nutrients() 
            print(nut)
            inlist.append(nut)
            outlist.append(inlist)
            
        
    cw.main(outlist)