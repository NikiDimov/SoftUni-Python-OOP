from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                if hardware.install(software):
                    return System._software.append(software)
        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                software = LightSoftware(name, capacity_consumption, memory_consumption)
                if hardware.install(software):
                    return System._software.append(software)
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                for software in hardware.software_components:
                    if software.name == software_name:
                        hardware.uninstall(software)
                        System._software.remove(software)
                        return
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        software_memory = sum([software.memory_consumption for software in System._software])
        hardware_memory = sum([hardware.memory for hardware in System._hardware])
        result += f"Total Operational Memory: {software_memory} / {hardware_memory}\n"
        software_capacity = sum([software.capacity_consumption for software in System._software])
        hardware_capacity = sum([hardware.capacity for hardware in System._hardware])
        result += f"Total Capacity Taken: {software_capacity} / {hardware_capacity}\n"
        return result.strip()

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            express_soft_comp = 0
            light_soft_comp = 0
            memory_usage_of_soft = 0
            capacity_usage_of_soft = 0
            for software in hardware.software_components:
                if software.software_type == "Express":
                    express_soft_comp += 1
                elif software.software_type == "Light":
                    light_soft_comp += 1
                memory_usage_of_soft += software.memory_consumption
                capacity_usage_of_soft += software.capacity_consumption
            result += f"Express Software Components: {express_soft_comp}\n"
            result += f"Light Software Components: {light_soft_comp}\n"
            result += f"Memory Usage: {memory_usage_of_soft} / {hardware.memory}\n"
            result += f"Capacity Usage: {capacity_usage_of_soft} / {hardware.capacity}\n"
            result += f"Type: {hardware.hardware_type}\n"
            result += f"Software Components: {', '.join([software.name for software in hardware.software_components]) if hardware.software_components else 'None'}\n"
        return result.strip()


System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())
