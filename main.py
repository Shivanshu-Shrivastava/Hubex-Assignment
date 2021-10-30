from os import replace, write
from bs4 import BeautifulSoup
import requests
import csv

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

print('Which Skill do you have ?')
skll_want = input('>')


soup = BeautifulSoup(html_text,'lxml')

jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

# For saving File in Excel
file  = open('job.csv','w')
writer = csv.writer(file)

# Header row
writer.writerow(['Company Name','Skills','Job Details','More Info'])


for job in jobs:
    company_name = job.find('h3',class_='joblist-comp-name').text.strip()
    skill = job.find('span',class_='srp-skills').text.strip()
    if skll_want in skill :
        details = job.find('ul',class_='list-job-dtl clearfix').li.text.strip()
        published_date = job.find('span',class_='sim-posted').span.text.strip()

        more_info = job.header.h2.a['href']
        print(f'Company Name : {company_name.strip()} ')
        print(f'Skill Required : {skill.strip()} ')
        print(f'Job details : {details.strip()} ')
        print(f'More Details : {more_info.strip()}\n')
        writer.writerow([company_name.encode('utf-8'), skill.encode('utf-8'), details.encode('utf-8'), more_info.encode('utf-8')])

file.close()