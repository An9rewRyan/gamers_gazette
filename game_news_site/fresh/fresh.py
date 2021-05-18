from fresh.sorting import quicksort

import bs4, requests

from igrm import igrm
from dtf import dtf
from vg import vg
from sort import sorting

import datetime
import operator

#from igrm import *
#from dtf import *
#from vg import *
#from sorting import *

from main.models import Post

def fresher():

    now = datetime.datetime.now()
    time = now.strftime("%H:%M")
    date = now.strftime("%d.%m.%Y")

    dtf_t = dtf.dtf_time()   
    vg_t = vg.vg_time()  
    igrm_t = igrm.igrm_time() 

    #dtf_t = dtf_time()  
    #vg_t = vg_time() 
    #igrm_t = igrm_time() 
    #dtf_d = dtf_old_date() 
    #vg_d = vg_old_date()  
    #igrm_d = igrm_old_date() 

    dtf_d = dtf.dtf_old_date()   
    vg_d = vg.vg_old_date()  
    igrm_d = igrm.igrm_old_date() 

    checker = True

    d3 = []
    d4 = []

    t1 = []
    t2 = []
    t3 = []
    t4 = []

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

    if d2 == []:
       
        for key in d1:
            t1.append(key)
        
        return sorting.quicksort(t1)

    if len(d2) == 1:

        for key in d1:
            t1.append(key)
            
        for key in d2:
            t2.append(key)
        
        return d2 + sorting.quicksort(t1)

    if len(d2) > 1:
        
        vals = d2
        vals = list(vals.values())
        val = vals[0]
        cnt = 1
        
        while cnt < len(d2):
            
            for key in d2:
                
                if d2[key] != val:
                    
                    d3 = dict(list(d2.items())[cnt:])
                    d4 = dict(list(d2.items())[:cnt-1])
                    break
                
                else:
                    cnt = cnt + 1

    if d3 == [] or d4 == []:

        for key in d1:
            t1.append(key)
            
        for key in d2:
            t2.append(key)

        return sorting.quicksort(t2) + sorting.quicksort(t1)

    if d3 != [] and d4 != []:

        for key in d1:
            t1.append(key)

        for key in d3:
            t3.append(key)

        for key in d4:
            t4.append(key)

        return sorting.quicksort(t4) +  sorting.quicksort(t3) + sorting.quicksort(t1)

def filler():

    arr = fresher()

    v_name = vg.vg_names()
    v_link = vg.vg_links()
    v_content = vg.vg_content()
    v_time = vg.vg_time()  
    v_date = vg.vg_date()  
    v_dt = []

    d_name = dtf.dtf_names()
    d_link = dtf.dtf_links()
    d_content = dtf.dtf_content()
    d_time = dtf.dtf_time()   
    d_date = dtf.dtf_date() 
    d_dt = []
    d_img_links = []
    
    #for i in range(1,11):
       # d_img_links.append("images/dtf{}.png".format(i))

    i_name = igrm.igrm_names()
    i_link = igrm.igrm_links()
    i_content = igrm.igrm_content()
    i_date = igrm.igrm_date() 
    i_time = igrm.igrm_time() 
    i_dt = []

    i = 0
    j = 0
    k = 0 
    o = 0

    for item in d_date:
        d_dt.append(str(item)+" "+d_time[i])
        i = i + 1

    i = 0

    for item in v_date:
        i_dt.append(str(item)+" "+i_time[i])
        i = i + 1
    
    i = 0

    for item in i_date:
        v_dt.append(str(item)+" "+v_time[i])
        i = i + 1

    i = 0



    Post.objects.all().delete()

    while i < 28:

        if arr[i] == d_time[j]:
            site = "dtf"
            p = Post(site = site, title = d_name[j], pub_date = d_dt[j], time = d_time[j], date = d_date[j], text =  d_content[j])
            p.save()    
            i = i + 1
            j = 0
            k = 0
            o = 0
        else:
            j = j + 1

        if arr[i] == i_time[k]:
            site = "igromania"
            p = Post(site = site, title = i_name[k], pub_date = i_dt[k],time = i_time[k], date = i_date[k], text =  i_content[k])
            p.save()
            i= i + 1
            k = 0
            o = 0
            j = 0

        else:
            k = k + 1

        if arr[i] == v_time[o]:
            site = "vgtimes"
            p = Post(site = site, title = v_name[o], pub_date = v_dt[o],time = v_time[o], date = v_date[o], text =  v_content[o])
            p.save()
            i = i + 1
            o = 0
            j = 0
            k = 0

        else:
            o = o + 1