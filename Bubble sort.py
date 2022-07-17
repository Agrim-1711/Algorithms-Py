#Bubble sort

import random
import time

#num_list = []
#while len(num_list) < 10:
  #n = random.randint(1,999)
  #num_list.append(n)
#print(num_list)

start=time.time()
num_list = [random.randint(1,999) for n in range (1,1001)]
print(f"input: {num_list} \n")

# Swap function
def swap_pos(pos1,pos2):
  num_list[pos1], num_list[pos2] = num_list[pos2], num_list[pos1]
  return num_list

for m in range(1,len(num_list)):
  for n in range(0,len(num_list)-m):
    #print(f"{n}, {num_list[n]}")
    if num_list[n] > num_list[n+1]:
      swap_pos(n,n+1)
      #print(f"output after {n+1} comparisons: {num_list}")
  #print(f"output after {m} passes: {num_list}")
print(f"output: {num_list}")
end=time.time()
print("Bubble sort for",len(num_list),"takes:",end-start,"seconds")