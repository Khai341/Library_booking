active_rooms = set()

def mark_room_online(room_number):
    active_rooms.add(room_number)

def mark_room_offline(room_number):
    active_rooms.discard(room_number)

def get_online_room_numbers():
    return list(active_rooms)