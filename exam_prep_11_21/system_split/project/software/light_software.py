

from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, software_type="Light", capacity_consumption=int(capacity_consumption*1.5),
                         memory_consumption=int(memory_consumption*0.5))

