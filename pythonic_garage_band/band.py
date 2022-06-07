class Musician:
    instruments = ["guitar", "bass", "drums"]
    sounds = ["face melting guitar solo", "bom bom buh bom", "rattle boom crash"]

    def __init__(self, name):
        self.name = name

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def get_instrument(self):
        pass

    def play_solo(self):
        pass


class Guitarist(Musician):
    instrument = Musician.instruments[0]
    sound = Musician.sounds[0]

    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.sound


class Bassist(Musician):
    instrument = Musician.instruments[1]
    sound = Musician.sounds[1]

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.sound


class Drummer(Musician):
    instrument = Musician.instruments[2]
    sound = Musician.sounds[2]

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.sound


class Band(Musician):
    solos = []
    instances = []

    def __init__(self, name, members):
        self.members = members
        self.instances.append(self)
        super(Band, self).__init__(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_instrument(self):
        return self.members

    def play_solos(self):
        for member in self.members:
            self.solos.append(member.play_solo())
        return self.solos

    @classmethod
    def to_list(cls):
        return cls.instances
