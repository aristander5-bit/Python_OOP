class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


car = Car("a", "b", 1, 4)
car.make = ""
print(car)



from unittest import TestCase,main


class CarTests(TestCase):

    def test_init_sets_attributes_correctly(self):
        car = Car("BMW", "X3", 8.5, 60)
        self.assertEqual(car.make, "BMW")
        self.assertEqual(car.model, "X3")
        self.assertEqual(car.fuel_consumption, 8.5)
        self.assertEqual(car.fuel_capacity, 60)
        self.assertEqual(car.fuel_amount, 0)

    def test_make_empty_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            Car("", "X3", 8.5, 60)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def model_empty_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            Car("BMW", "", 8.5, 60)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_model_empty_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            Car("BMW", "", 8.5, 60)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_zero_or_negative_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            Car("BMW", "X3", 0, 60)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            Car("BMW", "X3", -2.5, 60)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_zero_or_negative_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            Car("BMW", "X3", 8.5, 0)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            Car("BMW", "X3", 8.5, -50)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_negative_raises_exception(self):
        car = Car("BMW", "X3", 8.5, 60)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -10
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel_zero_or_negative_raises_exception(self):
        car = Car("BMW", "X3", 8.5, 60)
        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

        with self.assertRaises(Exception) as ex:
            car.refuel(-15)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_adds_fuel_successfully(self):
        car = Car("BMW", "X3", 8.5, 60)
        car.refuel(30)
        self.assertEqual(car.fuel_amount, 30)

    def test_refuel_exceeds_capacity_caps_at_capacity(self):
        car = Car("BMW", "X3", 8.5, 60)
        car.refuel(80)
        self.assertEqual(car.fuel_amount, 60)

    def test_drive_not_enough_fuel_raises_exception(self):
        car = Car("BMW", "X3", 10, 60)
        car.refuel(5)
        with self.assertRaises(Exception) as ex:
            car.drive(100)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive_reduces_fuel_amount_successfully(self):
        car = Car("BMW", "X3", 10, 60)
        car.refuel(30)
        car.drive(100)
        self.assertEqual(car.fuel_amount, 20)


if __name__ == "__main__":
    main()