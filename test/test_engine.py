import unittest
from datetime import datetime
from engine import capulet_engine, willoughby_engine, sternman_engine
from battery import nubbin_battery, spindler_battery

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        current_day = datetime.today().date()
        last_service_date = current_day.replace(year=current_day.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0