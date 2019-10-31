class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0
        self.direction = 'N'

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))
        print("I'm heading {} at {} kph".format(self.direction, self.speed))

    def accelerate(self):
        if self.speed != 120:
            self.speed += 5
        else:
            pass

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time

    def turn_left(self):
        directions = ['N', 'S', 'E', 'W']
        current_index = directions.index(self.direction)
        new_index = current_index + 3
        self.direction = directions[new_index % 4]

    def turn_right(self):
        directions = ['N', 'S', 'E', 'W']
        current_index = directions.index(self.direction)
        new_index = current_index + 1
        self.direction = directions[new_index % 4]








if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                 "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOSLR" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        elif action == 'L':
            my_car.turn_left()
        elif action == 'R':
            my_car.turn_right()

        my_car.step()
        my_car.say_state()