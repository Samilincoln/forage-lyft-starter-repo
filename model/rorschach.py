

from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery


class Rorschach(WilloughbyEngine):
    def needs_service(self):
        engine_status = WilloughbyEngine.needs_service()
        battery_health = NubbinBattery.needs_service()

        if engine_status or battery_health:
            return True
        else:
            return False
