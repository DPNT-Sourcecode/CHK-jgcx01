
class CheckoutSolution:
    
    # Dictionary Storing all the offers for sku
    multi_special_offers = {
        'A': [(5,200),(3, 130)],
        'B': [(2, 45)],
        'H': [(10, 80), (5, 45)],
        'K': [(2, 120)],
        'P': [(5,200)],
        'Q': [(3,80)],
        'V': [(3, 130), (2, 90)]
    }
    
    # Dictionary storing all the prices of the sku
    price = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15,
        'E': 40, 'F': 10, 'G' : 20, 'H': 10, 
        'I': 35, 'J': 60, 'K': 70, 'L': 90, 
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 
        'Q': 30, 'R': 50, 'S': 20, 'T': 20, 
        'U': 40, 'V': 50, 'W': 20, 'X': 17, 
        'Y': 20, 'Z': 21
    }
    
    # Dictionary storing all the cross sku free item offers
    free_items_offer={
        'E': (2, 'B', 1),
        'N': (3, 'M', 1),
        'R': (3, 'Q', 1),
    }
    
    # Dictionary storing all the self sku item offers.
    self_free_item_offer={
        'F': (2,1),
        'U': (3,1)
    }
    
    group_offer_items = ['S', 'T', 'X', 'Y', 'Z']
    group_offer_size = 3
    group_offer_price = 45

    def checkout(self, skus):
        #Checking to see if input is a string and upper case
        if not isinstance(skus,str):
            return -1

        count = {}
        
        #Looping to count the frequency of skus
        for sku in skus:
            if sku not in self.price:
                return -1
            count[sku] = count.get(sku, 0)+1
        
        total = 0
        
        #Adding free_item_offers for cross items
        for trigger_sku, (required_qty, target_sku, free_qty) in self.free_items_offer.items():
            if trigger_sku in count and target_sku in count:
                times = count[trigger_sku] //required_qty
                count[target_sku] = max(0, count[target_sku] - times * free_qty)
                
        group_items = []
        for item in self.group_offer_items:
            group_items += [item] * count.get(item, 0)
        group_items.sort(key= lambda i : self.price[i], reverse = True)
        
        group_sets = len(group_items) // self.group_offer_size
        total += group_sets * self.group_offer_price
        
        for i in range(group_sets * self.group_offer_size):
            count[group_items[i]] -= 1
                
        for sku, qty in count.items():
            if sku in self.multi_special_offers:
                for offer_qty, offer_price in self.multi_special_offers[sku]:
                    offer_count = qty // offer_qty
                    total += offer_count * offer_price
                    qty = qty % offer_qty
                    
            if sku in self.self_free_item_offer:
                trigger_qty, free_qty = self.self_free_item_offer[sku]
                group_size = trigger_qty + free_qty
                groups = qty // group_size
                remaining = qty % group_size
                total += (groups * trigger_qty + min(remaining, trigger_qty)) * self.price[sku]
            else:
                total += qty * self.price[sku]
                
        return total 
                
    
    

    #Unit Testing
'''
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
            
    #CHK 4 Unit Test
        def h_offer_test(self):
            self.assertEqual(self.checkout.checkout('HHHHHHHHHH'), 80)
        
        def u_offer_test(self):
            self.assertEqual(self.checkout.checkout("UUUU"), 120)
        
        def rq_offer_test(self):
            self.assertEqual(self.checkout.checkout("RRRQ"), 150)
    
    #CHK 5 Unit Test
        def test_group_discount_6(self):
            self.assertEqual(self.checkout.checkout("SXYZZT"), 90)
        
        def test_group_offer_with_remiander(self):
            self.assertEqual(self.checkout.checkout("STXYZ"), 82)
        
        def group_dicount_and_individuals(self):
            self.assertEqual(self.checkout.checkout("STXAB"), 45 + 50 + 30)
    
    
            
            
    #unittest.main()
'''



