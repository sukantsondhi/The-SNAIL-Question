
import sys

for line in sys.stdin:
    
    values = [int(i) for i in line.split()
             if i.isdigit()]
    
    n = values[0]
    m = values[1]
    H = values[2]
    
    days = 0
    dist = 0
    
    while(True):
        dist += n
        days += 1
        
        if dist >= H:
            break
        dist -= m  
          
        if (n - m <= 0):
            days = "Fail"
            break
            
    print(days)
 
    
        
  
    

       

    
