class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software):
        total_memory = sum([software.memory_consumption for software in self.software_components])
        total_capacity = sum([software.capacity_consumption for software in self.software_components])
        if software.memory_consumption <= self.memory-total_memory and \
                software.capacity_consumption <= self.capacity-total_capacity:
            self.software_components.append(software)
            return True
        raise Exception("Software cannot be installed")

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)


