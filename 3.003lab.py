import random

arr = random.sample(range(-6, 6), 12)
print("our random list: ", arr)
flag = 0
                                            
while flag == 0:
    if 0 in arr: # перевіряємо чи є 0 в списку
        first_zero_index = arr.index(0) # індекс першого 0
        flag = 1;
    else:
        print("we have not at list one zero in list: ")
    arr1 = []
if flag == 1:
    for i in arr[first_zero_index:]: arr1.append(i)
print(arr1)
