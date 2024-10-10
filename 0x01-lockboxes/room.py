def canVisitAllRooms(rooms):
    unlocked = [False] * len(rooms)
    unlocked[0] = True
    keys = [0]
    
    for key in keys:
        for new_key in rooms[key]:
            if new_key < len(rooms)  and not unlocked[new_key]:
                unlocked[new_key] = True
                keys.append(new_key)
    return all(unlocked)
rooms = [[1], [2], [3], []]
print(canVisitAllRooms(rooms))  # Output: True

rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(canVisitAllRooms(rooms))  # Output: False