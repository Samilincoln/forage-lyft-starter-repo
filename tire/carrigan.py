from tire.tire import Tire



class Carrigan(Tire):
    def __init__(self, tirewear_values):
        self.tirewear_values = tirewear_values

    def needs_service(self):
        for x in self.tirewear_values:
            if x >= 0.9:
                return True
            else:
                return False
            
        

        
