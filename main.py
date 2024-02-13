from recipe_scrapers import scrape_me
import csv_write as cw


outlist=[]
for web in weblist:
    scraper = scrape_me(web)

    # Q: What if the recipe site I want to extract information from is not listed below?
    # A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
    #scraper = scrape_me('https://www.feastingathome.com/tomato-risotto/', wild_mode=True)
    
    inlist=[]
    inlist.append(web)
    host=scraper.host()
    print(host)
    
    title=scraper.title()
    print(title)
    inlist.append(title)
    json=scraper.to_json()
    print(json['description'])
    inlist.append(json['description'])
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