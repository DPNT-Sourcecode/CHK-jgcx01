
import unittest # importing unit test module to more clerly check for unit testing 
class SumSolution:
    '''
    Sum Solution Class includes a methode called compute to return the sum of 2 numbers
    '''
    
    def compute(self, x, y):
        #Checking that both x and y are both postive intergers 
        if (not isinstance(x, (int,float)) or not isinstance(y, (int,float))):
            raise TypeError("Both x and y should be postive integers")

        #Checking that x and y are both between 0 and 100
        if not (0 <= x <= 100) or not (0 <= y <= 100):
            raise TypeError("Both x and y should be between 0 and 100")
        
        return x + y
    
                
    
    

