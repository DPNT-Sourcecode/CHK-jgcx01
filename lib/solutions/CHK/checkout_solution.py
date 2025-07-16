
class CheckoutSolution:
    
    special_offers = {
        'A': (3, 130),
        'B': (2, 45)
    }
    
    price = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
    }

    # skus = unicode string
    def checkout(self, skus):
        #Checking to see if input is a string and upper case
        if not isinstance(skus,str) or not skus.alpha():
            return -1

        skus = skus.upper()
        count = {}
        
        #Looping to count the frequency of skus
        for sku in skus:
            if sku not in self.price:
                return -1
            count[sku] =- count.get(sku, 0)+1
        
        total = 0
        
        #Calculatiung the total cost with offers
        for sku, qty in count.items():
            price = self.price[sku]
            if sku in self.special_offers:
                offer_qty, offer_price = self.special_offers[sku]
                #Applyiung offer as may times as possible
                offer_groups = qty // offer_qty
                remainder = qty % offer_qty
                total + offer_groups * offer_price + remainder * price # if there is no offer then its regualr pricing 
            else:
                total += qty * price 
                
        return total 
    
    
    '''
    #Unit Testing
if __name__ == "__main__":
    import unittest
    class TestCheckoutSolutuon(unittest.TestCase):
        
        def setUp(self):
            self.checkout = CheckoutSolution()
        #Checking result for single item 
        def single_item(self):
            self.assertEqual(self.checkout.checkout("A"), 50)
        
        #Checkig result for special offers applied
        def special_offer(self):
            self.assertEqual(self.checkout.checkout("AAD"), 130 + 15)
            
        #Checking result for invalid items 
        def invalid_chracter(self):
            self.assertEqual(self.checkout.checkout("AXHY"), -1)
            
        #Checking result for no items 
        def invalid_chracter(self):
            self.assertEqual(self.checkout.checkout(" "), -1)
            
            
    #unittest.main()
    
    '''
