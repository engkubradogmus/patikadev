'''
1)Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

'''
  
  

def flatten_list(n):
    res=[]
    typ = type(n)
    if (typ==list or typ==tuple or typ==set) :
        for item in n:
            item_typ = type(item)
            if (item_typ == str or item_typ==int or item_typ==float):
                res.append(item)
            elif (item_typ==list or item_typ==tuple or item_typ==set):
                res.extend(flatten_list(item)) # Recursion
    else:
        return(n)
    return (res)
    

a=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
b = flatten_list(a)
print(b)
   

  
 '''2)Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
'''




