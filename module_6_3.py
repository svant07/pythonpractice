class Horse:
    def __init__(self, x_distance, sound):
        self.x_distance = x_distance
        self.sound = sound

    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        x_distance = self.x_distance * dx


class Eagle:
    def __init__(self, y_distance, sound):
        self.y_distance = y_distance
        self.sound = sound

    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        y_distance = self.y_distance * dy


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance, sound, y_distance):
        super().__init__()
        #super().__init__(sound)
        #super().__init__(y_distance)

    def move(self, dx, dy):
        Horse.fly()
        Eagle.run()

    def get_pos(self):
        a = (self.x_distance, self.y_distance)
        return a

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
