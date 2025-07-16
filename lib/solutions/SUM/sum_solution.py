
class SumSolution:
    
    def compute(self, x, y):
        #Checking that both x and y are both postive intergers between 0 and 100 
        if (not isinstance(x, (int,float)) or not isinstance(y, (int,float))):
            raise TypeError("Both x and y should be postive integers")

        if not (0 <= x <= 100) or not (0 <= y <= 100):
            raise TypeError("Both x and y should be between 0 and 100")
        
        return x + y


