from concurrent.futures import ThreadPoolExecutor

# code in this file includes small samples of code from https://github.com/drsjb80/HPotter
# as a way of seeing how certain syntax works.

# line 21 in https://github.com/drsjb80/HPotter/blob/main/src/ListenThread.py
list1 = [1,2,3,4,5]
list2 = ['hey']
tst = 3 in list1 and list2[0] #if '3 in list1' is true, then 'tst' = list2[0]
print(tst)

# line 82 in https://github.com/drsjb80/HPotter/blob/main/src/ListenThread.py
list3 = [1,2,3]
tst = (list3[0],int(list3[2])) #creates tuple
print(tst)

# line 102 in https://github.com/drsjb80/HPotter/blob/main/src/ListenThread.py
i = 0
with ThreadPoolExecutor(max_workers=4) as executor: #define maximum number of executable threads?
    while True: 
        i+=1
        print(i)
        if i > 10000: break
