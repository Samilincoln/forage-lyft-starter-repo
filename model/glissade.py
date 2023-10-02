

from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery


class Glissade(WilloughbyEngine, SpindlerBattery):
    def needs_service(self):
        engine_status = WilloughbyEngine.needs_service()
        battery_health = SpindlerBattery.needs_service()

        if engine_status or battery_health:
            return True
        else:
            return False
