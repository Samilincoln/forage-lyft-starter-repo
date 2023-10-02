

from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class Calliope(CapuletEngine, SpindlerBattery):
    def needs_service(self):
        engine_status = CapuletEngine.needs_service()
        battery_health = SpindlerBattery.needs_service()

        if engine_status or battery_health:
            return True
        else:
            return False
