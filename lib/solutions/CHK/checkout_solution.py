
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
        'F': 10,
    }
    
    free_items_offer={
        'E': (2, 'B', 1),
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
        for trigger_sku, (required_qty, target_sku, free_qty) in self.free_items_offer.items():
            if trigger_sku in count and target_sku in count:
                free_items = (count[trigger_sku] // required_qty) * free_qty
                count[target_sku] = max(0, count[target_sku] - free_items)
                
        for sku, qty in count.items():
            if sku in self.multi_special_offers:
                for offer_qty, offer_price in self.multi_special_offers[sku]:
                    num_offers =  qty // offer_qty
                    total += num_offers * offer_price
                    qty %= offer_qty
                    
            if sku == 'F':
                free_fs = qty //3
                total += (qty - free_fs) * self.price['F']
            else:
                total += qty * self.price[sku]
        
        return total 
                
    
    

    #Unit Testing

if __name__ == "__main__":
    import unittest
    class TestCheckoutSolutuon(unittest.TestCase):
        
    #CHK 1 UNit Test
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
    
    #CHK 2 UNit Test
        def test_special_offer_3A(self):
            self.assertEqual(self.checkout.checkout("AAA"), 130)
    
        def test_special_offer_5A(self):
            self.assertEqual(self.checkout.checkout("AAAAA"), 130)
            
        def free_items_2E_gives_1B(self):
            self.assertEqual(self.checkout.checkout("EEB"), 130)
            
        def test_2E_and_2B(self):
            self.assertEqual(self.checkout.checkout("EEBB"), 130)
            
    #CHK 3 Unit Test
        def test_2F(self):
            self.assertEqual(self.checkout.checkout("FF"),20)
            
        def test_3F(self):
            self.assertEqual(self.checkout.checkout("FFF"), 20)
        
        def test_6F(self):
            self.assertEqual(self.checkout.checkout("FFFFFF"), 40)
            
            
    #unittest.main()




