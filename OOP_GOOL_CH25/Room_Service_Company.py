
class Room():
    def __init__(self, size, num_of_windows, directions):
        self.size = size
        self.num_of_windows = num_of_windows
        self.directions = directions
        for direction in self.directions:
            if direction != "west" and direction != "east" and direction != "south" and direction != "north":
                raise ValueError("Not a valid direction.")


    def __repr__(self):
        str = f"size: {self.size} m^2, num of windows: {self.num_of_windows}, directions: {self.directions}"
        return str

    def get_rent_price(self):
        rent_price = int((self.size + (self.num_of_windows/ 2))*80)
        return rent_price


room = Room(122.3, 4, ['west', 'east'])
print(room)
print(room.get_rent_price())


class MeetingRoom(Room):
    def __init__(self, size, num_of_windows, directions, table_size):
        super().__init__(size, num_of_windows, directions)
        self.table_size = table_size

    def __repr__(self):
        s = Room.__repr__(self) + f", table_size: {self.table_size}"
        return s

    def get_rent_price(self):
        rent_price = int((self.size + (self.num_of_windows/ 2))*80 + self.table_size*7)
        return rent_price

a = MeetingRoom(120, 5, ['north', 'west'], 8)
print(a)

print(a.get_rent_price())


class Building():
    def __init__(self,address, rooms):
        self.address = address
        self.rooms = rooms

    def __repr__(self):
        s = f"Address: {self.address} \n"
        rooms_sorted = sorted(self.rooms, key=lambda r:r.size, reverse=True)
        for room in rooms_sorted:
            s += room.__repr__() + "\n"

        return s[:-1]  # to remove the last "\n" from the textual visualization

    def get_room_by_budget(self, budget):
        new_list = []
        for room in self.rooms:
            if room.get_rent_price() <= budget:
                new_list.append(room)
        return new_list

    def get_meeting_room_by_occupancy(self, occupancy):
        new_list = []
        for room in self.rooms:
            if isinstance(room, MeetingRoom):
                if room.table_size >= occupancy:
                    new_list.append(room)
        return new_list



r1 = Room(122.3, 4, ['west', 'east'])
r2 = MeetingRoom(120, 5, ['north', 'west'], 8)
r3 = MeetingRoom(10, 1, ['south'], 2)
b = Building("Tel Aviv", [r2, r3, r1])
print(b)




