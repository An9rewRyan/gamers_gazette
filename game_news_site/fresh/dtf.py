#DTF
import bs4, requests
import re

def dtf_names():
    i = 0
    name_arr = []
    link_arr = []
    url = 'https://dtf.ru/gameindustry/entries/new'

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    soup1 = bs4.BeautifulSoup(res.text, 'html.parser')
    out1 = soup.find_all(class_='content-feed__link')
    out2 = soup1.find_all(class_='content-title content-title--short l-island-a')

    for item in out2:
        str2 = item.text
        str2 = str2[0:-20]
        str2 = str2.replace("\r","")
        str2 = str2.replace("\n","")
        name_arr.append(" "+str2.lstrip())

    for item in out1:
        str_ = str(item)
        str_ = str_[36:-6]
        link_arr.append(str_.lstrip())
    
    del name_arr[10:]

    return name_arr

def dtf_links():
    i = 0
    name_arr = []
    link_arr = []
    url = 'https://dtf.ru/gameindustry/entries/new'

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    soup1 = bs4.BeautifulSoup(res.text, 'html.parser')
    out1 = soup.find_all(class_='content-feed__link')
    out2 = soup1.find_all(class_='content-title content-title--short l-island-a')

    for item in out2:
        str2 = item.text
        str2 = str2[0:-20]
        str2 = str2.replace("\r","")
        str2 = str2.replace("\n","")
        name_arr.append(" "+str2.lstrip())

    for item in out1:
        str_ = str(item)
        str_ = str_[36:-6]
        link_arr.append(str_.lstrip())

    del link_arr[10:]

    return link_arr

def dtf_content():
    link_arr = dtf_links()
    arr = []
    #311311 комментариев8882просмотров
    #237237 комментариев4597просмотров Слушать
    remove1 = re.compile(r'\d+\s+\w+\d+\w+\s+Слушать')
    remove2 = re.compile(r'\d+\s+комментариев\d+просмотров')
    remove3 = re.compile(r'\d+\s+комментарий\d+просмотров')
    remove4 = re.compile(r'\d+просмотров')
    for item in link_arr:

        url = item

        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        out = soup.find_all(class_="content content--full")

        for item in out:

            str1 = str(item.text)
            str1 = str1.replace("\r","")
            str1 = str1.replace("\n","")
            str1 = remove1.sub('',str1)
            str1 = remove2.sub('',str1)
            str1 = remove3.sub('',str1)
            str1 = remove4.sub('',str1)
            #str2 = ' '.join(str1.split())
            #arr.append(str2)

            arr.append(str1) 
    del arr[10:]

    return arr

def dtf_date_time():
    link_arr = dtf_links()
    arr = []
    arr1 = []
    date_arr = []
    time_arr = []
    date_time_arr = []
    data = re.compile(r'\d\d\.\d\d\.\d\d\d\d\s\d\d\:\d\d')
    for link in link_arr:
        url = link
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        out = soup.find_all("span",class_="lm-hidden")
        for item in out:
            str_ = str(item)
            mo = data.search(str_)
            arr.append(mo.group())
    for item in arr: 
        str1 = str(item)
        str1 = str1.rstrip()
        str1 = str1.split(" ")
        str1 = "|".join(str1)
        arr1.append(str1)
    del arr1 [10:]
    return arr1

def dtf_time():
    date_time = dtf_date_time()
    time = []

    for item in date_time:
        item = str(item)
        item = item.split("|")
        time.append(item[1])
    return time

def dtf_date():
    date_time = dtf_date_time()
    date = []
    arr1 = []

    for item in date_time:
        arr = []
        item = str(item)
        item = item.split("|")
        item = str(item[0])
        item = item.split(".")
        arr.append(item[2])
        arr.append(item[1])
        arr.append(item[0])
        item = "-".join(arr)
        arr1.append(item)
    return arr1
def dtf_old_date():
    date_time = dtf_date_time()
    date = []

    for item in date_time:
        item = str(item)
        item = item.split("|")
        date.append(item[0])
    return date
def dtf_name2():
    link_arr = dtf_links()
    arr = []

    for item in link_arr:
        url = item
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        out = soup.find_all(class_="content content--full")


