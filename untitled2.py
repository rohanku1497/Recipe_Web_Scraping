# -*- coding: utf-8 -*-
"""
Created on Thu May  4 00:52:23 2023

@author: User
"""

from recipe_scrapers import scrape_me
scraper = scrape_me("https://averiecooks.com")
json=scraper.links()
print(json)
# scraper = scrape_me('https://bakingmischief.com/honey-roasted-carrots/#comments')
# title=scraper.to_json()
#print(title)
# for j in json:
#     print((j))
#     print()