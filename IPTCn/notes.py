from concurrent.futures import ThreadPoolExecutor

# code in this file includes small samples of code from https://github.com/The-Mostly-Muggles/HPotter
# as a way of seeing how certain syntax works.
# The code in this file is not necessarily intended to compile or execute.

# line 21 in .../src/ListenThread.py
list1 = [1,2,3,4,5]
list2 = ['hey']
tst = 3 in list1 and list2[0] #if '3 in list1' is true, then 'tst' = list2[0]
print(tst)

# line 82 in ../src/ListenThread.py
list3 = [1,2,3]
tst = (list3[0],int(list3[2])) #creates tuple
print(tst)

# line 102 in ../src/ListenThread.py
i = 0
with ThreadPoolExecutor(max_workers=4) as executor: #define maximum number of executable threads?
    while True: 
        i+=1
        print(i)
        if i > 10000: break

# line 120 .../src/ListenThread.py
'''
ct = ContainerThread(source, self.connection, self.config) # Create ContainterThread object
f = executor.submit(ct.start) # (from Python documentation) invoking start() function on a thread 
                              # object will invoke that object's run() function.
'''

# line 117 .../src/ContainerThread.py
# client = docker.from_env() # instansiate client... connect using default socket or environment configs
# line 118 
# self.container = client.containers.run(self.config['container'], detach=True) # create and run container in background
# self.container.reload() # retrieve all attributes of a container object, Default=FALSE

# line 101 ContainerThread.py: start_and_join threads(): creates OneWayThread objects and waits for them to terminate.
# line 95 ContainerThread.py: remove_rules(): Deletes "FORWARD" rule from 'self'... 
# not really sure about this one, I believe this function serves the purpose of halting the forwarding of network traffic. 
