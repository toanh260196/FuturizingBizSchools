#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:48:19 2017

@author: katerinadoyle
@author: Guy Simons
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import csv
import pandas as pd

 
 
def init_driver():

    #driver = webdriver.Chrome(executable_path='/Users/guysimons/Documents/JAVA/Webscraping/Drivers/chromedriver')
    #driver = webdriver.Chrome(executable_path='/Users/katerinadoyle/Documents/java/webscraping/drivers/chromedriver')
    driver = webdriver.Firefox(executable_path='/Users/katerinadoyle/Documents/java/webscraping/drivers/geckodriver')
    driver.wait = WebDriverWait(driver, 5)
    driver.implicitly_wait(10)
    return driver

def navigate_page(driver, page):
     driver.get(page)          
 
def lookup(driver, query):
    try:
        element = driver.find_element_by_xpath(query).text
        return element
    except:
          print("An error occured, the element doesn't exist")

driver = init_driver()
wait = WebDriverWait(driver, 10) #explicit waits
 
# indeed only has 50 companies listed on 2 pages. this was quickest way to get all the companies
links = ["https://www.indeed.com/Best-Places-to-Work", 
"https://www.indeed.com/Best-Places-to-Work?y=2017&cc=US&start=25"]

#get values of Select(driver.find_element_by_xpath("//div[@id = 'cmp-discovery-country-select']/select"))

companies = [ ]

for item in links:
    navigate_page(driver, item)

    # select the country. Include this in another for-loop? for item in country
    select = Select(driver.find_element_by_xpath("//div[@id = 'cmp-discovery-country-select']/select"))
    select.by_value = ('United States' )

    company_name = driver.find_elements_by_xpath("//div[@id = 'cmp-curated']/div/a/h4[@itemprop='name']")
    for i in range (0, len(company_name)):
        companies.append(company_name[i].text)

    # select the reviews. 

for item in companies:
    rev_comp = []
    pros_comp = []
    cons_comp = []
    #name_slice = item. not sure if this is the easiest way. url is www.indeeed.com/name-of-company. slash btw words need to be added

    #input company name in search field
    #select reviews
    navigate_page(driver, "https://www.indeed.com/Best-Places-to-Work")
    
    inputElement = driver.find_element_by_id("search-by-company")
    inputElement.send_keys(item)
    inputElement.send_keys(Keys.ENTER)
    
    rev_btn = driver.find_element_by_xpath("//div[@class='cmp-tile-footer-element']/a[@data-tn-element='reviews-footer-link']")
    rev_btn.click()

    while True: #
        
        # grap the reviews and store in datafile w/ name = item
        # currently only does 1st page. Need to create loop also for this? Or better way
        #for all pages ()
#            wait.until(EC.visibility_of_element_located())
        txt_rev = driver.find_elements_by_xpath("//span[@class='cmp-review-text']")
        pros = driver.find_elements_by_xpath("//div[@class='cmp-review-pro-text']")
        cons = driver.find_elements_by_xpath("//div[@class='cmp-review-con-text']")
        
        # store output
        for i in range(0, len(txt_rev)):
            rev_comp.append(txt_rev[i].text)
        for i in range(0, len(pros)):
            pros_comp.append(pros[i].text)
        for i in range(0, len(cons)):
            cons_comp.append(cons[i].text)
                
    try:
        #driver.find_element_by_link_text('next-page').click #correct by element?
        driver.find_element_by_class_name("company_reviews_pagination_link_nav".click)
        #currently stock on looping over page 1
    except:
        print ("Done!")
        
    with open ("reviews/"+item+".txt", "w") as output:
            #for i in range(0, len(txt_rev)):
             #   rev_comp.append(txt_rev[i].text)
             output.write(str(rev_comp))
                
    with open("reviews/"+item+"pros.txt", "w") as output:
        #for i in range(0, len(pros)):
         #   pros_comp.append(pros[i].text)
            output.write(str(pros_comp))
            
    with open("reviews/"+item+"cons.txt", "w") as output:
        #for i in range(0, len(cons)):
        #    cons_comp.append(cons[i].text)
            output.write(str(cons_comp))
                    
driver.quit()

#next_btn = driver.find_element_by_xpath("//span[@class='cmp-paginator-page']/a[. ='2']")
#next_btn.click()

#driver = init_driver()
#navigate_page(driver, "https://www.indeed.com/Best-Places-to-Work")


# get names of all companies
'''
for i in range(1, 50):
    
#    if i == 25:    
    next_btn = driver.find_element_by_xpath("//span[@class='cmp-paginator-page']/a[. ='2']")
    next_btn.click()

    company_name = driver.find_elements_by_xpath("//div[@id = 'cmp-curated']/div/a/h4[@itemprop='name']")

    for i in range (0, len(company_name)):
    companies.append(company_name1[i].text)
'''

'''
re.findall('/cmp/?/reviews', response)

for i in range (1, xx): (range of companies)
select reviews page. link to review page always /cmp/name-of-company/reviews
scrape text reviews

# store reviews in data set
    
    

ranks = []
names = []
countries = []

for i in range(1,101):
     rank = str(i)
     ranks.append(lookup(driver, "//*[@id='rankings_mod']/div["+ rank +"]//span[1]"))
     names.append(lookup(driver, "//*[@id='rankings_mod']/div["+ rank +"]//span[2]"))
     countries.append(lookup(driver, "//*[@id='rankings_mod']/div["+ rank +"]//span[3]"))




list_complete = pd.DataFrame({'Rank': ranks, 'University': names, 'Country':countries})
list_complete.to_csv('list.csv', index = False)

''' 
