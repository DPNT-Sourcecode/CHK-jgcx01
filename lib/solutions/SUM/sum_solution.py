
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
    
    #Unit Testing 
    if __name__ == "__main__":
        class TestSumSolution(unittest.TestCase):
            
            def setUp(self):
                self.solver = SumSolution() 
                
            #Testing to see if x and y are in range 0 - 100    
            def valid_range_test(self):
                self.assertEqual(self.solver.compute(25, 89), 100)
                
            #Testing to see if x and y still sum at bounds  
            def valid_bounds_test (self):
                self.assertEqual(self.solver.compute(0, 100), 100)
                
            #Testing to see if x or y are below the range 
            def below_bounds_test(self):
                self.assertEqual(self.solver.compute(-20, 30), 100)
                
            #Testing to see if x or y are above the range 
            def above_bounds_test(self):
                self.assertEqual(self.solver.compute(200, 100), 100)
                
            #Testing to invlaid data types 
            def invalid_datatypes_string_test(self):
                self.assertEqual(self.solver.compute("a", 100), 100)
                               
            def invalid_datatypes_float_test(self):
                self.assertEqual(self.solver.compute(100.4, 100), 100)
                
            def invalid_datatypes_none_test(self):
                self.assertEqual(self.solver.compute(100.4, None), 100)

        unittest.main()
                
    
    
