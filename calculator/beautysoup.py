import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

mysoup = BeautifulSoup(page.content, "html.parser")
results = mysoup.find(id="ResultsContainer")
print(results.prettify())

# extract string from the html
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.string)
    print(company_element.string.strip())
    print(location_element.string)
    print()

