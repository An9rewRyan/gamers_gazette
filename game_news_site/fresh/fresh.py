import bs4, requests
from igrm import igrm
from dtf import dtf
from vg import vg
from sort import sorting
import datetime
import operator
from main.models import Post

def fresher():

    now = datetime.datetime.now()
    time = now.strftime("%H:%M")
    date = now.strftime("%d.%m.%Y")
    dtf_t = dtf.dtf_time()   
    vg_t = vg.vg_time()  
    igrm_t = igrm.igrm_time() 

    dtf_d = dtf.dtf_date()   
    vg_d = vg.vg_date()  
    igrm_d = igrm.igrm_date() 

    t_list1 = []
    t_list2 = []
    tarray = vg_t + igrm_t + dtf_t   
    darray = vg_d + igrm_d + dtf_d

    tarray.append(time)
    darray.append(date)

    dt = dict(zip(tarray, darray))

    sorted_tuples = sorted(dt.items(), key=operator.itemgetter(1))
    s_dt = {k: v for k, v in sorted_tuples}
    cnt = 1


    for key in s_dt:
        if dt[key] == date:
            d1 = dict(list(s_dt.items())[cnt:])
            d2 = dict(list(s_dt.items())[:cnt-1])
            break
        else:
            cnt = cnt + 1

    for item in d1:
        t_list1.append(item)

    for item in d2:
        t_list2.append(item)

    t_list1 = sorting.quicksort(t_list1)
    t_list2 = sorting.quicksort(t_list2)
    
    arr = t_list2 + t_list1

    return arr

def filler():

    arr = fresher()

    v_name = vg.vg_names()
    v_link = vg.vg_links()
    v_content = vg.vg_content()
    v_time = vg.vg_time()  
    v_date = vg.vg_date()  

    d_name = dtf.dtf_names()
    d_link = dtf.dtf_links()
    d_content = dtf.dtf_content()
    d_time = dtf.dtf_time()   
    d_date = dtf.dtf_date() 

    i_name = igrm.igrm_names()
    i_link = igrm.igrm_links()
    i_content = igrm.igrm_content()
    i_date = igrm.igrm_date() 
    i_time = igrm.igrm_time() 

    i = 0
    j = 0
    k = 0 
    o = 0
    Post.objects.all().delete()
    while i < 29:

        if arr[i] == d_time[j]:
            site = "dtf"
            p = Post(site = site, title = d_name[j],time = d_time[j], date = d_date[j], text =  d_content[j])
            p.save()    
            i = i + 1
            j = 0
            k = 0
            o = 0
        else:
            j = j + 1

        if arr[i] == i_time[k]:
            site = "igromania"
            p = Post(site = site, title = i_name[k],time = i_time[k], date = i_date[k], text =  i_content[k])
            p.save()
            i= i + 1
            k = 0
            o = 0
            j = 0

        else:
            k = k + 1

        if arr[i] == v_time[o]:
            site = "vgtimes"
            p = Post(site = site, title = v_name[o],time = v_time[o], date = v_date[o], text =  v_content[o])
            p.save()
            i = i + 1
            o = 0
            j = 0
            k = 0

        else:
            o = o + 1