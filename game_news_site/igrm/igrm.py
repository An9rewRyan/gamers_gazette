#IGROMANIA
import bs4, requests
import re
from main.models import Post
import os

def igrm_names():
    name_arr = []
    url = 'https://www.igromania.ru/news/industry/'
    sep = '\"'
    j = 24

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    out = soup.find_all(class_='aubli_name')

    for item in out:
        name_arr.append(item.text)

    for i in range (1,14):
        del name_arr[j]
        j = j -1
    
    del name_arr[10:]

    return(name_arr)

def igrm_links():
    link_arr = []
    url = 'https://www.igromania.ru/news/industry/'
    sep = '\"'
    j = 24

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    out = soup.find_all(class_='aubli_name')

    for item in out:
        str1 = str(item)
        str1 = str1[28:]
        str1 = str1.split(sep, 1)[0]
        link_arr.append("https://www.igromania.ru/"+str1)

    for i in range (1,14):
        del link_arr[j]
        j = j -1
    
    del link_arr[10:]

    return(link_arr)

def igrm_content():
    sep = 'Больше на Игромании'
    link_arr = igrm_links()
    arr = []
    arr1 = []
    j = 11

    for item in link_arr:
        url = item
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        out = soup.find_all(class_="page_news_content haveselect")
        for item in out:
            str1 = str(item.text)
            str1 = str1.replace("\r","")
            str1 = str1.replace("\n","")
            str1 = str1.split(sep)
            arr.append(str1[0])

    del arr[10:]

    return arr

def igrm_date_time():
    link_arr = igrm_links()
    arr = []
    date_arr = []
    time_arr = []
    date_time_arr = []
    data = re.compile(r'\d\d\.\d\d\.\d\d\d\d\s\d\d\:\d\d')
    for link in link_arr:
        url = link
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        out = soup.find_all(class_="page_news_info clearfix")
        for item in out:
            str_ = str(item)
            mo = data.search(str_)
            arr.append(mo.group())
    for item in arr:
        str_ = str(item)
        str_ = str_.replace(' ','|')  
        date_time_arr.append(str_) 
    del date_time_arr[10:]
    return date_time_arr

def igrm_time():
    date_time = igrm_date_time()
    time = []

    for item in date_time:
        item = str(item)
        item = item.split("|")
        time.append(item[1])
    return time

def igrm_date():
    date_time = igrm_date_time()
    date = []

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
        date.append(item)
    return date

def igrm_old_date():
    date_time = igrm_date_time()
    date = []

    for item in date_time:
        item = str(item)
        item = item.split("|")
        date.append(item[0])
    return date

def igrm_main():
    site = "igromania"
    names = igrm_names()
    conts = igrm_content()
    dts = []
    date = igrm_date()
    time = igrm_time()
    site = ""
    chck = re.compile(r'src\=\".*\"')
    url = 'https://www.igromania.ru/news/industry/'
    img_urls= []
    
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    out = soup.find_all("div",class_="aubl_item")

    urls = []

    for item in out:

        mo = chck.search(str(item))
        img_urls.append(mo.group()[5:-1])

    del img_urls[10:]
    
    i = 1

    for item in img_urls:
        res = requests.get(item)
        img_file = open(os.path.join('D:\\agregator\\gamers_gazette\\game_news_site\\media\\images','igrm{}.png'.format(i)), 'wb')
        urls.append('images/igrm{}.png'.format(i))
        i = i + 1

        for chunk in res.iter_content(100000):
            img_file.write(chunk)
        img_file.close()

    i = 0

    for item in date:
        dts.append(str(item)+" "+time[i])
        i = i + 1
    
    for i in range (0, 10):
        p = Post(site = "igromania", title = names[i], img = urls[i], pub_date = dts[i], time = time[i], date = date[i], text =  conts[i])
        p.save() 
