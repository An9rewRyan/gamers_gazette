import bs4, requests

def quicksort(array): 

    if len(array) < 2:

        return array
        
    else: 

        pivot = array[0]
        less = [i for i in array if i < pivot]
        greater=  [ i for i in array if i > pivot]

        return quicksort(less)  + [pivot] + quicksort(greater)





