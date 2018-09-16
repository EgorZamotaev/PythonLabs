import math

#bubble sort
def BubbleSort(x):
   n = len(x)
   i = 0; j = 0; k = 0;
   for i in range(0, n-1):
       j = i
       for k in range(i, n):
           if x[k]<x[j]:
               j = k
       x[i], x[j] = x[j], x[i]
       
#gnome sort
def GnomeSort(list):
   n = len(a)
   i = 0
   while i < n-1:
       if a[i] <= a[i+1]:
           i +=1
       else:
           a[i], a[i+1] = a[i+1], a[i]
           if i != 0:
               i -= 1
           else:
               i +=1

#bucket sort
def listmerge(lstlst):
    all=[]
    for lst in lstlst:
      all.extend(lst)
    return all

def BucketSort(x):
  l=min(x)
  m=int((max(x)-min(x))/10)+1
  z=[]
  for i in range(m):
    f=[]
    for j in range(len(x)):
      if int(x[j])<l+(i+1)*10 and int(x[j])>=l+i*10:
        f.append(x[j])
    z.append(f)
  for  bucket in range(len(z)):
    BubbleSort(z[bucket])
  z=listmerge(z)
  for num in range(len(x)):
    x[num]=z[num]



def hashing(a):
  m = a[0]
  for i in range(1, len(a)):
    if (m < a[i]):
      m = a[i]
  result = [m, int(math.sqrt(len(a)))]
  return result

 
 
def re_hashing(i, code):
  return int(i / code[0] * (code[1] - 1))


   
#heatsort

# To heapify subtree rooted at index i.
def heapify(arr, n, i):
    largest = i # обозначить наибольшее значение как корень
    l = 2 * i + 1     
    r = 2 * i + 2     
    # Проверить, есть ли левое поддерево и больше ли оно, чем корень
    if l < n and arr[i] < arr[l]:
        largest = l
    # Проверить, есть ли правое поддерево и больше ли оно, чем корень
    if r < n and arr[largest] < arr[r]:
        largest = r
    # Поменять корень, если значение largest изменились
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)
 
def HeapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    # Уменьшаем количество элементов по одному
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
 

a = []
for i in range(int(input())):
    a.append(int(input()))
    
func=input("Выберите вид сортировки: BubbleSort, GnomeSort, BucketSort, HeapSort ")
if func=="BubbleSort":
  BubbleSort(a)
if func=="GnomeSort":
  GnomeSort(a)
if func=="BucketSort"
  BucketSort(a)
if func=="HeapSort"
  HeapSort(a)
print(a)
