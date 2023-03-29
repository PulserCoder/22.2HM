
class Unit:
    def __init__(self, field, state='fly', x=0, y=0):
        self.field = field
        self.speed = 1
        self.state = state
        self.x = x
        self.y = y

    def move(self, direction):
        speed = self._get_speed()
        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)
    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        raise ValueError('something wrong')