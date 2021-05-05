from unittest import TestCase, main

from OOP.exam_prep2.project.hardware.hardware import Hardware
# from project.hardware.hardware import Hardware
from OOP.exam_prep2.project.software.light_software import LightSoftware
# from project.software.light_software import LightSoftware


class TestHardware(TestCase):
    def setUp(self):
        self.hardware = Hardware("My name", "Heavy", 500, 500)

    def test_attr_are_set(self):
        self.assertEqual("My name", self.hardware.name)
        self.assertEqual("Heavy", self.hardware.type)
        self.assertEqual(500, self.hardware.capacity)
        self.assertEqual(500, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_hardware_has_no_memory_when_software_installed_raises(self):
        self.software = LightSoftware("S_name", 501, 501)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(self.software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_equal_capacity_and_memory_when_software_installed(self):
        self.software = LightSoftware("S_name", 300, 1000)
        self.hardware.install(self.software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_software_is_installed(self):
        self.software = LightSoftware("S_name", 200, 500)
        self.hardware.install(self.software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_uninstall_unexisting_software_does_not_complain(self):
        self.software = LightSoftware("S_name", 200, 500)
        self.assertEqual(0, len(self.hardware.software_components))
        self.hardware.uninstall(self.software)
        self.assertEqual(0, len(self.hardware.software_components))

    def test_uninstall_software(self):
        self.software = LightSoftware("S_name", 200, 500)
        self.hardware.install(self.software)
        self.assertIn(self.software, self.hardware.software_components)
        self.assertEqual(1, len(self.hardware.software_components))

        self.hardware.uninstall(self.software)
        self.assertNotIn(self.software, self.hardware.software_components)
        self.assertEqual(0, len(self.hardware.software_components))


if __name__ == "__main__":
    main()
