#VG TIMES
import bs4, requests
import re
from main.models import Post
import os

def vg_names():
    name_arr = []
    url = 'https://vgtimes.ru/tags/%D0%98%D0%B3%D1%80%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/'
    sep = '\"'
    j = 19

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    out = soup.find_all(class_='item-name type0')

    for item in out:
        str1 = str(item.text)
        str1 = str1[1:-2]
        str1 = str1
        name_arr.append(str1)   

    del name_arr[10:]

    return(name_arr)

def vg_links():
    link_arr = []
    url = 'https://vgtimes.ru/tags/%D0%98%D0%B3%D1%80%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/'
    sep = '\"'
    j = 19

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    out = soup.find_all(class_='item-name type0')

    for item in out:
        str1 = str(item)
        str1 = str1[39:]
        str1 = str1.split(sep, 1)[0]
        link_arr.append(str1)

    del link_arr[10:]   

    return link_arr

def vg_content():
    link_arr = vg_links()
    arr = []
    arr1 = []
    j = 11
    for item in link_arr:
        url = item
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        out = soup.find_all(class_="news_item_content")
        for item in out:
            str1 = str(item.text)
            str1 = str1.replace("\r","")
            str1 = str1.replace("\n","")
            arr.append(str1)
    for item in arr:
        item = str(item)
        item = item[0:-171]
        arr1.append(item)

    del arr1[10:]

    return arr1

def vg_date_time():
    link_arr = vg_links()
    arr = []
    date_arr = []
    time_arr = []
    date_time_arr = []
    for link in link_arr:
        url = link
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        out = soup.find_all(class_="news_item_date")
        for item in out:
            str1 = str(item)
            str1 = str1[44:]
            str1 = str1.split("+")
            arr.append(str1[0])
    for item in arr:
        str1 = str(item)
        str1 = str1.replace("-",".")[0:-3]
        str1 = str1.split("MSK")
        str1 = "|".join(str1)
        date_time_arr.append(str1)
    
    del date_time_arr[10:]
    return date_time_arr

def vg_time():
    date_time = vg_date_time()
    time = []

    for item in date_time:
        item = str(item)
        item = item.split("|")
        time.append(item[1])
    return time

def vg_date():
    date_time = vg_date_time()
    date = []

    for item in date_time:
        sm1 = []
        item = str(item)
        item = item.split("|")
        sm = str(item[0])
        year = str(sm[0:4])

        for item in sm:
            sm1.append(item)
        del sm1[0:5]
        sm1 = "".join(sm1)
        sm1 = sm1+"."+year
        sm1 = sm1.split(".")
        sm1[0], sm1[1] = sm1[1], sm1[0]
        sm1 = ".".join(sm1)
        
        date.append(sm1)
        arr1 = []

    for item in date:
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

def vg_old_date():
    date_time = vg_date_time()
    date = []

    for item in date_time:
        sm1 = []
        item = str(item)
        item = item.split("|")
        sm = str(item[0])
        year = str(sm[0:4])

        for item in sm:
            sm1.append(item)
        del sm1[0:5]
        sm1 = "".join(sm1)
        sm1 = sm1+"."+year
        sm1 = sm1.split(".")
        sm1[0], sm1[1] = sm1[1], sm1[0]
        sm1 = ".".join(sm1)
        date.append(sm1)
    return date


    #src="/uploads/posts/2021-05/v-steam-vyshla-novaya-pesochnica-s-otkrytym-mirom-v-kotoroy-obeschayut-prodvinutyy-kraft-77278-m.jpg?1621339308"
def vg_img():
    Post.objects.all().delete()

    names = vg_names()
    conts = vg_content()
    dts = []
    date = vg_date()
    time = vg_time()
    site = "vgtimes"
    chck = re.compile(r'src\=\".*\"')
    url = 'https://vgtimes.ru/tags/%D0%98%D0%B3%D1%80%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8'
    img_urls= []
    
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    out = soup.find_all("div",class_="image_wrap type0")

    urls = []

    for item in out:

        mo = chck.search(str(item))
        img_urls.append('https://vgtimes.ru'+mo.group()[5:-1])

    del img_urls[10:]
    
    i = 1

    for item in img_urls:
        res = requests.get(item)
        img_file = open(os.path.join('D:\\agregator\\gamers_gazette\\game_news_site\\media\\images','vg{}.png'.format(i)), 'wb')
        urls.append('images/vg{}.png'.format(i))
        i = i + 1

        for chunk in res.iter_content(100000):
            img_file.write(chunk)
        img_file.close()

    i = 0

    for item in date:
        dts.append(str(item)+" "+time[i])
        i = i + 1
    
    for i in range (0, 10):
        p = Post(site = site, title = names[i], img = urls[i], pub_date = dts[i], time = time[i], date = date[i], text =  conts[i])
        p.save() 