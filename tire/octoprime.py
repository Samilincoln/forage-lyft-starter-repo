from tire.tire import Tire



class Octoprime(Tire):
    def __init__(self, tirewear_values):
        self.tirewear_values = tirewear_values

    def checker(self):
        val_sum = 0
        for x in self.tirewear_values:
            val_sum += x
        return val_sum

    def needs_service(checker):
        if checker() >= 3:
            return True
        else:
            return False
           