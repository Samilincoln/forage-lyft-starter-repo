

from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery


class Palindrome(SternmanEngine, SpindlerBattery):
    def needs_service(self):
        engine_status = SternmanEngine.needs_service()
        battery_health = SpindlerBattery.needs_service()

        if engine_status or battery_health:
            return True
        else:
            return False
