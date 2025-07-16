
class CheckoutSolution:
    
    multi_special_offers = {
        'A': [(5,200),(3, 130)],
        'B': [(2, 45)]
    }
    
    price = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
    }
    
    free_items_offer={
        'E': (2, 'B', 1)
    }

    # skus = unicode string
    def checkout(self, skus):
        #Checking to see if input is a string and upper case
        if not isinstance(skus,str):
            return -1

        total = 0
        count = {}
        
        #Looping to count the frequency of skus
        for sku in skus:
            if sku not in self.price:
                return -1
            count[sku] = count.get(sku, 0)+1
        
        total = 0
        
        #Adding free_item_offers
        for sku, (required_qty_sku, offer_sku, free_qty_sku) in self.free_items_offer.items():
            if sku in count and offer_sku in count:
                offer_times = count[sku] // required_qty_sku
                count[sku] = max(0, count[offer_sku] - offer_times * free_qty_sku)
        
        #Calculatiung the total cost with offers and applying multi-buy offers
        for sku, qty in count.items():
            if sku in self.multi_special_offers:
                for offer_qty, offer_price in self.multi_special_offers[sku]:
                    num_offers = qty // offer_qty
                    total += num_offers * offer_price
                    qty = qty % offer_qty
            else:
                pass
            
            total += qty * self.price[sku]
                
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

