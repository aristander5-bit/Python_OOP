from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    fuel = 35.6
    horse_power = 112.5

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_class_attributes_types(self):
        self.assertIsInstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float)
        self.assertIsInstance(self.vehicle.fuel_consumption, float)
        self.assertIsInstance(self.vehicle.fuel, float)
        self.assertIsInstance(self.vehicle.capacity, float)
        self.assertIsInstance(self.vehicle.horse_power, float)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_success(self):
        self.vehicle.drive(5)
        self.assertEqual(29.35, self.vehicle.fuel)

    def test_drive_fail(self):
        self.vehicle.fuel = 1
        with self.assertRaises(Exception) as e:
            self.vehicle.drive(1.5)
        self.assertEqual("Not enough fuel", str(e.exception))

    def test_refuel_success(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(2.5)
        self.assertEqual(3.5, self.vehicle.fuel)

    def test_refuel_fail(self):
        self.vehicle.fuel = 35
        with self.assertRaises(Exception) as e:
            self.vehicle.refuel(2.3)
        self.assertEqual("Too much fuel", str(e.exception))

    def test_str(self):
        expected = f"The vehicle has {self.horse_power} " \
               f"horse power with {self.fuel} fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.vehicle))




if __name__ == "__main__":
    main()