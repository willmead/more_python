num_iterations = 180
rate = 20
total = 10

for time in range(0, num_iterations, rate):
    total *= 2  
    print(f"Time: {time} mins")
    print(f"No. Bacteria: {total}")
    
    
