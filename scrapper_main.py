from recipe_scrapers import scrape_me
import extract

websites=input(r"Enter websites to Scrape information(multiple websites to be seperated by comma):")

weblist= websites.split(",")
print(weblist)
scrapelist={}
for web in weblist:
    #scraper = scrape_me(https://www.allrecipes.com,https://baking-sense.com,https://bakingmischief.com,https://averiecooks.com)
    scraper = scrape_me(web)
    json=scraper.links()
    #print((json))
    
    print("Scraping receipes pls be patient.....")
    cnt=0
    slist=[]
    tlist=[]
    for j in json:
        if 'href' in j:
            #print(j)
            #print()
            href=j['href']
            #href="'"+href+"'"
            #href='https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/'
            
            #print(".")
            try:
                scraper = scrape_me(href)
                title=scraper.title()
                if title not in tlist:
                    slist.append(href)
                    tlist.append(title)
                    print("Scraping Reciepe ",cnt,":",title)
                    cnt=cnt+1
                if cnt > 2:
                    break
                
            except :
                pass
    print("slist is",slist)
    scrapelist[web]=slist

print(scrapelist)
if len(scrapelist) > 0:
    print("collecting data")
    extract.main(scrapelist,weblist)
else:
    print("no data could be scraped")





#https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/