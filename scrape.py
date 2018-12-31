from lxml import html
import requests
import re
from bs4 import BeautifulSoup
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import csv


def scrapedata():
    page = requests.get('https://www2.eecs.berkeley.edu/Faculty/Lists/CS/faculty.html')
    tree = html.fromstring(page.content)
    professors = []
    title = []
    email = list(emaildata())
    interests = []
    profilelink = []
    list1 = []
    i = 1
    while i != 104:
        list1.append(i)
        i += 1
    print(list1)
    for i in list1:
        professors.append(re.sub('[^A-Za-z0-9 ]+', '', str(tree.xpath('//*[@id="block-system-main"]/div/div[' + str(i) + ']/div[2]/h3/a/text()'))))
        title.append(re.sub('[^A-Za-z0-9 ]+', '', str(tree.xpath('//*[@id="block-system-main"]/div/div[' + str(i) + ']/div[2]/p/strong[1]/text()'))))
        interests.append(re.sub('[^A-Za-z0-9 ]+', '', str(tree.xpath('//*[@id="block-system-main"]/div/div[' + str(i) + ']/div[2]/p/a[' + str(i) + ']/text()'))))
        profilelink.append(re.sub('[^A-Za-z0-9 ]+', '', str(tree.xpath('//*[@id="block-system-main"]/div/div[' + str(i) + ']/div[2]/h3/a/text()'))))
    print(professors)
    print(title)    
    print(interests)
    print(profilelink)
    with open('data.csv', mode = 'w') as employee_file:
        writer = csv.writer(employee_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writer.writerow(['Profressor Name', 'Title', 'Email', 'interests', 'profilelink'])
        for i in list1:
            writer.writerow([professors[i], title[i], email[i], interests[i], profilelink[i]])


def emaildata():
    new_urls = deque(['https://www2.eecs.berkeley.edu/Faculty/Lists/CS/faculty.html'])
    processed_urls = list()
    emails = list()
    url = new_urls.popleft()
    processed_urls.append(url)
    # extract base url to resolve relative links
    parts = urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url
    print("Processing %s" % url)
    response = requests.get(url)
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    emails.append(new_emails)
    print(emails)
    return emails


def main():
    scrapedata()


if __name__ == "__main__":
    main() 