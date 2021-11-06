class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if room.take_room(people) is None:
                    self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                guests = room.guests
                if room.free_room() is None:
                    self.guests -= guests

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {','.join([str(room.number) for room in self.rooms if not room.is_taken])}\n" \
               f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}"

