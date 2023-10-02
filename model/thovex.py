

from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery


class Thovex(CapuletEngine, NubbinBattery):
    def needs_service(self):
        engine_status = CapuletEngine.needs_service()
        battery_health = NubbinBattery.needs_service()

        if engine_status or battery_health:
            return True
        else:
            return False
