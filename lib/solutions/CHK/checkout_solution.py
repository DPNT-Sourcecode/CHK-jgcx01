
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
        #Checking for the string of the itme and if it not an uppercase letter
        if not isinstance(skus,str) or not skus.alpha():
            return -1

        skus.upper()
        count = {}
        
        for sku in skus:
            if sku not in self.price:
                return -1
            count[sku] =- count.get(sku, 0)+1
        
        total = 0
        
        
        for sku, qty in count.items():
            price = self.price[sku]
            if sku in self.special_offers:
                offer_qty, offer_price = self.special_offers[sku]
                offer_groups = qty // offer_qty
                remainder = qty % offer_qty
                total + offer_groups * offer_price + remainder * price
            else:
                total += qty * price 
        return total 

