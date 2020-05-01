# Hello! My name is Wonnetz Phanthavong and this is the
# first ever web scraper I ever built. It isn't the most efficient
# piece of code, but it works!
# I use these two links to learn how to do this.
# https://www.youtube.com/watch?v=XQgXKtPSzUI&t
# https://medium.com/@msalmon00/web-scraping-job-postings-from-indeed-96bd588dcb4b

import requests
import csv
from bs4 import BeautifulSoup as soup

URL = 'https://www.indeed.com/jobs?q=data+analyst&l=Atlanta%2C+GA'


# Saves the data of the URL
page = requests.get(URL)


# HTML Parses the HTML text of the given URL
page_soup = soup(page.text, "html.parser")

# Creating the file and its headers
outfile = "Indeed_Job_Listings.csv"
headers = "title, company, date posted, summary"

# Opens the file and grants writing permissions
f = open(outfile, "w")
f.write(headers)

# Extracts the title of the job
def extract_job_title(soup):
    jobs = []
    for h2 in soup.findAll(name="h2", attrs={"class": "title"}):
        for a in h2.findAll(name="a", attrs={"data-tn-element": "jobTitle"}):
            jobs.append(a["title"])
    return jobs


# Extracts the company name
def extract_company(soup):
    companies = []
    for div in soup.findAll(name="div", attrs={"class": "sjcl"}):
        companies.append(div.span.text.strip())
    return companies


# Extracts the date the listing was posted
def extract_date(soup):
    date = []
    for div in soup.findAll(name="div", attrs={"class": "result-link-bar"}):
        date.append(div.span.text.strip())
    return date


# Extracts the summary of the job
def extract_summary(soup):
    summary = []
    for div in soup.findAll(name="div", attrs={"class": "summary"}):
        summary.append(div.text.strip())
    return summary


# This assigns the return results to actual values
titles = extract_job_title(page_soup)
companies = extract_company(page_soup)
dates = extract_date(page_soup)
summaries = extract_summary(page_soup)

# Tests the results
print(titles)
print(companies)
print(dates)
print(summaries)

# Sets up the lists to be written to the csv file
rows = zip(titles, companies, dates, summaries)

with open("Indeed_Job_Listings.csv", "w") as outfile:
    wr = csv.writer(outfile, dialect='excel')
    for row in rows:
        wr.writerow(row)

f.close()