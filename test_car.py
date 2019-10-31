import unittest

from Car import Car


class TestCar(unittest.TestCase):
      def setUp(self):
          self.car = Car()


class TestInit(TestCar):
      def test_initial_speed(self):
          self.assertEqual(self.car.speed, 0)

      def test_initial_odometer(self):
          self.assertEqual(self.car.odometer, 0)

      def test_initial_time(self):
          self.assertEqual(self.car.time, 0)

      def test_initial_direction(self):
          self.assertEqual(self.car.direction, 'N')

class TestAccelerate(TestCar):
      def test_accelerate_from_zero(self):
          self.car.accelerate()
          self.assertEqual(self.car.speed, 5)

      def test_multiple_accelerates(self):
          for _ in range(3):
            self.car.accelerate()
          self.assertEqual(self.car.speed, 15)

      def  test_max_speed(self):
          for _ in range(50):
              self.car.accelerate()
          self.assertEqual(self.car.speed, 120)


class TestBrake(TestCar):
       def test_brake_once(self):
           self.car.accelerate()
           self.car.brake()
           self.assertEqual(self.car.speed, 0)

       def test_multiple_brakes(self):
            for _ in range(5):
                self.car.accelerate()
            for _ in range(3):
                self.car.brake()
            self.assertEqual(self.car.speed, 10)

       def test_should_not_allow_negative_speed(self):
           self.car.brake()
           self.assertEqual(self.car.speed, 0)

       def test_multiple_brakes_at_zero(self):
           for _ in range(3):
               self.car.brake()
           self.assertEqual(self.car.speed, 0)


class TestTurning(TestCar):

    def test_turn_left(self):
        self.car.turn_left()
        self.assertEqual(self.car.direction, 'W')

    def test_turn_right(self):
        self.car.turn_right()
        self.assertEqual(self.car.direction, 'S')

    def test_multiple_turns(self):
        self.car.turn_left()
        self.car.turn_left()
        self.car.turn_right()
        self.car.turn_left()
        self.car.turn_right()
        self.car.turn_right()
        self.car.turn_right()
        self.car.turn_left()
        self.assertEqual(self.car.direction, 'N')



