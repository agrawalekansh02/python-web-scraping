from contextlib import closing
from bs4 import BeautifulSoup


def readHTML():
    raw_html = open('data.html').read()
    htmler = BeautifulSoup(raw_html, 'html.parser')
    datacollection =[]
    for p in htmler.findAll('div',{"class":True}):
        paragraph = htmler.find(class = "media-body")
        datacollection.append(str(paragraph) + "\n")
    print(datacollection)



def main():
    readHTML()


if __name__ == "__main__":
    main()