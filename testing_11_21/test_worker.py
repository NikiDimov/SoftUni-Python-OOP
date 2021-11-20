class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."


# -----------------------------------------------------------------
from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Test", 1000, 100)

    def test_correct_initialization(self):
        self.assertEqual('Test', self.worker.name)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(1000, self.worker.salary)

    def test_workers_energy_incrementation(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_worker_tries_to_work_with_negative_energy(self):
        worker = Worker("Test", 1000, -2)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_tries_to_work_with_0_energy(self):
        worker = Worker("Test", 1000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_money_increased_energy_decreased(self):
        self.worker.work()
        self.assertEqual(1000, self.worker.money)
        self.assertEqual(99, self.worker.energy)

    def test_get_info(self):
        self.assertEqual("Test has saved 0 money.", self.worker.get_info())


if __name__ == "__main__":
    main()
