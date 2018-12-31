import re
 
 
def readTXT():
    lines = []
    data = []
    with open ('data.txt', 'rt') as data:
        for line in data:
            if line.find('<a href="https://www2.eecs.berkeley.edu/Faculty/Homepages/') == -1:
                print(' ')
            else:
                lines.append(line)
    for l in lines:
        data.append(re.sub('\s+', ' ', l))
    print(data)


def main():
    readTXT()


if __name__ == "__main__":
    main()