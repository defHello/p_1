
# rooms = [{"name": "Kitchen", "lenght": 6, "width": 4},
#          {"name": "Kitchen", "lenght": 5.5, "width": 4.5},
#          {"name": "Kitchen", "lenght": 5, "width": 4},
#          {"name": "Kitchen", "lenght": 7, "width": 6.3},]
# for room in rooms:
#     area = room["lenght"] * room["width"]
#     print(area)

def area(rooms_dict):
    return rooms_dict["name"], rooms_dict["length"] * rooms_dict["width"]

rooms = [{"name": "Kitchen", "length": 6, "width": 4},
         {"name": "room_1", "length": 5.5, "width": 4.5},
         {"name": "room_2", "length": 5, "width": 4},
         {"name": "room_3", "length": 7, "width": 6.3},]

area_room = list(map(area, rooms ))
area_dict = dict(area_room)
print(area_dict)
