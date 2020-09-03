
import time
initialize=time.time()
print(initialize)
i=0
while(i<=50):
    i=i+1
    print(i,time.time()-initialize)
initialize2=time.time()
for j in range(0,1):
    print(j)
print("This is ending of while loop, and print time",time.time()-initialize2)

