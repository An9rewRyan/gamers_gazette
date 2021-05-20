#DTF
import bs4, requests
import re
import os
from main.models import Post

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
    remove5 = re.compile(r'\d+\s+комментария')
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
            str1 = remove5.sub('',str1)
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

def dtf_main():

    names = dtf_names()
    links = dtf_links()
    conts = dtf_content()
    dts = []
    date = dtf_date()
    time = dtf_time()
    site = "dtf"
    #"https://leonardo.osnova.io/91e47474-c70d-55ad-af16-b3bc2335e282/"
    chck = re.compile(r'\"https\:\/\/.*\/\"')
    url = 'https://dtf.ru/gameindustry/entries/new'
    img_urls= []
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    out = soup.find_all('div',class_='content-image')
    urls = []

    for item in out:

        mo = chck.search(str(item))
        img_urls.append(mo.group()[1:-1])

    del img_urls[10:]

    i = 0

    for item in date:
        dts.append(str(item)+" "+time[i])
        i = i + 1
    
    i = 1

    for item in img_urls:
        res = requests.get(item)
        img_file = open(os.path.join('D:\\agregator\\gamers_gazette\\game_news_site\\media\\images','dtf{}.png'.format(i)), 'wb')
        urls.append('images/dtf{}.png'.format(i))
        i = i + 1

        for chunk in res.iter_content(100000):
            img_file.write(chunk)
        img_file.close()

    i = 1
    
    for i in range (0, 10):
        p = Post(site = site, title = names[i], img = urls[i], pub_date = dts[i], time = time[i], date = date[i], text =  conts[i])
        p.save() 




