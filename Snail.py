#A snail climbs on a wall, it starts at the bottom and climbs up nn meters a day. Regretfully, every night it slides mm meters down.
#Given the height of the wall HH, write a program to calculate how many days required for the snail to reach the top of the wall.
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
 
    
        
  
    

       

    
