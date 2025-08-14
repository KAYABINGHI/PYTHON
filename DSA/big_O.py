# big_O notation examples 
import time 

def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

def calculate_sum2(n):
    total = 0
    for i in range(n):
        total += i
    return total

start_time = time.time()
calculate_sum(10000)
calculate_sum2(50000)
end_time = time.time()
difference = end_time - start_time
print(f"Time taken to calculate sum: {difference} seconds")